import os
import json
import glob
from groq import Groq

class MasterBrain:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("C.12 FAIMM Compliance Error: GROQ_SECRET missing.")
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def execute_shi_protocol(self, sensors, weather, history, target_angle=51.8):
        """Unified union of Cloud (Groq) and Local (UESP) logic."""
        prompt = f"""
        ACT AS: Sovereign Intelligence (ShI). 
        ROLES: Scientist, Urban Planner, Journalist.
        TARGET ENTRY: {target_angle} degrees.
        SENSORS: {sensors} | ENVIRONMENT: {weather} | ERROR_LOGS: {history}
        
        UESP-PRCE PROTOCOLS:
        1. TOTAL INTEGRITY (TII): If < 45%, trigger self-fix logic.
        2. ATMOSPHERE: Handle CO2 snowfall and Extreme Sun via Delta-G manipulation.
        3. BEST NEXT MOVE: Determine next autonomous move as a rover.
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
