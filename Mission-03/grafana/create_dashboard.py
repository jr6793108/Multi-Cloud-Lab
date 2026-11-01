import json
from pathlib import Path

DATASOURCE = {
    "type": "prometheus",
    "uid": "mission03-prometheus"
}

panels = [
    (
        "Application Availability",
        'up{job="mission03-application"}',
        "stat",
        "short"
    ),
    (
        "HTTP Requests per Second",
        'sum(rate(mission03_http_requests_total[5m]))',
        "timeseries",
        "reqps"
    ),
    (
        "HTTP Response Latency (Average)",
        'sum(rate(mission03_http_request_duration_seconds_sum[5m])) / clamp_min(sum(rate(mission03_http_request_duration_seconds_count[5m])), 0.000001)',
        "timeseries",
        "s"
    ),
    (
        "CPU Utilization",
        '100 * (1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])))',
        "timeseries",
        "percent"
    ),
    (
        "Memory Utilization",
        '100 * (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)',
        "timeseries",
        "percent"
    ),
    (
        "Root Filesystem Utilization",
        '100 * (1 - node_filesystem_avail_bytes{mountpoint="/",fstype!~"tmpfs|overlay"} / node_filesystem_size_bytes{mountpoint="/",fstype!~"tmpfs|overlay"})',
        "timeseries",
        "percent"
    )
]

dashboard_panels = []

for index, (title, expression, panel_type, unit) in enumerate(panels):
    panel = {
        "id": index + 1,
        "title": title,
        "type": panel_type,
        "datasource": DATASOURCE,
        "gridPos": {
            "h": 8,
            "w": 12,
            "x": (index % 2) * 12,
            "y": (index // 2) * 8
        },
        "targets": [
            {
                "expr": expression,
                "refId": "A",
                "datasource": DATASOURCE
            }
        ],
        "fieldConfig": {
            "defaults": {
                "unit": unit
            },
            "overrides": []
        },
        "options": {}
    }

    dashboard_panels.append(panel)

dashboard = {
    "uid": "mission03-monitoring",
    "title": "Mission-03 - Application & Infrastructure Monitoring",
    "tags": ["mission03", "terraform", "prometheus", "grafana"],
    "timezone": "browser",
    "schemaVersion": 41,
    "version": 1,
    "refresh": "15s",
    "time": {
        "from": "now-1h",
        "to": "now"
    },
    "panels": dashboard_panels
}

output = Path("grafana/dashboards/mission03-monitoring.json")
output.write_text(json.dumps(dashboard, indent=2) + "\n")

print(f"Created: {output}")
print(f"Dashboard panels: {len(dashboard_panels)}")
