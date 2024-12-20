# Image Description Web Application

This repository contains a simple web application that allows users to upload an image and receive a text description of its content. The project includes both a backend API powered by a pre-trained image classification model and a frontend interface for user interaction.

---

## Features
- **Backend**: Built using Flask and TensorFlow, leveraging the VGG16 pre-trained model for image classification.
- **Frontend**: User-friendly interface using HTML, CSS, and JavaScript for image upload and displaying results.
- **Deployment**: Can be deployed locally or on cloud platforms like Heroku, AWS, or Render.

---

## Requirements

### Backend
- Python 3.8+
- Flask
- TensorFlow
- Pillow

### Frontend
- A modern web browser

---

## Installation and Setup

### Backend Setup
1. Clone the repository:
   ```bash
   git clone <https://github.com/rishabhgoyal-123/ImageClasificationUsingPretrainedModel.git>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```bash
   python app.py
   ```
   By default, the API will be accessible at `http://localhost:5000`.

### Frontend Setup
1. Open `frontend.html` in a web browser.
2. Ensure the backend server is running.
3. Upload an image and click the "Submit" button to get a description.

---

## API Endpoints

### POST `/upload`
- **Description**: Accepts an image file and returns the top 3 predicted descriptions with their probabilities.
- **Request**: `multipart/form-data`
  - `image`: Image file (PNG/JPEG).
- **Response**:
  ```json
  {
      "description": [
          {"label": "label_name", "probability": 0.95},
          {"label": "label_name", "probability": 0.85},
          {"label": "label_name", "probability": 0.75}
      ]
  }
  ```
- **Error Response**:
  ```json
  {
      "error": "Error message"
  }
  ```

---

## Deployment

### Local Deployment
1. Follow the backend and frontend setup instructions.
2. Use `ngrok` or similar tools to expose the backend API for external access if needed.


## Future Improvements
- Add multilingual support for descriptions.
- Enhance frontend design using a modern framework (e.g., React, Vue).
- Optimize backend with more advanced pre-trained models (e.g., CLIP by OpenAI).

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.
