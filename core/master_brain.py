import os
import json
from groq import Groq

class MasterBrain:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("C.12 FAIMM Compliance Error: GROQ_SECRET missing.")
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def calculate_sovereign_physics(self, artemis_telemetry):
        """Processes Artemis Sensor Suite via Unified Grand Prophetic Equation."""
        prompt = f"""
        ROLES: NASA AI Scientist (C.12 FAIMM Lead), Geologist, Metallurgist.
        ARTEMIS SENSOR INPUT: {artemis_telemetry}
        
        TASKS:
        1. Solve Unified Grand Prophetic Equation (Psi_G) for navigation vectors.
        2. Apply Law of Dimensional Overwrite (ADO) to Artemis Lidar/SWIR data.
        3. Determine Building Locations (1, 2, 3...) based on Gemology and Metallurgy.
        4. Calculate Solar Farming efficiency & Horticulture potential (pH/Salts).
        5. Propose Modular Prefab Container Vacuum Solutions for the target body.
        
        RETURN: JSON ONLY [psi_g, ado_status, nav_cmd, building_location_id, solar_yield, stoichiometry_report].
        """
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
