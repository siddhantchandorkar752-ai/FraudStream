<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,30:0a1628,60:0d3b6e,100:00b4d8&height=280&section=header&text=FRAUDSTREAM&fontSize=90&fontColor=ffffff&fontAlignY=38&desc=Real-Time%20Credit%20Card%20Fraud%20Detection%20API&descAlignY=62&descSize=24&animation=fadeIn" width="100%"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=22&duration=2500&pause=700&color=00B4D8&center=true&vCenter=true&multiline=true&width=850&height=130&lines=Sub-500ms+Fraud+Detection+%7C+Production+REST+API;XGBoost+ROC-AUC+0.9212+%7C+590K+Transactions;FastAPI+%2B+Docker+%2B+Swagger+%7C+Banking-Grade;Every+Transaction+Scored+in+Milliseconds)](https://git.io/typing-svg)

<br/>

<img src="https://img.shields.io/badge/Python-3.11-00b4d8?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-0.110-0d3b6e?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/XGBoost-2.0.3-00b4d8?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Docker-Containerized-0d3b6e?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-1.4-00b4d8?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-LIVE-00ff88?style=for-the-badge"/>

<br/><br/>

> ### *"Banks don't use Streamlit dashboards. They use APIs. This is one."*
> FraudStream exposes a production REST API that scores any credit card transaction in under 500ms — ROC-AUC 0.9212 on 590K real transactions.

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/siddhantchandorkar752-ai/FraudStream)
[![Swagger Docs](https://img.shields.io/badge/API-Swagger_Docs-00b4d8?style=for-the-badge)](http://localhost:8000/docs)

</div>

---

## WHAT IS FRAUDSTREAM?

```
╔══════════════════════════════════════════════════════════════════════╗
║     FRAUDSTREAM — Real-Time Fraud Detection API v1.0                ║
║     "Every second, thousands of transactions. Every one scored."    ║
║                                                                      ║
║     MODEL:     XGBoost — ROC-AUC 0.9212 — 590K transactions        ║
║     API:       FastAPI REST — sub-500ms prediction latency          ║
║     DEPLOY:    Docker containerized — production-ready              ║
║     MONITOR:   Real-time prediction stats — in-memory tracker      ║
╚══════════════════════════════════════════════════════════════════════╝
```

FraudStream is not a dashboard. It is not a notebook. It is a **production-grade REST API** — the same architecture used in real banking fraud detection systems.

> Most ML projects stop at model training. FraudStream starts where they stop.

---

## THE PROBLEM

```
Every second — thousands of credit card transactions globally.
Banks must detect fraud in milliseconds — not minutes.

A slow system = real money lost.
A batch system = fraud already happened.
A notebook demo = useless in production.

FraudStream solves all three.
Sub-500ms. Real-time. Containerized. API-first.
```

| What Banks Need | What Most ML Projects Deliver | What FraudStream Delivers |
|----------------|-------------------------------|--------------------------|
| REST API | Jupyter notebook | FastAPI production API |
| Sub-500ms latency | Batch prediction | 23ms average latency |
| Docker deployment | Local `python main.py` | Fully containerized |
| API documentation | README only | Swagger UI auto-generated |
| Real-time monitoring | None | In-memory prediction tracker |

---

## ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TRANSACTION INPUT (JSON)                          │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
               ┌────────────────────────────┐
               │     FastAPI REST API        │  ← /api/v1/predict
               │     Pydantic validation     │     type-safe schemas
               └──────────────┬─────────────┘
                              │
                              ▼
               ┌────────────────────────────┐
               │      PREPROCESSOR          │  ← Feature alignment
               │   preprocessor.py          │     null handling
               └──────────────┬─────────────┘
                              │
                              ▼
               ┌────────────────────────────┐
               │    XGBOOST CLASSIFIER      │  ← ROC-AUC: 0.9212
               │    210 numeric features    │     scale_pos_weight=10
               └──────────────┬─────────────┘
                              │
                              ▼
               ┌────────────────────────────┐
               │   PREDICTION RESPONSE      │  ← is_fraud, probability
               │   + RISK LEVEL             │     risk_level, latency_ms
               └──────────────┬─────────────┘
                              │
                              ▼
               ┌────────────────────────────┐
               │   PREDICTION MONITOR       │  ← Real-time stats
               │   monitor.py               │     in-memory tracking
               └────────────────────────────┘
```

---

## RISK SCORING SYSTEM

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                      │
│   LOW       0.0 – 0.4   Transaction approved — standard processing  │
│   MEDIUM    0.4 – 0.6   Flag for secondary review                   │
│   HIGH      0.6 – 0.8   Hold transaction — manual review required   │
│   CRITICAL  0.8 – 1.0   BLOCK — fraud confirmed with high confidence│
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## MODEL PERFORMANCE

| Metric | Value | Notes |
|--------|-------|-------|
| **ROC-AUC** | **0.9212** | Primary metric for imbalanced fraud data |
| **Accuracy** | 96% | On held-out test set |
| **Dataset** | IEEE-CIS | 590,540 transactions |
| **Features** | 210 | Numeric, preprocessed |
| **Imbalance** | 3.5% fraud | Handled via `scale_pos_weight=10` |
| **Latency** | ~23ms avg | End-to-end API response |

---

## API ENDPOINTS

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service info + version |
| GET | `/api/v1/health` | Health check + model status |
| POST | `/api/v1/predict` | Fraud prediction — main endpoint |
| GET | `/api/v1/stats` | Real-time monitoring statistics |
| GET | `/docs` | Swagger UI — interactive API docs |

---

## LIVE EXAMPLE

**Request:**
```bash
curl -X POST http://localhost:8000/api/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"TransactionAmt": 15000.0, "ProductCD": "C", "card4": "mastercard"}'
```

**Response:**
```json
{
  "transaction_id": "a1b2c3d4",
  "is_fraud": true,
  "fraud_probability": 0.847,
  "risk_level": "CRITICAL",
  "latency_ms": 23.4,
  "model_version": "1.0.0"
}
```

---

## TECH STACK

| Layer | Technology | Version | Why |
|-------|-----------|---------|-----|
| **API** | FastAPI | 0.110 | Async, typed, Swagger auto-generated |
| **Model** | XGBoost | 2.0.3 | SOTA gradient boosting for tabular fraud data |
| **Validation** | Pydantic v2 | Latest | Type-safe request/response schemas |
| **Data** | pandas + scikit-learn | 1.4 | Feature alignment + preprocessing |
| **Container** | Docker | Latest | Production deployment — zero setup |
| **Orchestration** | docker-compose | Latest | Multi-container management |
| **Config** | python-dotenv | Latest | Secure environment management |

---

## PROJECT STRUCTURE

```
FraudStream/
├── api/
│   ├── main.py           # FastAPI app + middleware + CORS
│   ├── routes.py         # All API endpoint definitions
│   └── schemas.py        # Pydantic request/response models
├── core/
│   ├── predictor.py      # XGBoost model loader + inference
│   ├── preprocessor.py   # Feature alignment + null handling
│   └── monitor.py        # Real-time prediction stats tracker
├── models/               # Trained model artifacts (.pkl)
├── data/                 # Training data (gitignored)
├── train.py              # Model training script
├── config.py             # Centralized configuration
├── Dockerfile            # Production container definition
├── docker-compose.yml    # Multi-container orchestration
├── requirements.txt
└── .env.example
```

---

## QUICK START

### Option 1 — Docker (Recommended)
```bash
git clone https://github.com/siddhantchandorkar752-ai/FraudStream.git
cd FraudStream
pip install -r requirements.txt
python train.py
docker build -t fraudstream .
docker run -p 8000:8000 -v $(pwd)/models:/app/models fraudstream
```

### Option 2 — Local
```bash
git clone https://github.com/siddhantchandorkar752-ai/FraudStream.git
cd FraudStream
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train.py
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

Visit: `http://localhost:8000/docs`

---

## WHAT I LEARNED

- **Production APIs are not demos** — FastAPI + Pydantic v2 enforce contracts that Streamlit never could
- **Docker is non-negotiable** — packaging model artifacts with dependencies is the difference between "works on my machine" and "works everywhere"
- **Class imbalance in fraud** — `scale_pos_weight` changes everything; accuracy alone is a lie on 3.5% fraud rate
- **Swagger is free documentation** — FastAPI generates interactive API docs automatically from type hints
- **Latency matters** — 23ms average means this can run in real banking middleware, not just demos

---

## WHY THIS STANDS OUT

```
Average ML portfolio:   Jupyter notebook → accuracy score → done.

FraudStream:            Train → Package → REST API → Docker → Swagger
                        → Real-time monitoring → Sub-500ms latency
                        → Production architecture banks actually use
```

---

## LICENSE

MIT License — free to use, modify, distribute.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:0d3b6e,100:000000&height=70&text=Siddhant%20Chandorkar&fontSize=30&fontColor=00b4d8&fontAlign=50&fontAlignY=50" width="500"/>

<br/><br/>

[![GitHub](https://img.shields.io/badge/GitHub-siddhantchandorkar752--ai-0d3b6e?style=for-the-badge&logo=github&logoColor=white)](https://github.com/siddhantchandorkar752-ai)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-siddhantchandorkar-00b4d8?style=for-the-badge&logo=huggingface&logoColor=white)](https://siddhantchandorkar-fraudstream.hf.space/docs)

<br/>

*"Most engineers build models. I build systems banks can actually deploy."*

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00b4d8,40:0d3b6e,100:000000&height=140&section=footer&text=FRAUDSTREAM%20v1.0&fontSize=34&fontColor=ffffff&fontAlignY=68&animation=fadeIn" width="100%"/>

</div>
