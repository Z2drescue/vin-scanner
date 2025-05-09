from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def extract_vin(text):
    vin_pattern = r'\b[A-HJ-NPR-Z0-9]{17}\b'
    matches = re.findall(vin_pattern, text.upper())
    return matches[0] if matches else None

@app.route('/extract-vin', methods=['POST'])
def extract_vin_api():
    data = request.get_json()
    ocr_text = data.get('text', '')
    vin = extract_vin(ocr_text)
    return jsonify({'vin': vin if vin else 'No VIN detected'})

if __name__ == '__main__':
    app.run(debug=True)
