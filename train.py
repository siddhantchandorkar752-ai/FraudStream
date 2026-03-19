import os
import sys
import pickle
import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from xgboost import XGBClassifier

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

def load_data() -> pd.DataFrame:
    trans_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "train_transaction.csv")
    iden_path  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "train_identity.csv")
    if not os.path.exists(trans_path):
        raise FileNotFoundError(f"Dataset not found at {trans_path}")
    logger.info("Loading transaction data...")
    transaction = pd.read_csv(trans_path, engine="python", encoding="latin-1", on_bad_lines="skip")
    logger.info("Loading identity data...")
    identity = pd.read_csv(iden_path, engine="python", encoding="latin-1", on_bad_lines="skip")
    df = transaction.merge(identity, on="TransactionID", how="left")
    logger.info(f"Merged shape: {df.shape}")
    return df

def preprocess(df: pd.DataFrame):
    logger.info("Preprocessing...")
    df = df[df.columns[df.isnull().mean() < 0.5]]
    df = df.select_dtypes(include=["number"])
    df = df.fillna(df.median())
    target = config.TARGET_COLUMN
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found.")
    X = df.drop(columns=[target])
    y = df[target]
    logger.info(f"Features: {X.shape[1]} | Samples: {X.shape[0]}")
    return X, y, list(X.columns)

def train(X, y):
    logger.info("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    logger.info("Training XGBoost...")
    model = XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        scale_pos_weight=10,
        random_state=42,
        eval_metric="auc",
        verbosity=0,
    )
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, proba)
    logger.info(f"\n{classification_report(y_test, preds)}")
    logger.info(f"ROC-AUC: {auc:.4f}")
    return model

def save(model, feature_names):
    os.makedirs(os.path.dirname(config.MODEL_PATH), exist_ok=True)
    with open(config.MODEL_PATH, "wb") as f:
        pickle.dump({"model": model, "feature_names": feature_names}, f)
    logger.info(f"Model saved -> {config.MODEL_PATH}")

if __name__ == "__main__":
    df = load_data()
    X, y, feature_names = preprocess(df)
    model = train(X, y)
    save(model, feature_names)
    logger.info("Training complete!")