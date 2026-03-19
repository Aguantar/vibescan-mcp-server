"""Tool: vibescan_scan — Scan a project directory for security issues."""

import json
from pathlib import Path


def run(path: str = ".", min_severity: str = "info") -> str:
    """Run VibeScan on the specified directory and return results as JSON."""
    from vibescan.collector import collect
    from vibescan.models import Severity
    from vibescan.rules import get_all_rules

    target = Path(path).resolve()
    if not target.exists():
        return json.dumps({"error": f"Path does not exist: {path}"})
    if not target.is_dir():
        return json.dumps({"error": f"Path is not a directory: {path}"})

    try:
        threshold = Severity(min_severity.lower())
    except ValueError:
        return json.dumps({
            "error": f"Invalid severity '{min_severity}'. Choose from: critical, high, medium, low, info"
        })

    ctx = collect(target)

    all_issues = []
    for rule in get_all_rules():
        all_issues.extend(rule.run(ctx))

    filtered = [i for i in all_issues if i.severity >= threshold]
    filtered.sort(key=lambda i: (-i.severity.rank, i.file, i.line or 0))

    issues_data = []
    for issue in filtered:
        issues_data.append({
            "severity": issue.severity.value,
            "rule": issue.rule_id,
            "file": issue.file,
            "line": issue.line,
            "message": issue.message,
            "fix": issue.fix,
        })

    # Summary by severity
    severity_counts = {}
    for issue in filtered:
        sev = issue.severity.value
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    result = {
        "project_root": str(target),
        "files_scanned": len(ctx.text_files),
        "files_skipped": len(ctx.skipped_files),
        "total_issues": len(filtered),
        "severity_counts": severity_counts,
        "issues": issues_data,
    }

    return json.dumps(result, default=str)
