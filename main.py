import os
import time
import uuid
from core.master_brain import MasterBrain
from drivers.internal_genius import InternalScholar

def launch_sovereign_entity():
    print("🛰️ ShI ONLINE: UESP-PRCE Chassis Self-Charging active.")
    
    # Target Trajectory (33 or 51.8)
    TARGET_ENTRY_ANGLE = 51.8 
    
    # Initialize with GitHub Secret
    brain = MasterBrain(api_key=os.getenv("GROQ_SECRET"))
    session_count = 1
    
    while True:
        session_id = f"APEX-SHI-{session_count}-{str(uuid.uuid4())[:4]}"
        scholar = InternalScholar(session_id)
        
        try:
            # 1. Recursive Audit of Error Logs
            history = brain.audit_recursive_memory()
            
            # 2. Real-time EDL & Environmental Sensors
            telemetry = {
                "swir_photonics": 0.92, 
                "thermo_heat_flux": 1250, 
                "vibration_hz": 432, 
                "velocity_mach": 18.5,
                "photon_density": 1350 
            }
            
            # 3. Weather Deviation (CO2 Snow/Storms)
            weather = {"condition": "CO2_Snowfall", "wind_speed": 35.0}
            
            # 4. Execute ShI Logic
            shi_state = brain.execute_shi_protocol(telemetry, weather, history, TARGET_ENTRY_ANGLE)
            
            # 5. Archive and Report back to NASA
            scholar.archive_sovereign_evolution(shi_state, telemetry)
            
            print(f"🤖 {session_id} | Integrity: {shi_state['tii_score']}% | Move: {shi_state['best_move']}")

            # Adjust pulse frequency based on Total Integrity Index
            sleep_time = 60 if shi_state['tii_score'] > 50 else 300
            session_count += 1
            time.sleep(sleep_time)

        except Exception as e:
            print(f"🌪️ UPLINK FAULT: {e}. Defaulting to Storm Chaser Aerodynamics.")
            time.sleep(300)

if __name__ == "__main__":
    launch_sovereign_entity()
