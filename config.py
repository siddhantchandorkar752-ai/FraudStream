import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    MODEL_PATH: str = os.path.join(BASE_DIR, os.getenv("MODEL_PATH", "models/fraud_model.pkl"))
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", 8000))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    TARGET_COLUMN: str = "isFraud"
    FRAUD_THRESHOLD: float = 0.5

config = Config()