import pandas as pd
from src.kpis import calculate_kpis
from src.clean import clean_incidents
def test_kpis():
    df=pd.DataFrame({"incident_id":["1","2"],"status":["Resolved","Open"],"mttr_hours":[10,None],"sla_breach":[False,False]})
    k=calculate_kpis(df); assert k["total_incidents"]==2; assert k["open_incidents"]==1; assert k["resolution_rate"]==50.0; assert k["median_mttr_hours"]==10.0
def test_cleaning_removes_duplicates(tmp_path):
    raw=tmp_path/"raw.csv"
    df=pd.DataFrame({"incident_id":["1","1"],"created_at":["2025-01-01","2025-01-01"],"resolved_at":["2025-01-02","2025-01-02"],"category":["Phishing","Phishing"],"severity":["SEV-3","SEV-3"],"source":["SIEM Rule","SIEM Rule"],"assigned_team":[None,None],"business_unit":["IT","IT"],"mttr_hours":[24,24],"sla_breach":[False,False]})
    df.to_csv(raw,index=False); cleaned,meta=clean_incidents(raw)
    assert len(cleaned)==1; assert meta["duplicates_removed"]==1; assert cleaned.iloc[0]["assigned_team"]=="Unassigned"
