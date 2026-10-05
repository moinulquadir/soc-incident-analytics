"""Streamlit dashboard for the SOC Incident Analytics portfolio."""
from pathlib import Path
import sys,pandas as pd,streamlit as st,plotly.express as px
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from src.kpis import calculate_kpis
DATA=ROOT/"data/clean/incidents_clean.csv"
st.set_page_config(page_title="SOC Incident Analytics",page_icon="🛡️",layout="wide")
st.title("🛡️ SOC Incident Analytics"); st.caption("Synthetic security operations data • Python • SQL • Streamlit")
if not DATA.exists(): st.error("Clean data not found. Run: python run_pipeline.py"); st.stop()
df=pd.read_csv(DATA); k=calculate_kpis(df)
c1,c2,c3,c4,c5=st.columns(5)
c1.metric("Incidents",f'{k["total_incidents"]:,}'); c2.metric("Open",f'{k["open_incidents"]:,}'); c3.metric("Resolution rate",f'{k["resolution_rate"]:.1f}%'); c4.metric("Median MTTR",f'{k["median_mttr_hours"]:.1f}h'); c5.metric("SLA breach rate",f'{k["sla_breach_rate"]:.1f}%')
left,right=st.columns(2)
with left:
    trend=df.groupby("month",as_index=False).size().rename(columns={"size":"incidents"}); st.plotly_chart(px.line(trend,x="month",y="incidents",markers=True,title="Incident volume over time"),use_container_width=True)
with right:
    sev=df.groupby("severity",as_index=False).size().rename(columns={"size":"incidents"}); st.plotly_chart(px.bar(sev,x="severity",y="incidents",title="Incidents by severity"),use_container_width=True)
left,right=st.columns(2)
with left:
    team=df[df.status.eq("Resolved")].groupby("assigned_team",as_index=False).agg(avg_mttr=("mttr_hours","mean"),incidents=("incident_id","count")); team["avg_mttr"]=team["avg_mttr"].round(1)
    st.plotly_chart(px.bar(team.sort_values("avg_mttr"),x="avg_mttr",y="assigned_team",orientation="h",title="Average MTTR by team"),use_container_width=True)
with right:
    cat=df.groupby("category",as_index=False).size().rename(columns={"size":"incidents"}); st.plotly_chart(px.pie(cat,names="category",values="incidents",title="Incident mix by category"),use_container_width=True)
st.subheader("Incident Explorer")
sev_filter=st.multiselect("Severity",sorted(df.severity.unique()),default=sorted(df.severity.unique()))
status_filter=st.multiselect("Status",sorted(df.status.unique()),default=sorted(df.status.unique()))
view=df[df.severity.isin(sev_filter)&df.status.isin(status_filter)]
st.dataframe(view.sort_values("created_at",ascending=False),use_container_width=True,hide_index=True)
