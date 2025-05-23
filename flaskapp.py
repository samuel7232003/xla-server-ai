import traceback

from flask import Flask, request, jsonify
from flask_cors import CORS
from requests import get
import os
import uuid

from EfficientNetB3.predict import preprocess_image, predict_image

app = Flask(__name__)
CORS(app)

@app.route('/img', methods=['POST'])
def post_data():
    payload = request.get_json()
    if not payload or 'img' not in payload:
        return jsonify({'error': 'Invalid or missing JSON payload'}), 400

    input_img = payload['img']

    try:
        # Tải ảnh từ URL
        response = get(input_img)
        response.raise_for_status()  # kiểm tra lỗi HTTP

        # Tạo thư mục nếu chưa tồn tại
        os.makedirs('./data', exist_ok=True)

        # Tạo tên file duy nhất và lưu ảnh
        img_filename = f"{uuid.uuid4().hex}.jpg"
        img_save_path = os.path.join('data', img_filename)

        with open(img_save_path, "wb") as file:
            file.write(response.content)

        # Tiền xử lý ảnh và dự đoán
        processed_image = preprocess_image(img_save_path)
        result = predict_image(processed_image)
        print(result)
        output_img = "REAL" if result == 0 else "FAKE"
        return jsonify({'text': output_img}), 200

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
