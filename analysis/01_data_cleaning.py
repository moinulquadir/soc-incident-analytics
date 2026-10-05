from src.clean import clean_incidents
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
df,meta=clean_incidents(); df.to_csv(ROOT/"data/clean/incidents_clean.csv",index=False); print(meta)
