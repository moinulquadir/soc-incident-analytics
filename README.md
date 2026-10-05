# SOC Incident Analytics

A recruiter-ready cybersecurity analytics portfolio project using synthetic SOC incident data.

## Quick start

```bash
pip install -r requirements.txt
python run_pipeline.py
streamlit run dashboard/app.py
```

Run tests with `pytest -q`.

## What this demonstrates

Python/Pandas data cleaning, SQL incident analysis, SOC KPIs including MTTR and SLA breach rate, an interactive Streamlit/Plotly dashboard, automated tests, and GitHub Actions CI.

## Security concepts

**MTTR:** how quickly incidents are resolved.  
**SLA breach:** an incident that takes longer than its allowed resolution target.  
**Synthetic data:** generated data used so this public portfolio does not expose real security telemetry or PII.

## Disclaimer

This is a learning/portfolio project using synthetic data.