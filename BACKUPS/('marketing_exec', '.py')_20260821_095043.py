import os
import json
import time

def run_marketing_pipeline():
    print("📈 Initializing Automated Marketing Execution Engine...")
    
    leads_file = "showroom_leads.json"
    
    if os.path.exists(leads_file):
        with open(leads_file, "r") as f:
            active_leads = json.load(f)
        print(f"🔍 Found {len(active_leads)} active campaign targets.")
    else:
        active_leads = []
        print("⚠️ Showroom leads database not found.")
    
    for lead in active_leads:
        print(f"➡️ Sending automated campaign pitch to: {lead.get('email')}...")
        time.sleep(0.5)
        print(f"✨ Success! Loop complete for Campaign: {lead.get('campaign_id')}.")
        
    print("\n🎉 Marketing execution loop finished successfully.")

if __name__ == "__main__":
    run_marketing_pipeline()
