from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/inference/<token>', methods=['GET'])
def get_inference(token):
    file_path = f'data/{token}.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        return jsonify({"price": data})
    else:
        return jsonify({"error": "Token data not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
