from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

# 1. Load the secret file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-key-123") # Default key if .env fails

company_info = {
    "name": "Brito JR Construction LLC",
    "owner": "Michael Brito",

    # 2. THE FIX: If .env is missing, use these strings as backup
    "phone": os.getenv("COMPANY_PHONE") or "475-312-5251",
    "email": os.getenv("COMPANY_EMAIL") or "britojr.construction@gmail.com"
}


# Updated Service Data
services_data = [
    {
        "id": "roofing",
        "title": "Roofing",
        "short_desc": "Rubber & Asphalt Roof Specialist",
        "details": ["Rubber roof", "Asphalt roof", "Leak Repair"],
        "icon": "/static/img/rooficon.png",
        "long_description": "Your roof is your home's first line of defense. We specialize in long-lasting EPDM Rubber roofing for flat roofs and architectural shingles for residential homes.",
        "video_url": "",
        "gallery": ["/static/img/roof1.jpg"]
    },
    {
        "id": "siding",
        "title": "Siding",
        "short_desc": "Vinyl Siding & Restoration",
        "details": ["Vinyl Siding", "Trim Work", "Insulation"],
        "icon": "/static/img/sideicon.png",
        "long_description": "Boost your curb appeal and energy efficiency with premium vinyl siding. We handle everything from tear-down to Tyvek wrapping and final installation.",
        "video_url": "",
        "gallery": ["/static/img/side1.jpg"]
    },
    {
        "id": "decking",
        "title": "Decking",
        "short_desc": "Custom Decks & Patios",
        "details": ["Composite", "Wood", "Railings"],
        "icon": "/static/img/deckicon.png",
        "long_description": "Expand your living space outdoors. Whether you want maintenance-free composite decking or traditional pressure-treated wood, we build solid structures.",
        "video_url": "",
        "gallery": ["/static/img/deck1.jpg"]
    },
    {
        "id": "snow-removal",
        "title": "Roof Snow & Ice Dam Removal",
        "short_desc": "Winter Roof Protection",
        "details": ["Snow Shoveling", "Ice Dam Prevention", "Gutter Clearing"],
        "icon": "/static/img/rooficon.png",
        "long_description": "Protect your home's structural integrity during harsh winters. We safely clear heavy snow from your roof to prevent frozen gutters, dangerous ice dams, and costly interior water damage.",
        "video_url": "",
        "gallery": ["/static/img/roof1.jpg"]
    }
]

projects_data = [
    {
        "name": "Full Home Siding",
        "type": "",
        "image": "/static/img/imgbr1.jpeg",
        "video_id": ""  # This is a PHOTO
    },
    {
        "name": "Decking",
        "type": "Custom Deck",
        "image": "", # Leave empty, we will auto-grab the YouTube thumbnail
        "video_id": "YZoG0-2R59k" # This is a VIDEO
    },
    {
        "name": "Roofing",
        "type": "",
        "image": "/static/img/roofing1.jpeg",
        "video_id": ""  # This is a PHOTO
    },
    {
        "name": "Full Home Siding",
        "type": "",
        "image": "",
        "video_id": "P1oRVVNUjps"
    },
    {
        "name": "Decking",
        "type": "Custom Deck",
        "image": "/static/img/decking1.jpeg",
        "video_id": ""
    },
    {
        "name": "Roofing",
        "type": "",
        "image": "/static/img/roofing2.jpeg",
        "video_id": ""
    },
    {
        "name": "Full Home Improvement",
        "type": "",
        "image": "",
        "video_id": "7lbPuBh5nPU"
    },
    {
        "name": "Decking",
        "type": "Custom Deck",
        "image": "/static/img/decking2.jpeg",
        "video_id": ""
    },
    {
        "name": "Roofing",
        "type": "",
        "image": "/static/img/roofing3.jpeg",
        "video_id": ""
    },
    {
        "name": "Full Home Siding",
        "type": "",
        "image": "",
        "video_id": "hUkhHkyBVqE"
    },
    {
        "name": "Decking",
        "type": "Custom Deck",
        "image": "/static/img/decking3.jpeg",
        "video_id": ""
    },
    {
        "name": "Roofing",
        "type": "",
        "image": "/static/img/roofing4.jpeg",
        "video_id": ""
    },
    {
        "name": "Full Home Siding",
        "type": "",
        "image": "/static/img/siding1.jpeg",
        "video_id": ""
    },
    {
        "name": "Decking",
        "type": "Custom Deck",
        "image": "",
        "video_id": "XGUWGbZjifI"
    },
    {
        "name": "Roofing",
        "type": "",
        "image": "/static/img/roofing5.jpeg",
        "video_id": ""
    },
    {
        "name": "Full Home Siding",
        "type": "",
        "image": "/static/img/siding2.jpeg",
        "video_id": ""
    },
    {
        "name": "Full Home Siding",
        "type": "",
        "image": "/static/img/siding3.jpeg",
        "video_id": ""
    },
    {
        "name": "Decking",
        "type": "Custom Deck",
        "image": "",
        "video_id": "KIieR1wpY1c"
    },
    {
        "name": "Stone Siding",
        "type": "",
        "image": "",
        "video_id": "a_iZuZ99Pcs"
    },
]

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html',
                           company=company_info,
                           services=services_data,
                           projects=projects_data)

@app.route('/service/<service_id>')
def service_detail(service_id):
    service = next((item for item in services_data if item["id"] == service_id), None)
    if service:
        return render_template('service_detail.html', service=service, company=company_info)
    return "Service not found", 404

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    message = request.form.get('message')
    print(f"NEW LEAD: {name} | {phone}")
    return "Message Received!"

if __name__ == '__main__':
    app.run(debug=True)