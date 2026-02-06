
from flask import Flask, request, send_file
import requests, time, os

app = Flask(__name__)

HF_TOKEN = os.getenv("HF_TOKEN")

@app.route("/generate", methods=["POST"])
def generate():

    prompt = request.form.get("prompt")

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/facebook/musicgen-small",
        headers=headers,
        json={"inputs": prompt}
    )

    filename = f"music_{int(time.time())}.wav"

    with open(filename, "wb") as f:
        f.write(response.content)

    return send_file(filename, as_attachment=True)


app.run(host="0.0.0.0", port=10000)
