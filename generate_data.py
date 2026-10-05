"""Generate a deterministic synthetic SOC incident dataset."""
from pathlib import Path
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parent
OUT=ROOT/"data/raw/incident_tickets.csv"
def generate(n=1200,seed=42):
    rng=np.random.default_rng(seed)
    categories=rng.choice(["Phishing","Malware","Unauthorized Access","Data Loss","DDoS","Misconfiguration"],n,p=[.35,.22,.15,.10,.08,.10])
    severities=rng.choice(["SEV-1","SEV-2","SEV-3","SEV-4"],n,p=[.08,.22,.40,.30])
    teams=rng.choice(["SOC Tier 1","SOC Tier 2","IR Team","IT Ops","App Security"],n)
    sources=rng.choice(["EDR Alert","SIEM Rule","User Report","Email Gateway","Threat Intel"],n)
    units=rng.choice(["Retail Banking","Operations","IT","HR","Finance","Treasury"],n)
    created=pd.Timestamp("2025-01-01")+pd.to_timedelta(rng.integers(0,548,n),unit="D")+pd.to_timedelta(rng.integers(0,24,n),unit="h")
    base={"SEV-1":6,"SEV-2":18,"SEV-3":48,"SEV-4":96}; sla={"SEV-1":4,"SEV-2":24,"SEV-3":72,"SEV-4":120}
    mttr=np.round([base[s]*rng.lognormal(0,.55) for s in severities],1)
    resolved=created+pd.to_timedelta(mttr,unit="h")
    df=pd.DataFrame({"incident_id":[f"INC-{i:05d}" for i in range(1,n+1)],"created_at":created,"resolved_at":resolved,"category":categories,"severity":severities,"source":sources,"assigned_team":teams,"business_unit":units,"mttr_hours":mttr,"sla_breach":[mttr[i]>sla[s] for i,s in enumerate(severities)]})
    df.loc[rng.choice(n,size=int(n*.03),replace=False),["resolved_at","mttr_hours"]]=pd.NA
    df.loc[rng.choice(n,10,replace=False),"assigned_team"]=np.nan
    return pd.concat([df,df.sample(8,random_state=7)],ignore_index=True)
if __name__=="__main__":
    OUT.parent.mkdir(parents=True,exist_ok=True); generate().to_csv(OUT,index=False); print(f"Wrote {OUT}")
