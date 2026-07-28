from flask import Flask, jsonify, render_template

import time

# Initialize the Flask application
app = Flask(__name__)

# Define the root route (Home page)
@app.route('/')
def home():
    return "Hello, World! Welcome to your Flask Application."

# Define an API route that returns JSON data
@app.route('/api/data')
def get_data():
    return jsonify({"status": "success", "message": "Data retrieved successfully"})

@app.route('/delayed-api', methods=['GET'])
def delayed_api():
    # Blocks the current thread for 10 seconds
    time.sleep(15) 
    return jsonify(message="Responded after 10 seconds")

# Run the app locally (Only for development)
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=8000, debug=True)
