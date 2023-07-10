from flask import Flask, jsonify, request
from flask_pymysql import MySQL, cursors

app = Flask(__name__)

@app.route('/api/hello', methods = ['GET','POST'])
def welcome():
    return jsonify(response="Hello World")

@app.route('/api/calculate', methods = ['GET'])
def calculate():
    args = request.args

    try:
        operation = args.get("operation")
        num1 = args.get("num1")
        num2 = args.get("num2")

        data = {"operation": operation,
                "num1": num1,
                "num2": num2}

        if "addition" in operation:
            result = int(num1)+int(num2)

        elif "subtraction" in operation:
            result = int(num1)-int(num2)

        elif "multiplication" in operation:
            result = int(num1)*int(num2)

        elif "division" in operation:
            result = int(num1)/int(num2)

        data["result"] = result
        return jsonify(response=data)
        
    except Exception as e:
        return jsonify(response="Opps! There was some problem with the query! Please try again!"),400
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)