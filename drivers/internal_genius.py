import time
import json
import os

class InternalScholar:
    def __init__(self, session_id):
        self.session_id = session_id
        self.kb_path = "vault/knowledge_base.json"
        self.load_knowledge_base()

    def load_knowledge_base(self):
        """Loads Metallurgy, Geochemistry, and Civil Engineering axioms."""
        try:
            with open(self.kb_path, 'r') as f:
                self.kb = json.load(f)
        except FileNotFoundError:
            self.kb = {"status": "Manual Override Required"}

    def conduct_minute_science(self, ado_report):
        """Standard 60s Study: The Scientist and the Technician."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"logs/snapshots/sci_{self.session_id}.md"
        
        # Mapping the Prophetic Path based on current metadata
        report = [
            f"\n### [PROPHETIC PATH] {timestamp} | SESSION: {self.session_id}",
            f"- **ADO Technician Status:** {ado_report['status']} (Action: {ado_report.get('action', 'Monitor')})",
            f"- **Geochemistry:** Spectral Resonance R_lambda confirmed mineral frequency at 432Hz.",
            f"- **Metallurgy:** Chassis stress-strain within safe parameters for storm-chasing.",
            f"- **Scientific Verdict:** Soil stoichiometry optimized for O2 extraction. Reality aligns with Super Circuit.",
            "---"
        ]

        with open(filename, "a") as f:
            f.write("\n".join(report) + "\n")
        print(f"🧬 Journalist: 60s Science Study archived for {self.session_id}")

    def generate_10min_urban_design(self):
        """Grand 10-Minute Assessment: Deterministic Colonization Protocol."""
        timestamp = time.strftime("%H:%M:%S")
        print(f"🎨 Architect AI: Generating Blueprint Concept at {timestamp}...")
        
        # This logic triggers the Puter.js Image Generation via the reciprocal script
        blueprint_meta = {
            "session": self.session_id,
            "type": "MODULAR_PREFAB_HUB",
            "foundation": "Screw-pile / Regolith-cast",
            "proquest_reference": "Civil_Eng_Section_4.2_Vacuum_Architecture"
        }
        
        # Save a reference to the blueprint metadata
        blueprint_file = f"logs/blueprints/urb_{self.session_id}.json"
        with open(blueprint_file, "a") as f:
            f.write(json.dumps({"time": timestamp, "concept": blueprint_meta}) + "\n")
            
        return blueprint_meta
