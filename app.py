from flask import Flask, jsonify, render_template
from flask_cors import CORS
import math
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    """Serve the user-friendly web interface"""
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def api_info():
    """API information endpoint"""
    return jsonify({
        "message": "Welcome to the Simple Math API!",
        "version": "1.0.0",
        "description": "A simple API for basic geometric calculations",
        "endpoints": {
            "GET /": "User-friendly web interface",
            "GET /api": "This API information",
            "GET /circle/perimeter/<radius>": "Calculate circle perimeter",
            "GET /circle/area/<radius>": "Calculate circle area",
            "GET /rectangle/perimeter/<width>/<height>": "Calculate rectangle perimeter",
            "GET /rectangle/area/<width>/<height>": "Calculate rectangle area",
            "GET /triangle/area/<base>/<height>": "Calculate triangle area",
            "GET /health": "Health check"
        }
    })

@app.route('/circle/perimeter/<radius>', methods=['GET'])
def circle_perimeter(radius):
    try:
        radius_float = float(radius)
    except ValueError:
        return jsonify({"error": "Radius must be a valid number"}), 400
        
    if radius_float < 0:
        return jsonify({"error": "Radius must be positive"}), 400
    
    perimeter = 2 * math.pi * radius_float
    
    return jsonify({
        "shape": "circle",
        "calculation": "perimeter",
        "radius": radius_float,
        "formula": "2 × π × radius",
        "result": round(perimeter, 4),
        "unit": "same as radius unit"
    })

@app.route('/circle/area/<radius>', methods=['GET'])
def circle_area(radius):
    try:
        radius_float = float(radius)
    except ValueError:
        return jsonify({"error": "Radius must be a valid number"}), 400
        
    if radius_float < 0:
        return jsonify({"error": "Radius must be positive"}), 400
    
    area = math.pi * radius_float * radius_float
    
    return jsonify({
        "shape": "circle",
        "calculation": "area",
        "radius": radius_float,
        "formula": "π × radius²",
        "result": round(area, 4),
        "unit": "square units"
    })

@app.route('/rectangle/perimeter/<width>/<height>', methods=['GET'])
def rectangle_perimeter(width, height):
    try:
        width_float = float(width)
        height_float = float(height)
    except ValueError:
        return jsonify({"error": "Width and height must be valid numbers"}), 400
        
    if width_float < 0 or height_float < 0:
        return jsonify({"error": "Width and height must be positive"}), 400
    
    perimeter = 2 * (width_float + height_float)
    
    return jsonify({
        "shape": "rectangle",
        "calculation": "perimeter",
        "width": width_float,
        "height": height_float,
        "formula": "2 × (width + height)",
        "result": round(perimeter, 4),
        "unit": "same as input units"
    })

@app.route('/rectangle/area/<width>/<height>', methods=['GET'])
def rectangle_area(width, height):
    try:
        width_float = float(width)
        height_float = float(height)
    except ValueError:
        return jsonify({"error": "Width and height must be valid numbers"}), 400
        
    if width_float < 0 or height_float < 0:
        return jsonify({"error": "Width and height must be positive"}), 400
    
    area = width_float * height_float
    
    return jsonify({
        "shape": "rectangle",
        "calculation": "area",
        "width": width_float,
        "height": height_float,
        "formula": "width × height",
        "result": round(area, 4),
        "unit": "square units"
    })

@app.route('/triangle/area/<base>/<height>', methods=['GET'])
def triangle_area(base, height):
    try:
        base_float = float(base)
        height_float = float(height)
    except ValueError:
        return jsonify({"error": "Base and height must be valid numbers"}), 400
        
    if base_float < 0 or height_float < 0:
        return jsonify({"error": "Base and height must be positive"}), 400
    
    area = 0.5 * base_float * height_float
    
    return jsonify({
        "shape": "triangle",
        "calculation": "area",
        "base": base_float,
        "height": height_float,
        "formula": "0.5 × base × height",
        "result": round(area, 4),
        "unit": "square units"
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "OK",
        "timestamp": datetime.now().isoformat(),
        "message": "Math API is running perfectly!"
    })

if __name__ == '__main__':
    print("🚀 Starting User-Friendly Math API...")
    print("📱 Web Interface: http://127.0.0.1:5000")
    print("🔧 API Info: http://127.0.0.1:5000/api")
    app.run(debug=True, host='127.0.0.1', port=5000)