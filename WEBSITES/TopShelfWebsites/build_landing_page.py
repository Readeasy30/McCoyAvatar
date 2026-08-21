import os
import time

def generate_leasing_landing_page():
    print("🎨 WEBSITE DIRECTOR: Drafting High-Converting Leasing Landing Page...")
    
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Top Shelf Websites - Premium Website Leasing</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0F172A; color: #E2E8F0; line-height: 1.6; padding: 40px; }
        .container { max-width: 1200px; margin: 0 auto; text-align: center; }
        h1 { color: #38BDF8; font-size: 2.5rem; margin-bottom: 10px; }
        .subtitle { color: #94A3B8; font-size: 1.2rem; margin-bottom: 40px; }
        .pricing-grid { display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; margin-top: 20px; }
        .price-card { background-color: #1E293B; border-radius: 12px; padding: 30px; width: 280px; border-top: 5px solid #38BDF8; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        .price-card.popular { border-top-color: #F59E0B; }
        .plan-name { font-size: 1.5rem; font-weight: bold; margin-bottom: 10px; }
        .plan-price { font-size: 2rem; color: #F8FAFC; font-weight: bold; margin-bottom: 20px; }
        .features { list-style: none; padding: 0; margin: 0 0 30px 0; text-align: left; font-size: 0.95rem; color: #CBD5E1; }
        .features li { margin-bottom: 10px; }
        .features li::before { content: "✓ "; color: #10B981; font-weight: bold; }
        .btn { display: inline-block; background-color: #0EA5E9; color: #FFF; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold; }
        .btn.popular { background-color: #F59E0B; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Smart Website Leasing for Local Businesses</h1>
        <p class="subtitle">Get a professional, AI-accelerated online presence without the huge upfront cost.</p>
        
        <div class="pricing-grid">
            <!-- Plan 1 -->
            <div class="price-card">
                <div class="plan-name">START Plan</div>
                <div class="plan-price">$59<span style="font-size:1rem;color:#94A3B8">/mo</span></div>
                <ul class="features">
                    <li>Professional Standard Setup</li>
                    <li>Mobile Responsive Design</li>
                    <li>Secure Fast Hosting</li>
                    <li>Basic Monthly Updates</li>
                </ul>
                <a href="#" class="btn">Lease Now</a>
            </div>
            
            <!-- Plan 2 -->
            <div class="price-card popular">
                <div class="plan-name" style="color:#F59E0B">GROW Plan</div>
                <div class="plan-price">$99<span style="font-size:1rem;color:#94A3B8">/mo</span></div>
                <ul class="features">
                    <li>Advanced Custom Setup</li>
                    <li>Integrated Lead Capture</li>
                    <li>Priority Maintenance</li>
                    <li>Marketing Copy Tools</li>
                </ul>
                <a href="#" class="btn popular">Most Popular</a>
            </div>
            
            <!-- Plan 3 -->
            <div class="price-card">
                <div class="plan-name">PRO Plan</div>
                <div class="plan-price">$149<span style="font-size:1rem;color:#94A3B8">/mo</span></div>
                <ul class="features">
                    <li>Full Enterprise Solutions</li>
                    <li>Advanced Business Tracking</li>
                    <li>Dedicated Avatar Automation</li>
                    <li>24/7 Priority Support</li>
                </ul>
                <a href="#" class="btn">Go Pro</a>
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    target_path = "WEBSITES/TopShelfWebsites/index.html"
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_template)
        f.flush() # Force hardware disk write immediately
        
    print(f"💾 Crash Protection: Premium landing page markup flushed to: {target_path}")
    print("🎉 Success! Website templates are updated for production deployment.")

if __name__ == "__main__":
    generate_leasing_landing_page()
