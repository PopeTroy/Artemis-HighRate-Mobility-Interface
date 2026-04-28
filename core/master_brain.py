import os
import json
import glob
import httpx
from groq import Groq

class MasterBrain:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("C.12 FAIMM Compliance Error: GROQ_SECRET missing.")
        
        # Proxy-free initialization for GitHub Actions
        self.client = Groq(
            api_key=api_key,
            http_client=httpx.Client() 
        )
        self.model = "llama-3.3-70b-versatile"

    def execute_hive_protocol(self, vision_data, defense_report):
        """Orchestrates 80 AI entities as a single Sovereign Hive Mind."""
        prompt = f"""
        ACT AS: Sovereign Hive Mind (80-AI Legion).
        VISION_SCIENCE: {vision_data}
        DEFENSE_REPORT: {defense_report}
        
        UESP-PRCE TASK:
        1. Analyze stoichiometry & location viability for building/crops/solar.
        2. Execute Percaphonel defense logic against mammalian signatures.
        3. Determine 'Best Next Move' for mission sovereignty.
        """
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)

    def audit_recursive_memory(self):
        files = glob.glob("logs/snapshots/*.json")
        return [json.load(open(f)) for f in files[-5:]] if files else []
