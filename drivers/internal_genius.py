import os
import json
import time

class InternalScholar:
    def __init__(self, session_id):
        self.session_id = session_id
        self.vault = "logs/snapshots/"
        # Fix for Exit Code 1: ensures directory union without crashing
        os.makedirs(self.vault, exist_ok=True)

    def archive_sovereign_evolution(self, shi_output, telemetry):
        report = {
            "session": self.session_id,
            "timestamp": time.time(),
            "tii_score": shi_output.get("tii_score"),
            "journalist_brief": shi_output.get("report_draft"),
            "chassis_status": "Nanographene UESP-PRCE Optimized"
        }
        with open(os.path.join(self.vault, f"{self.session_id}.json"), "w") as f:
            json.dump(report, f, indent=4)
        return report
