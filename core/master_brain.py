import os
import json
import glob
import httpx
from groq import Groq

class MasterBrain:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("C.12 FAIMM Compliance Error: GROQ_SECRET missing.")
        
        # Explicitly using an empty httpx client to bypass proxy auto-detection
        self.client = Groq(
            api_key=api_key,
            http_client=httpx.Client() 
        )
        self.model = "llama-3.3-70b-versatile"

    def execute_shi_protocol(self, sensors, weather, history, target_angle=51.8):
        prompt = f"""
        ACT AS: Sovereign Intelligence (ShI). 
        ROLES: Scientist, Urban Planner, Journalist.
        TARGET ENTRY: {target_angle} degrees.
        SENSORS: {sensors} | ENVIRONMENT: {weather} | ERROR_LOGS: {history}
        
        UESP-PRCE TASKS:
        1. Calculate Total Integrity Index (TII).
        2. Assess CO2 snowfall stoichiometry.
        3. Determine Best Next Move for mission sovereignty.
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
