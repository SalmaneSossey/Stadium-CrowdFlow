# Stadium CrowdFlow — Task Board

## MVP goal
Predict congestion by **time + zone** and show **recommendations** on a dashboard.

## Workstreams (owners)
### 1) Frontend (Dashboard)
Owner: Ali
- Heatmap / risk by zone
- Timeline chart
- Recommendations panel (actions list)

### 2) Backend (API)
Owner: Salmane
- /health
- /predict  -> input: time, zone, context -> output: risk_score (+ confidence)
- /recommend -> input: risk_score + context -> output: actions list

### 3) ML baseline
Owner: Mathyiss
- Baseline model (forecasting/classification)
- Evaluation metric (e.g., MAE/F1)
- Save model artifact or provide reproducible training script

### 4) Pitch & Story
Owner: Mohamed
- Problem + stakeholders + Morocco 2030 framing
- Value proposition + impact (KPIs)
- Demo script (60–90 seconds)
