from flask import Flask, request, jsonify, render_template
from keras.models import load_model
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
model = load_model(os.path.join(os.getcwd(), 'trained_model.h5')) 

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(file).convert('L')  
        img = img.resize((64, 64))  
        img_array = np.array(img) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)
        img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension

        prediction = model.predict(img_array)
        result = 'Fake' if prediction[0][0] > 0.5 else 'Real'
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
