from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

# Load the secret file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


company_info = {
    "name": "Brito JR Construction LLC",
    "owner": "Michael Brito",
    # Now Python pulls the data from the secret file
    "phone": os.getenv("COMPANY_PHONE"),
    "email": os.getenv("COMPANY_EMAIL")
}

# We store services in a List of Dictionaries.
# This makes it easy to add more later without changing the HTML.
services_data = [
    {
        "title": "Roofing",
        "details": ["Rubber roof", "Asphalt roof"],
        "icon": "/static/img/rooficon.png"
    },
    {
        "title": "Siding",
        "details": ["Vinyl Siding"],
        "icon": "/static/img/sideicon.png"
    },
    {
        "title": "Decking",
        "details": ["All types of decking"],
        "icon": "/static/img/deckicon.png"
    }
]

projects_data = [
    {
        "name": "Historic Home Siding",
        "type": "Vinyl Siding",
        "description": "Complete restoration of a 1920s home using premium vinyl siding.",
        "image": "/static/img/imgbr1.jpeg" # Example Image
    },
    {
        "name": "Newark Roof Repair",
        "type": "Rubber Roof",
        "description": "Commercial flat roof repair using EPDM rubber.",
        "image": "/static/img/imgbr1.jpeg" # Example Image
    }
]


# --- ROUTES ---
@app.route('/')
def home():
    # We pass the data TO the template
    return render_template('index.html',
                           company=company_info,
                           services=services_data,
                           projects=projects_data)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    message = request.form.get('message')

    print(f"NEW LEAD: {name} | {phone} | {message}")

    return "Message Received! (We will make this pretty later)"

if __name__ == '__main__':
    app.run(debug=True)