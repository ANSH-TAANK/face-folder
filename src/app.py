# from flask import Flask, render_template, request, jsonify
# from model import load_images_from_folders, train_model
# import numpy as np
# import cv2

# # app = Flask(__name__)
# app = Flask(__name__, template_folder='templates')

# # Load and train the model
# real_folder = 'data/real'
# fake_folder = 'data/fake'
# X, y = load_images_from_folders(real_folder, fake_folder) 
# model, le = train_model(X, y)


# @app.route('/')
# def index():
#     print("Index route accessed")  # Add this line for debugging
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     file = request.files['image']
#     img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
#     img = cv2.resize(img, (64, 64)).reshape(1, -1)  # Flatten the image
#     prediction = model.predict(img)
#     label = le.inverse_transform(prediction)[0]
#     return jsonify({'label': label})

# if __name__ == "__main__":
#     app.run(debug=True)




# from flask import Flask, render_template, request, jsonify
# import numpy as np
# import cv2
# from preprocess import load_images_from_folders
# from model import train_model

# app = Flask(__name__, template_folder='templates')

# # Load and train the model
# real_folder = 'data/real'
# fake_folder = 'data/fake'
# X, y = load_images_from_folders(real_folder, fake_folder)
# model, le = train_model(X, y)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     file = request.files['image']
#     img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
#     img = cv2.resize(img, (64, 64)).reshape(1, 64, 64, 1)  # Adjust for input shape
#     img = img.astype('float32') / 255.0  # Normalize
#     prediction = model.predict(img)
#     label = le.inverse_transform(np.argmax(prediction, axis=1))[0]
#     return jsonify({'label': label})

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from keras.models import load_model
# from preprocess import load_data
# import numpy as np

# app = Flask(__name__)

# # Load your trained model
# model = load_model('your_model.h5')  # Update this with the actual model path
# label_encoder = None  # Load your label encoder if needed

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     images = np.array(data['images'])  # Expecting a list of images
#     images = images.astype('float32') / 255.0
#     images = images.reshape(images.shape[0], 64, 64, 1)  # Adjust shape if necessary

#     predictions = model.predict(images)
#     predicted_classes = np.argmax(predictions, axis=1)

#     # Decode labels if label_encoder is available
#     decoded_classes = label_encoder.inverse_transform(predicted_classes)

#     return jsonify({'predictions': decoded_classes.tolist()})

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# from tensorflow.keras.models import load_model
# import numpy as np
# import cv2
# import os

# app = Flask(__name__)
# model = load_model('trained_model.h5')  # Load the trained model

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             # Save the uploaded file temporarily
#             filepath = os.path.join('uploads', file.filename)
#             file.save(filepath)

#             # Preprocess the image
#             img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
#             img = cv2.resize(img, (64, 64))
#             img = img.astype('float32') / 255.0  # Normalize
#             img = img.reshape(1, 64, 64, 1)  # Reshape for model input

#             # Make prediction
#             prediction = model.predict(img)
#             predicted_class = np.argmax(prediction, axis=1)

#             # Map predicted class to label
#             class_label = 'Fake' if predicted_class[0] == 0 else 'Real'

#             return f'Predicted Class: {class_label}'

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from keras.models import load_model
# import numpy as np
# from PIL import Image

# app = Flask(__name__)
# model = load_model('trained_model.h5')  # Ensure this path is correct

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400

#     file = request.files['file']
    
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     try:
#         img = Image.open(file)
#         img = img.resize((150, 150))  # Adjust this size if needed
#         img_array = np.array(img) / 255.0  # Normalize the image
#         img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

#         prediction = model.predict(img_array)

#         # Assuming binary classification
#         result = 'Real' if prediction[0][0] > 0.5 else 'Fake'  # Modify threshold as needed
#         return jsonify({'prediction': result})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from keras.models import load_model
# import numpy as np
# from PIL import Image

# app = Flask(__name__)
# model = load_model('trained_model.h5')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400

#     file = request.files['file']
    
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     try:
#         img = Image.open(file)
#         img = img.resize((150, 150))
#         img_array = np.array(img) / 255.0
#         img_array = np.expand_dims(img_array, axis=0)

#         prediction = model.predict(img_array)
#         result = 'Real' if prediction[0][0] > 0.5 else 'Fake'
#         return jsonify({'prediction': result})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from keras.models import load_model
# import numpy as np
# from PIL import Image
# import os

# app = Flask(__name__)
# model = load_model(os.path.join(os.getcwd(), 'trained_model.h5'))  # Ensure the path is correct

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400

#     file = request.files['file']
    
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     try:
#         img = Image.open(file).convert('L')  # Ensure it's grayscale
#         img = img.resize((64, 64))  # Match the size used during training
#         img_array = np.array(img) / 255.0  # Normalize
#         img_array = np.expand_dims(img_array, axis=0)
#         img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension

#         prediction = model.predict(img_array)
#         result = 'Real' if prediction[0][0] > 0.5 else 'Fake'
#         return jsonify({'prediction': result})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify, render_template
from keras.models import load_model
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
model = load_model(os.path.join(os.getcwd(), 'trained_model.h5'))  # Ensure the path is correct

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(file).convert('L')  # Ensure it's grayscale
        img = img.resize((64, 64))  # Match the size used during training
        img_array = np.array(img) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)
        img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension

        prediction = model.predict(img_array)
        result = 'Real' if prediction[0][0] > 0.5 else 'Fake'
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
