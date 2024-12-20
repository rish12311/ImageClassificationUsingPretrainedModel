from flask import Flask, request, jsonify
from PIL import Image
import tensorflow as tf
import numpy as np
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Load a pre-trained model
model = tf.keras.applications.vgg16.VGG16(weights='imagenet')


def preprocess_image(image):
    # Convert the image to RGB (removes the alpha channel if present)
    image = image.convert('RGB')

    # Resize the image to 224x224 as expected by VGG16
    image = image.resize((224, 224))

    # Convert the image to a numpy array
    image = np.array(image)

    # Preprocess the image for VGG16
    image = tf.keras.applications.vgg16.preprocess_input(image)

    # Add batch dimension (VGG16 expects input in the form of (batch_size, height, width, channels))
    return np.expand_dims(image, axis=0)


@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    try:
        image = Image.open(file.stream)
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        decoded_predictions = tf.keras.applications.vgg16.decode_predictions(predictions, top=3)
        response = [{'label': pred[1], 'probability': float(pred[2])} for pred in decoded_predictions[0]]
        return jsonify({'description': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
