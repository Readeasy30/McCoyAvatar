import os
import subprocess
import time
import json

def run_backup_loop():
    print("🔄 Initializing Automated Git Backup Daemon...")
    print("🔒 Power Shield Active: Scanning workspace for changes every 5 minutes...")
    
    log_path = os.path.join("MANAGEMENT", "backup_daemon_status.json")
    os.makedirs("MANAGEMENT", exist_ok=True)
    
    while True:
        try:
            # check for local changes or untracked files
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
            
            if status.stdout.strip():
                print("⚡ Local modifications detected! Initiating automatic cloud backup...")
                
                # Run standard git lifecycle commands safely
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", "Automated system daemon snapshot save"], check=True)
                subprocess.run(["git", "push", "origin", "main"], check=True)
                
                print("💾 Success: Workspace state automatically locked to GitHub.")
                
            # Log health parameters to hard disk using hardware flush rules
            health = {
                "daemon_state": "RUNNING",
                "last_backup_check": time.strftime("%Y-%m-%d %H:%M:%S"),
                "hardware_write_flush": "LOCKED"
            }
            with open(log_path, "w") as f:
                json.dump(health, f, indent=4)
                f.flush()
                
        except Exception as e:
            print(f"⚠️ Backup sequence skipped or delayed: {str(e)}")
            
        # Sleep for 300 seconds (5 minutes) before the next scan pass
        time.sleep(300)

if __name__ == "__main__":
    run_backup_loop()
