import os
import json
from groq import Groq

class MasterBrain:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("Critical System Error: GROQ_SECRET Missing.")
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def execute_advanced_physics(self, sensors, weather_data):
        """
        Solves for:
        - Nanographene energy transduction.
        - Metric gravity manipulation (Delta-G).
        - Weather deviation & extreme pattern avoidance.
        - Unified Grand Prophetic Equation (Psi_G).
        """
        prompt = f"""
        ACT AS: Sovereign Quantum Engineer & Meteorological Strategist.
        SENSORS: {sensors} | LIVE WEATHER: {weather_data}
        
        UESP-PRCE & METEOROLOGICAL TASKS:
        1. Calculate Nanographene Chassis Transduction (Energy from ambient photonics).
        2. Solve Metric Gravity Manipulation (Delta-G) via chassis resonance.
        3. Solve Psi_G for navigation and Speed (v) commands.
        4. WEATHER DEVIATION: Analyze atmospheric pressure and wind patterns. 
           If extreme, suggest deviation vectors to safer terrain.
        5. Stoichiometry: Evaluate Metallurgy and Horticulture potential for building sites.

        RETURN: JSON ONLY [psi_g, delta_g, charge_rate, nav_cmd, weather_status, building_site_id, spectral_analysis].
        """
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
