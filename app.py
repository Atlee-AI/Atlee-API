from flask import Flask, request
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

@app.route('/store-history', methods=['POST', 'OPTIONS'])
def store_history():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    else:
        data = request.json
        if data:
            with open('browsing_history.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                for page in data:
                    writer.writerow([page['title'], page['url']])
            response = 'Data stored successfully', 200
        else:
            response = 'No data received', 400

    return response

if __name__ == '__main__':
    app.run(debug=True, port=3000)