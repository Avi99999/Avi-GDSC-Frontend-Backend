from flask import Flask, request, jsonify

app = Flask(__name__)

# GET endpoint
@app.route('/get-endpoint', methods=['GET'])
def get_endpoint():
    response_data = {
        "message": "Hello, this is a JSON response from the GET endpoint!"
    }
    return jsonify(response_data)

# POST endpoint
@app.route('/post-endpoint', methods=['POST'])
def post_endpoint():
    data = request.get_json()
    # Process the received data (if needed)
    confirmation_message = {
        "message": "Data received successfully!",
        "received_data": data
    }
    return jsonify(confirmation_message)

if __name__ == '__main__':
    app.run(debug=True)