import os
import time
import uuid
from core.master_brain import MasterBrain
from drivers.internal_genius import InternalScholar

def run_union_protocol():
    print("🛰️ ShI UNION INITIALIZED: Groq + AI Hive + Puter Cloud.")
    
    TARGET_ANGLE = 51.8 
    
    # Initialize using the GitHub Action Secret
    api_key = os.getenv("GROQ_SECRET")
    brain = MasterBrain(api_key=api_key)
    session_count = 1
    
    while True:
        session_id = f"APEX-{session_count}-{str(uuid.uuid4())[:4]}"
        scholar = InternalScholar(session_id)
        
        try:
            history = brain.audit_recursive_memory()
            telemetry = {"vibration_hz": 432, "velocity_mach": 18.5}
            weather = {"condition": "CO2_Snowfall", "wind_speed": 45.0}
            
            # Execute Sovereign Logic via Groq
            shi_state = brain.execute_shi_protocol(telemetry, weather, history, TARGET_ANGLE)
            scholar.archive_sovereign_evolution(shi_state, telemetry)
            
            print(f"🤖 {session_id} | TII: {shi_state['tii_score']}% | Move: {shi_state['best_move']}")

            # Adaptive Pulse Timing
            time.sleep(60 if shi_state['tii_score'] > 50 else 300)
            session_count += 1

        except Exception as e:
            print(f"🌪️ UNION DISRUPTED: {e}. Re-syncing with Cloud...")
            time.sleep(300)

if __name__ == "__main__":
    run_union_protocol()
