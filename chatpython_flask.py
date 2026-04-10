from flask import Flask, request, jsonify

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def get_response(user):
    user = user.lower()

    if user in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you with your hotel needs today? 😊"

    elif user in ["bye", "goodbye", "exit"]:
        return "Thank you for visiting! Have a great day 😊"

    elif "room" in user:
        return "We offer Deluxe, Standard, and Suite rooms."

    elif "price" in user or "cost" in user:
        return "Prices start from ₹2000 per night."

    elif "book" in user:
        return "Sure! Please provide your name and dates."

    elif "check in" in user or "check-in" in user:
        return "Check-in time is 2 PM."

    elif "check out" in user or "check-out" in user:
        return "Check-out time is 11 AM."

    elif "wifi" in user:
        return "Yes, we provide free WiFi."

    elif "breakfast" in user:
        return "Complimentary breakfast is included."

    elif "parking" in user:
        return "Free parking is available."

    elif "location" in user:
        return "We are located in the city center."

    elif "contact" in user:
        return "You can call us at +91-9876543210."

    elif "cancel" in user:
        return "Free cancellation within 24 hours."

    elif "restaurant" in user:
        return "Yes, we have an in-house restaurant."

    elif "gym" in user:
        return "Yes, gym access is available."

    elif "pool" in user:
        return "We have a swimming pool."

    elif "pet" in user:
        return "Sorry, pets are not allowed."

    elif "payment" in user:
        return "We accept cash, card, and UPI."

    elif "offer" in user:
        return "We have seasonal discounts available!"

    elif "family" in user:
        return "Yes, family rooms are available."

    elif "single" in user:
        return "Yes, single rooms are available."

    elif "help" in user:
        return "You can ask about rooms, booking, facilities, etc."

    else:
        return "Sorry, I didn't understand that. Try asking something else."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
