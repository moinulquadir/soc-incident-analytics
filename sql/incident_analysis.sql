-- SOC Incident Analytics: recruiter-facing SQL examples
SELECT severity,COUNT(*) AS incidents,SUM(CASE WHEN status='Resolved' THEN 1 ELSE 0 END) AS resolved,
ROUND(100.0*SUM(CASE WHEN status='Resolved' THEN 1 ELSE 0 END)/COUNT(*),1) AS resolution_rate_pct
FROM incidents_clean GROUP BY severity ORDER BY severity;
SELECT assigned_team,COUNT(*) AS incidents,
ROUND(AVG(CASE WHEN status='Resolved' THEN mttr_hours END),1) AS avg_mttr_hours,
ROUND(100.0*AVG(CASE WHEN status='Resolved' AND sla_breach THEN 1 ELSE 0 END),1) AS sla_breach_pct
FROM incidents_clean GROUP BY assigned_team ORDER BY sla_breach_pct DESC;
SELECT category,COUNT(*) AS incidents,
ROUND(100.0*COUNT(*)/(SELECT COUNT(*) FROM incidents_clean),1) AS share_pct
FROM incidents_clean GROUP BY category ORDER BY incidents DESC;
SELECT month,COUNT(*) AS incidents,SUM(CASE WHEN sla_breach THEN 1 ELSE 0 END) AS sla_breaches
FROM incidents_clean GROUP BY month ORDER BY month;
