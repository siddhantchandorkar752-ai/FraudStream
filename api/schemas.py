from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class TransactionRequest(BaseModel):
    TransactionAmt: float = Field(..., gt=0, description="Transaction amount in USD")
    ProductCD: Optional[str] = Field(default="W", description="Product code")
    card4: Optional[str] = Field(default="visa", description="Card network")
    card6: Optional[str] = Field(default="debit", description="Card type")
    P_emaildomain: Optional[str] = Field(default="gmail.com", description="Purchaser email domain")
    R_emaildomain: Optional[str] = Field(default="gmail.com", description="Recipient email domain")
    addr1: Optional[float] = Field(default=299.0)
    addr2: Optional[float] = Field(default=87.0)
    dist1: Optional[float] = Field(default=0.0)
    dist2: Optional[float] = Field(default=0.0)
    C1: Optional[float] = Field(default=1.0)
    C2: Optional[float] = Field(default=1.0)
    C3: Optional[float] = Field(default=0.0)
    C4: Optional[float] = Field(default=0.0)
    C5: Optional[float] = Field(default=0.0)
    C6: Optional[float] = Field(default=1.0)
    C7: Optional[float] = Field(default=0.0)
    C8: Optional[float] = Field(default=1.0)
    C9: Optional[float] = Field(default=1.0)
    C10: Optional[float] = Field(default=0.0)
    C11: Optional[float] = Field(default=1.0)
    C12: Optional[float] = Field(default=0.0)
    C13: Optional[float] = Field(default=29.0)
    C14: Optional[float] = Field(default=1.0)
    D1: Optional[float] = Field(default=14.0)
    D2: Optional[float] = Field(default=0.0)
    D3: Optional[float] = Field(default=0.0)
    D4: Optional[float] = Field(default=0.0)
    D5: Optional[float] = Field(default=0.0)
    D6: Optional[float] = Field(default=0.0)
    D7: Optional[float] = Field(default=0.0)
    D8: Optional[float] = Field(default=0.0)
    D9: Optional[float] = Field(default=0.0)
    D10: Optional[float] = Field(default=14.0)
    D11: Optional[float] = Field(default=13.0)
    D12: Optional[float] = Field(default=0.0)
    D13: Optional[float] = Field(default=0.0)
    D14: Optional[float] = Field(default=0.0)
    D15: Optional[float] = Field(default=117.0)
    M1: Optional[str] = Field(default="T")
    M2: Optional[str] = Field(default="T")
    M3: Optional[str] = Field(default="T")
    M4: Optional[str] = Field(default="M0")
    M5: Optional[str] = Field(default="F")
    M6: Optional[str] = Field(default="T")
    M7: Optional[str] = Field(default="F")
    M8: Optional[str] = Field(default="F")
    M9: Optional[str] = Field(default="F")
    V1: Optional[float] = Field(default=1.0)
    V2: Optional[float] = Field(default=1.0)
    V3: Optional[float] = Field(default=1.0)
    V4: Optional[float] = Field(default=1.0)
    V5: Optional[float] = Field(default=1.0)

class PredictionResponse(BaseModel):
    transaction_id: str
    is_fraud: bool
    fraud_probability: float
    risk_level: str
    latency_ms: float
    model_version: str = "1.0.0"

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    total_predictions: int
    fraud_rate: float
    avg_latency_ms: float
    uptime_seconds: float