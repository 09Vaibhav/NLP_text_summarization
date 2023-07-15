from flask import Flask, render_template, request,  jsonify
import extractive_summarization as es
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/process', methods=['POST'])
def process():
    
    data = request.data # Access the input data from the form
    print(data)
    # Process the data or perform any backend operations
    # result = data.upper()  # Example: Convert the input to uppercase
    result = es.extractive_summarization(data)
    # print(data)
    # return jsonify({'result': result})
    return result


if __name__ == '__main__':
    app.run(debug=True)
