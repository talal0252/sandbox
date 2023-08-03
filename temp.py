from flask import Flask, request, jsonify
from sandbox import Sandbox

app = Flask(__name__)

@app.route('/execute_python', methods=['POST'])
def execute_python():
    try:
        python_code = request.json.get('python_code')
        sandbox = Sandbox()
        result = sandbox.execute(python_code)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)