"""Tool: vibescan_rules — List all available detection rules."""

import json


def run() -> str:
    """List all VibeScan detection rules with descriptions."""
    from vibescan.rules import get_all_rules

    rules_data = []
    for rule in get_all_rules():
        cls_name = type(rule).__name__
        rules_data.append({
            "id": cls_name,
            "name": getattr(rule, "name", cls_name),
            "description": getattr(rule, "description", ""),
        })

    return json.dumps({"rules": rules_data, "total": len(rules_data)}, default=str)
