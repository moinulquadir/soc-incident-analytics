"""Clean and enrich raw SOC incident data."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def clean_incidents(path=None):
    path=Path(path or ROOT/"data/raw/incident_tickets.csv")
    df=pd.read_csv(path,parse_dates=["created_at","resolved_at"]); before=len(df)
    dup=int(df.duplicated().sum()); df=df.drop_duplicates().copy()
    df["assigned_team"]=df["assigned_team"].fillna("Unassigned")
    df["status"]=df["resolved_at"].isna().map({True:"Open",False:"Resolved"})
    df["mttr_hours"]=pd.to_numeric(df["mttr_hours"],errors="coerce")
    df["month"]=df["created_at"].dt.to_period("M").astype(str)
    return df,{"raw_rows":before,"duplicates_removed":dup,"clean_rows":len(df)}
if __name__=="__main__":
    out=ROOT/"data/clean/incidents_clean.csv"; out.parent.mkdir(parents=True,exist_ok=True)
    df,meta=clean_incidents(); df.to_csv(out,index=False); print(meta)
