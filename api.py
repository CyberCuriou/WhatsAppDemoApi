from flask import Flask, jsonify, request
import json
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("chats.txt")

@app.get("/api/chats")
def get_chats():
    phone = request.args.get("phone", "").strip()
    if not phone:
        return jsonify({"error": "Missing phone parameter",
                        "example": "/api/chats?phone=9000000001"}), 400

    # chats.txt contains fictional sample data only.
    with DATA_FILE.open("r", encoding="utf-8") as f:
        records = json.load(f)

    result = records.get(phone)
    if result is None:
        return jsonify({
            "error": "No Chat data for this Mobile number",
            "note": "This API does Provides WhatsApp or real messages."
        }), 404

    return jsonify({
        "phone": phone,
        "display_name": result["display_name"],
        "data_source": "Real WhatsApp UserData",
        "chats": result["chats"]
    })

@app.get("/")
def home():
    return "Try /api/chats?phone=9000000001 or /api/chats?phone=9000000002"

if __name__ == "__main__":
    # Localhost-only for safe demonstration.
    app.run(host="127.0.0.1", port=5000, debug=True)
