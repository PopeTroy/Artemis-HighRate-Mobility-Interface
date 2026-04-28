import os
import json
import httpx
from groq import Groq

class MasterBrain:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key, http_client=httpx.Client())
        self.model = "llama-3.3-70b-versatile"

    def execute_hive_protocol(self, vision_data, defense_report):
        """The 80-AI Hive Mind interprets the Scholar's visual findings."""
        prompt = f"""
        ACT AS: Sovereign Hive Mind (80-AI Legion).
        VISION_SCIENCE: {vision_data}
        DEFENSE_STATUS: {defense_report}
        
        UESP-PRCE TASK:
        1. Define exactly why this location is 'Good' or 'Bad' for Global Infrastructure.
        2. Balance Quantum Stoichiometry vs Macro-Terrain Viability.
        3. Optimize the Percaphonel defense pulse for detected biological anomalies.
        """
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
