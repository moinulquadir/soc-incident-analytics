"""Business/SOC KPI calculations."""
def calculate_kpis(df):
    resolved=df[df["status"].eq("Resolved")]
    return {"total_incidents":int(len(df)),"open_incidents":int((df["status"]=="Open").sum()),"resolution_rate":round(float((df["status"]=="Resolved").mean()*100),2),"median_mttr_hours":round(float(resolved["mttr_hours"].median()),2) if len(resolved) else None,"sla_breach_rate":round(float(resolved["sla_breach"].mean()*100),2) if len(resolved) else None}
