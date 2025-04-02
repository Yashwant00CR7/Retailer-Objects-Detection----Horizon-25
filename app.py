import os
import torch
import cv2
import numpy as np
from flask import Flask, request, jsonify
from io import BytesIO
from PIL import Image
import io
import requests
from collections import Counter
from ultralytics import YOLO

# Initialize Flask
app = Flask(__name__)

# Load your YOLO model
model = YOLO('best.pt')  # Load trained model

# POST request to send image and detect objects
@app.route('/detect', methods=['POST'])
def detect_objects():
    try:
        # Get the image from the request
        img_file = request.files['image']
        img_bytes = img_file.read()

        # Convert bytes to image
        image = Image.open(io.BytesIO(img_bytes))
        img_np = np.array(image)

        # Run inference using YOLO
        results = model(img_np)  # Returns a list of Results objects
        result = results[0]  # Extract the first Results object

        # Get class names
        class_names = model.names  # Class names are stored in the model

        # Extract detected class IDs and confidence scores
        detected_classes = result.boxes.cls.cpu().numpy()
        confidence_scores = result.boxes.conf.cpu().numpy()

        # Count occurrences of each class
        class_counts = Counter(detected_classes)

        # Select the class with the highest count or confidence
        best_class = None
        if class_counts:
            # Find the most frequently detected class
            most_common_class, count = class_counts.most_common(1)[0]

            # Filter instances of the most common class
            indices = np.where(detected_classes == most_common_class)
            best_confidence = max(confidence_scores[indices])  # Get max confidence

            # Assign the final best class
            best_class = class_names[int(most_common_class)]

        # Return the best detected class
        return jsonify({"best_detected_class": best_class})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app
if __name__ == "__main__":
    # app.run(debug=True)
    # if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=environ.get("PORT", 5000))