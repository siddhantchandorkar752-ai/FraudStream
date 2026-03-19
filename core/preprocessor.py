import os
import pandas as pd
import numpy as np
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

EXPECTED_FEATURES: List[str] = []

def load_feature_names(path: str) -> List[str]:
    import pickle
    with open(path, "rb") as f:
        return pickle.load(f)

def preprocess_transaction(data: Dict[str, Any], feature_names: List[str]) -> pd.DataFrame:
    df = pd.DataFrame([data])
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0.0
    df = df[feature_names]
    df = df.fillna(0.0)
    df = df.select_dtypes(include=[np.number])
    logger.info(f"Preprocessed transaction shape: {df.shape}")
    return df