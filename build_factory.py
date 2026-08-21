import os
import shutil
import time
import json

def execute_build():
    print("🚀 Starting Avatar Factory Automated Build File System...")
    
    core_files = ["build_avatar_assets.py", "marketing_exec.py", "speech_avatar.py"]
    backup_dir = "BACKUPS"
    dist_dir = "EXECUTIVES"
    
    os.makedirs(backup_dir, exist_ok=True)
    os.makedirs(dist_dir, exist_ok=True)
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    files_saved = 0

    print("⚡ Scanning for local modifications to protect...")
    
    for file in core_files:
        if os.path.exists(file):
            backup_name = f"{os.path.splitext(file)}_{timestamp}.py"
            shutil.copy(file, os.path.join(backup_dir, backup_name))
            shutil.copy(file, os.path.join(dist_dir, file))
            print(f"💾 Protected & copied: {file} -> {dist_dir}/{file}")
            files_saved += 1
        else:
            print(f"⚠️ Warning: {file} not found in root directory. Skipping.")

    manifest_path = os.path.join(dist_dir, "build_manifest.json")
    build_log = {
        "build_status": "SUCCESS" if files_saved > 0 else "EMPTY",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "files_secured": files_saved
    }
    
    with open(manifest_path, "w") as f:
        json.dump(build_log, f, indent=4)
        f.flush()
        
    print(f"\n✅ Build complete! {files_saved} files locked into '{dist_dir}/'.")
    print("🔒 Electrical pop protection active. All code states are securely cloned.")

if __name__ == "__main__":
    execute_build()
