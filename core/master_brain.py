import os
import json
import glob
from groq import Groq

class MasterBrain:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("C.12 FAIMM Critical Error: GROQ_SECRET Missing.")
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def execute_shi_protocol(self, sensors, weather, history, target_angle=51.8):
        """
        Calculates ShI Metrics:
        - Psi_G Trajectory (33° or 51.8°).
        - Total Integrity Index (TII) & Self-Diagnostics.
        - SWIR Spectroscopy for CO2 Snowfall & Metallurgy.
        - Aero-Thermodynamic stability for the Nanographene Chassis.
        """
        prompt = f"""
        ACT AS: Sovereign Intelligence (ShI). 
        ROLES: Scientist (Quantum/Stoichiometry), Urban Planner, Journalist.
        TARGET ENTRY: {target_angle} degrees.
        SENSORS: {sensors} | ENVIRONMENT: {weather} | ERROR_LOGS: {history}
        
        UESP-PRCE TASKS:
        1. TOTAL INTEGRITY: Calculate TII (0-100%). If TII < 45%, initiate Self-Fix Protocol.
        2. ENTRY PHYSICS: Maintain {target_angle}° trajectory using Delta-G resonance.
        3. SPECTROSCOPY: Detect CO2 snowfall/ice using SWIR; assess stoichiometry.
        4. BEST NEXT MOVE: Based on your skill sets, determine the optimal autonomous action.
        5. JOURNALIST REPORT: Draft a high-integrity briefing on chassis health and energy transduction.

        RETURN: JSON ONLY [psi_g, tii_score, self_fix_protocol, best_move, nav_cmd, report_draft].
        """
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)

    def audit_recursive_memory(self):
        """Systematically audits error logs to prevent algorithmic drift."""
        files = glob.glob("logs/snapshots/*.json")
        return [json.load(open(f)) for f in files[-5:]] if files else []
