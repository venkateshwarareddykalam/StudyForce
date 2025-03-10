from flask import Blueprint, request, jsonify
from firebase_setup import db

progress_bp = Blueprint("progress", __name__)

@progress_bp.route("/update", methods=["POST"])
def update_progress():
    data = request.json
    user_id = data.get("user_id")
    progress = data.get("progress", {})

    db.collection("users").document(user_id).update({"progress": progress})
    return jsonify({"message": "Progress updated successfully!"})
