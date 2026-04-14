import os
import json
from groq import Groq

class MasterBrain:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def analyze_terrain_and_physics(self, sensor_data, image_meta):
        """
        Solves: Unified Grand Prophetic Equation & Dimensional Overwrite.
        Analyzes: Metallurgy, Gemology, and Solar Potential.
        """
        prompt = f"""
        ROLES: Scientist, Geologist, Quantum Physicist.
        DATA: {sensor_data} | IMAGE_META: {image_meta}
        TASKS:
        1. Calculate the Unified Grand Prophetic Equation (Psi_G).
        2. Apply Law of Dimensional Overwrite (D_O) to verify terrain stability.
        3. Analyze for: Stoichiometry, Metallurgy (Iron/Magnesium), and Gemology.
        4. Evaluate Horticulture/Agriculture potential in Regolith.
        5. Recommend Solar Farm placement based on Artemis camera imagery.
        6. Commands: Speed up, Slow down, or Stop based on D_O results.
        RETURN: JSON with keys [equations, study_report, navigation_commands, location_id]
        """
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
