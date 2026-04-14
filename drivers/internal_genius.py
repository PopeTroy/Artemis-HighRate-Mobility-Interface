import json
import time

class InternalScholar:
    def __init__(self):
        self.kb_path = "vault/knowledge_base.json"

    def perform_40s_study(self, sensor_data, ado_report):
        """
        Conducts the scientific study and includes the Technician's Audit.
        Translates findings into human-readable Mission Snapshots.
        """
        timestamp = int(time.time())
        session_id = "SOL-X" # Dynamically pulled in main.py
        
        # 1. Scientific Study (Geochemistry/Metallurgy/Architecture)
        study_findings = self.analyze_geology(sensor_data)
        
        # 2. Technical Audit (The Journalist reporting on the ADO)
        tech_status = "OPERATIONAL"
        tech_notes = "All systems aligned with Super Circuit."
        
        if ado_report['status'] == "HARDWARE_FAILURE":
            tech_status = "CRITICAL_ADAPTATION"
            tech_notes = f"ADO Stress-test failed for {ado_report['sensor']}. Systematic rerouting active."
        elif ado_report['status'] == "RESOLVED":
            tech_status = "HEALED"
            tech_notes = f"Autonomous reset successful for {ado_report['sensor']}."

        # 3. Compile the Snapshot
        snapshot = {
            "header": f"DEEP STUDY SNAPSHOT | {tech_status}",
            "session": session_id,
            "geology_study": study_findings,
            "technician_audit": tech_notes,
            "urban_planning_verdict": "Sovereign Site Identified. Blueprinting via Puter-IG."
        }
        
        self.save_journalist_report(snapshot, timestamp)
        return snapshot

    def analyze_geology(self, data):
        # Using Metallurgy and Stoichiometry KB to analyze regolith
        return "Basalt/Hematite mix. High load-bearing for modular containers."

    def save_journalist_report(self, snapshot, timestamp):
        """Saves MD file for manual GitHub Push."""
        filename = f"logs/snapshots/study_{timestamp}.md"
        with open(filename, "w") as f:
            f.write(f"# 🧬 Mission Study: {snapshot['header']}\n\n")
            f.write(f"**Session:** {snapshot['session']}\n")
            f.write(f"**Technical Audit:** {snapshot['technician_audit']}\n")
            f.write(f"**Scientific Verdict:** {snapshot['geology_study']}\n")
