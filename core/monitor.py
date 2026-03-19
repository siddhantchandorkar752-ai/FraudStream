import logging
import time
from collections import deque
from typing import Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class PredictionMonitor:
    def __init__(self, window_size: int = 1000):
        self.window_size = window_size
        self.predictions = deque(maxlen=window_size)
        self.latencies = deque(maxlen=window_size)
        self.start_time = datetime.now()

    def record(self, label: int, proba: float, latency_ms: float) -> None:
        self.predictions.append({"label": label, "proba": proba, "ts": datetime.now().isoformat()})
        self.latencies.append(latency_ms)

    def get_stats(self) -> Dict[str, Any]:
        if not self.predictions:
            return {"total": 0, "fraud_rate": 0.0, "avg_latency_ms": 0.0}
        total = len(self.predictions)
        fraud_count = sum(1 for p in self.predictions if p["label"] == 1)
        avg_latency = sum(self.latencies) / len(self.latencies)
        return {
            "total_predictions": total,
            "fraud_count": fraud_count,
            "legitimate_count": total - fraud_count,
            "fraud_rate": round(fraud_count / total, 4),
            "avg_latency_ms": round(avg_latency, 2),
            "uptime_seconds": round((datetime.now() - self.start_time).total_seconds(), 1),
        }