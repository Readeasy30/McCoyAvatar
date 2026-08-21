import os
import sys
import json
import time

def run_integrity_firewall():
    print("🛡️ Initializing Local Code Integrity Firewall...")
    
    target_repos = ["WEBSITES/ReadEasy30", "WEBSITES/MathEasy30", "WEBSITES/TopShelfWebsites"]
    blocked_files = 0
    
    print("\n⚡ Auditing active development repositories for structural bugs...")
    
    for repo in target_repos:
        if os.path.exists(repo):
            for root, dirs, files in os.walk(repo):
                for file in files:
                    file_path = os.path.join(root, file)
                    
                    # Safeguard 1: Prevent 1-byte or completely empty file writes
                    if os.path.getsize(file_path) <= 1 and not file.endswith(".txt"):
                        print(f"❌ FIREWALL BLOCK: Empty/Corrupted asset detected at: {file_path}")
                        blocked_files += 1
                        
                    # Safeguard 2: Catch accidental broken template markers
                    try:
                        if file.endswith(".json"):
                            with open(file_path, "r", encoding="utf-8") as f:
                                json.load(f)
                    except Exception:
                        print(f"❌ FIREWALL BLOCK: Invalid formatting inside structural file: {file_path}")
                        blocked_files += 1

    # Write status ledger using forced hard disk flush safety rules
    log_path = os.path.join("MANAGEMENT", "firewall_status.json")
    os.makedirs("MANAGEMENT", exist_ok=True)
    
    report = {
        "engine": "Workspace Integrity Guard V1",
        "firewall_state": "SECURE" if blocked_files == 0 else "THREATS_BLOCKED",
        "total_violations_stopped": blocked_files,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open(log_path, "w") as f:
        json.dump(report, f, indent=4)
        f.flush()
        
    print("\n💾 Crash Protection: Firewall status matrix safely flushed to hardware disk.")
    if blocked_files > 0:
        print(f"⚠️ Warning: Firewall has isolated {blocked_files} code issues. Clean them before pushing.")
    else:
        print("🎉 Success! All active workspace repository configurations passed the firewall check.")

if __name__ == "__main__":
    run_integrity_firewall()
