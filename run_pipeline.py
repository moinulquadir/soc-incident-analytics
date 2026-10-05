"""Build the dataset and clean layer in one command."""
from generate_data import generate,OUT
from src.clean import clean_incidents,ROOT
OUT.parent.mkdir(parents=True,exist_ok=True); generate().to_csv(OUT,index=False)
cleaned,meta=clean_incidents(OUT)
dest=ROOT/"data/clean/incidents_clean.csv"; dest.parent.mkdir(parents=True,exist_ok=True)
cleaned.to_csv(dest,index=False); print(f"Pipeline complete: {meta}; output={dest}")
