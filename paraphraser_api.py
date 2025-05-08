from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/paraphrase", methods=["POST"])
def paraphrase():
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"다음 영어 문장을 더 자연스럽고 사람 말투로 바꿔줘:\n\n{text}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        result = response["choices"][0]["message"]["content"].strip()
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

