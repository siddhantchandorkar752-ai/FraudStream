import time
import uuid
import logging
import pandas as pd
from fastapi import APIRouter, HTTPException, Depends
from api.schemas import TransactionRequest, PredictionResponse, HealthResponse
from core.predictor import FraudPredictor
from core.preprocessor import preprocess_transaction
from core.monitor import PredictionMonitor

logger = logging.getLogger(__name__)

router = APIRouter()
monitor = PredictionMonitor()
_predictor: FraudPredictor = None

def get_predictor() -> FraudPredictor:
    global _predictor
    if _predictor is None:
        _predictor = FraudPredictor()
    return _predictor

def get_risk_level(proba: float) -> str:
    if proba >= 0.8:
        return "CRITICAL"
    elif proba >= 0.6:
        return "HIGH"
    elif proba >= 0.4:
        return "MEDIUM"
    return "LOW"

@router.get("/health", response_model=HealthResponse, tags=["System"])
def health_check(predictor: FraudPredictor = Depends(get_predictor)):
    stats = monitor.get_stats()
    return HealthResponse(
        status="healthy",
        model_loaded=predictor.model is not None,
        total_predictions=stats["total_predictions"],
        fraud_rate=stats["fraud_rate"],
        avg_latency_ms=stats["avg_latency_ms"],
        uptime_seconds=stats["uptime_seconds"],
    )

@router.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
def predict(
    transaction: TransactionRequest,
    predictor: FraudPredictor = Depends(get_predictor)
):
    start = time.perf_counter()
    try:
        data = transaction.model_dump()
        df = preprocess_transaction(data, predictor.get_feature_names())
        label, proba = predictor.predict(df)
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        monitor.record(label, proba, latency_ms)
        return PredictionResponse(
            transaction_id=str(uuid.uuid4()),
            is_fraud=bool(label),
            fraud_probability=proba,
            risk_level=get_risk_level(proba),
            latency_ms=latency_ms,
        )
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats", tags=["Monitoring"])
def get_stats():
    return monitor.get_stats()