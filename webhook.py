from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return jsonify({"message": "OK"}), 200 
    else:
        return jsonify({"message": "Not OK"}), 405

if __name__ == '__main__':
    app.run(debug=True, port=5000)
