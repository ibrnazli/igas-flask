from flask import Flask, request, jsonify
from waitress import serve
import cv2
import numpy as np
import tensorflow as tf
import os  # os modülünü ekle

app = Flask(__name__)

def analyze_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return {"error": "Görsel okunamadı"}

    risks = []
    suggestions = []

    risks.extend([
        "Sprinkler sistemi eksik",
        "Duman algılama cihazı eksik",
        "Yakıt tankı güvenlik eksikliği",
        "Depolama alanında düzensizlik",
    ])
    suggestions.extend([
        "Sprinkler sistemi kurun ve düzenli bakım yapın.",
        "Duman algılama cihazı yerleştirin.",
        "Yakıt tankı için güvenlik önlemleri alın.",
        "Depolama alanını düzenli tutun ve erişim yollarını açık bırakın.",
    ])

    return {"risks": risks, "suggestions": suggestions}

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "Lütfen bir fotoğraf yükleyin"}), 400

    image_file = request.files['image']
    image_path = f"temp_{image_file.filename}"
    image_file.save(image_path)

    try:
        result = analyze_image(image_path)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.remove(image_path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render'ın $PORT değişkenini kullan, yoksa 5000
    serve(app, host='0.0.0.0', port=port)