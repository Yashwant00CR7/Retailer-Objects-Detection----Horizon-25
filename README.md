


# 🛒 Object Detection Model – Shopping App

This repository contains the Machine Learning model developed for our smart shopping app. The model identifies objects/products in real-time using images from a camera or image input. This model is a core component of our app's intelligent features like dynamic pricing, AR navigation, and voice assistance.

<img width="434" height="246" alt="image" src="https://github.com/user-attachments/assets/46d169f5-30c9-49e5-a8b2-f247f3145962" />


## 🚀 Features

- Detects multiple product categories using YOLOv5
- Supports image and live camera input
- Fast and lightweight – suitable for mobile deployment
- REST API support for easy integration with apps
- Used in conjunction with AR-based indoor navigation and voice support

## Test the Model here
👉 Try the model here:  
**[🔗 Hugging Face Space](https://huggingface.co/spaces/Yash030/my-yolo-app)**

<img width="1600" height="765" alt="image" src="https://github.com/user-attachments/assets/0009232c-4bda-41ba-b705-7ff14cdce25b" />


## 🧠 Model Details

- **Architecture**: YOLOv5 (You Only Look Once)
- **Framework**: PyTorch
- **Training Dataset**: Custom-labeled product dataset (e.g., sarees, kurtis, watches, electronics)
- **Classes**: `["Saree", "Kurti", "Watch", "Sneakers", "Headphones", ...]`
- **Performance**: mAP@0.5 ≈ 90% on test set

## 📦 Project Structure



object-detection-model/
```
├── models/                  # Trained YOLO model weights (.pt)
├── dataset/                 # Sample training images (optional)
├── api/                     # Flask API to serve model
│   ├── app.py               # Main API endpoint (/predict)
│   └── utils.py             # Preprocessing & prediction functions
├── detect.py                # Script for testing detection on local images
├── requirements.txt         # Required Python packages
└── README.md                # Project documentation

```

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Yashwant00CR7/Retailer-Objects-Detection----Horizon-25.git
cd Retailer-Objects-Detection----Horizon-25
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run Inference on Sample Image

```bash
python detect.py --source path/to/image.jpg --weights models/best.pt
```

### 4. Run Flask API

```bash
cd api
python app.py
```

* Send a POST request to `/predict` with an image.
* Response: JSON with object names and bounding box coordinates.

## 🧪 Sample API Request (using Python)

```python
import requests

image_path = 'test.jpg'
files = {'file': open(image_path, 'rb')}
response = requests.post('http://localhost:5000/predict', files=files)
print(response.json())
```

## 📊 Model Output

The model returns:

```json
[
  {
    "class": "Watch",
    "confidence": 0.93,
    "box": [x1, y1, x2, y2]
  },
  {
    "class": "Sneakers",
    "confidence": 0.89,
    "box": [x1, y1, x2, y2]
  }
]
```

## 📱 Integration

* **Frontend**: Flutter app with camera access
* **Backend**: Flask API (can be deployed via Render, Railway, or Hugging Face Spaces)
* **Text-to-Speech**: Converts detected object names into speech
* **AR Navigation**: Detected product passed to Unity to trigger pathfinding

## 📌 Future Enhancements

* Improve detection on occluded/low-light images
* Add multi-language voice support
* Lightweight on-device inference with YOLOv8 Nano

## 🧑‍💻 Authors

* \[Your Name] – ML Model Development
* \[Teammates] – API, UI/UX, Navigation

## 📜 License

MIT License – free to use, modify, and distribute.

---

