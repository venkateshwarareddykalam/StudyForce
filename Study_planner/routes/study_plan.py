from flask import Blueprint, request, jsonify
import google.generativeai as genai
from config import GEMINI_API_KEY

study_bp = Blueprint("study", __name__)

genai.configure(api_key=GEMINI_API_KEY)

@study_bp.route("/generate-study-plan", methods=["POST"])
def generate_study_plan():
    data = request.json
    subjects = ", ".join(data.get("subjects", []))
    study_hours = data.get("study_hours", "2")
    strengths = ", ".join(data.get("strengths", []))
    weaknesses = ", ".join(data.get("weaknesses", []))
    goals = data.get("goals", "Improve academic performance")

    prompt = f"""Create a structured and personalized study plan for a student.  
- Subjects: {subjects}  
- Daily Study Time: {study_hours} hours  
- Strengths: {strengths}  
- Weaknesses: {weaknesses}  
- Goal: {goals}  

### **Response Format:**  
Generate the study plan as a **structured text**, ensuring that each **week** is stored in a numbered **Week array** format.

#### **Example Response Format:**
**Week 1**
Monday: 9:00 AM - 10:30 AM: Math
Tuesday: 10:00 AM - 11:30 AM: Science

**Week 2**
Monday: 8:00 AM - 9:30 AM: English
Tuesday: 9:30 AM - 11:00 AM: Physics
"""


    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        study_plan = response.text

        return jsonify({"study_plan": study_plan})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
