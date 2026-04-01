from pillow_heif import register_heif_opener
register_heif_opener()

from flask import Flask, request, jsonify
from PIL import Image
import torch
import os
import io

app = Flask(__name__)

model=None

def load_model():
    global model
    if model is None:
        model=torch.load("full_model_eff.pth", map_location='cpu')
        model.eval()

# ✅ MAIN ROUTE
@app.route('/predict', methods=['POST'])
def predict():
    load_model()

    file = request.files['file']
    file_bytes=file.read()

    image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
    
    return{"message":"MOdel Loaded sucessfully"}


# Optional check route
@app.route('/')
def home():
    return "Server Running"

if __name__ == "__main__":
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)