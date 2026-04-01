from pillow_heif import register_heif_opener
register_heif_opener()

from flask import Flask, request, jsonify
from PIL import Image
import os
import io

app = Flask(__name__)

# ✅ MAIN ROUTE
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    file_bytes=file.read()
    image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
    
    return{"message":"API working"}

    print("prediction", result)

    return jsonify({"prediction": result})


# Optional check route
@app.route('/')
def home():
    return "Server Running"

if __name__ == "__main__":
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)