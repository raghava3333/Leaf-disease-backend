from pillow_heif import register_heif_opener
register_heif_opener()
from flask import Flask, request, jsonify
from PIL import Image
import os
import io
import torchvision.transforms as transforms

app = Flask(__name__)

# Load model
model = torch.load("full_model_eff.pth", map_location='cpu')
model.eval()

# Class names (VERY IMPORTANT)
class_names = [
    'Anthracnose fruit',
    'Anthracnose leaf',
    'Bacterial Canker fruit',
    'Gall_Mid leaf',
    'Healthy fruit',
    'Healthy leaf'
]

# Transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# ✅ MAIN ROUTE
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    file_bytes=file.read()
    image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
    
    return{"message":"API working"}
    image = transform(image).unsqueeze(0)

    result = class_names[predicted.item()]

    print("prediction", result)

    return jsonify({"prediction": result})


# Optional check route
@app.route('/')
def home():
    return "Server Running"

if __name__ == "__main__":
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)