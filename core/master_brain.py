import os
import json
from groq import Groq

class MasterBrain:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def execute_quantum_analysis(self, telemetry, image_data):
        """Live Groq calculation for Dimensional Overwrite and Metallurgy."""
        prompt = f"""
        ACT AS: Chief Scientist.
        INPUT: {telemetry} | IMAGE_DATA: {image_data}
        EQUATIONS TO SOLVE: 
        1. Unified Grand Prophetic Equation (Psi_G).
        2. Apex Dimensional Overwrite (ADO) Law.
        3. Law of Dimensional Overwrite (Manual Override).
        
        STUDY PARAMETERS: 
        Stoichiometry, Metallurgy, Gemology, Meteorology, and Solar Farming potential.
        
        TASK:
        Determine if current terrain supports 'Building Location' status.
        Translate math into rover velocity (v) commands.
        
        RETURN: JSON with [psi_g_val, ado_result, nav_cmd, mineral_profile, solar_yield]
        """
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
