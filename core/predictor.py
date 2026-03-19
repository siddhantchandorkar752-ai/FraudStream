import os
import pickle
import numpy as np
import pandas as pd
import logging
from typing import Dict, Any, Tuple
from config import config

logger = logging.getLogger(__name__)

class FraudPredictor:
    def __init__(self):
        self.model = None
        self.feature_names = None
        self._load()

    def _load(self) -> None:
        if not os.path.exists(config.MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {config.MODEL_PATH}. Run train.py first.")
        with open(config.MODEL_PATH, "rb") as f:
            artifact = pickle.load(f)
        self.model = artifact["model"]
        self.feature_names = artifact["feature_names"]
        logger.info(f"Model loaded from {config.MODEL_PATH}")

    def predict(self, df: pd.DataFrame) -> Tuple[int, float]:
        proba = self.model.predict_proba(df)[0][1]
        label = int(proba >= config.FRAUD_THRESHOLD)
        logger.info(f"Prediction: label={label}, proba={proba:.4f}")
        return label, round(float(proba), 4)

    def get_feature_names(self) -> list:
        return self.feature_names