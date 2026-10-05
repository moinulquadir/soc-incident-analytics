# Project Overview
## Architecture
generate_data.py → data/raw/incident_tickets.csv → src/clean.py → data/clean/incidents_clean.csv → src/kpis.py / sql/ → dashboard/app.py
## Data-quality controls
The synthetic source deliberately contains duplicate tickets, missing assignment-team values, unresolved/open incidents, and numeric fields requiring coercion.
## Interview discussion
Synthetic data was chosen intentionally: it demonstrates the complete workflow without exposing operational security data. In production, the same transformations could consume sanitized SIEM/ITSM exports.
