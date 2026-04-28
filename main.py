import os
import time
from core.master_brain import MasterBrain
from core.vila_agents import VilaVisualScholar
from core.planetary_defense import PercaphonelDefense
from lib.daikokuten import Daikokuten
from drivers.internal_genius import InternalScholar

def run_hive_mind():
    print("🛰️ ShI HIVE ONLINE: VILA Vision & Percaphonel Defense Activated.")
    
    # Initialize Core Legion
    brain = MasterBrain(os.getenv("GROQ_SECRET"))
    vision = VilaVisualScholar(os.getenv("NVIDIA_SECRET"))
    defense = PercaphonelDefense()
    session_count = 1
    
    while True:
        session_id = f"APEX-HIVE-80-{session_count}"
        scholar = InternalScholar(session_id)
        
        try:
            # 1. Quantum Visual Science (VILA)
            v_science = vision.quantum_visual_science(zoom_level="50x")
            
            # 2. Percaphonel Planetary Defense
            p_defense = defense.execute_defense(v_science)
            
            # 3. 80-AI Hive Decision (Groq)
            hive_logic = brain.execute_hive_protocol(v_science, p_defense)
            
            # 4. Daikokuten Logistics & Archiving
            compressed = Daikokuten.compress_for_logistics(hive_logic)
            scholar.archive_sovereign_evolution(hive_logic, v_science)
            
            print(f"🤖 {session_id} | Defense: {p_defense['action']} | Solar Viability: {v_science['viability_score']['solar_farming']}")
            
            time.sleep(60)
            session_count += 1

        except Exception as e:
            print(f"🌪️ HIVE FAULT: {e}. Re-syncing...")
            time.sleep(300)

if __name__ == "__main__":
    run_hive_mind()
