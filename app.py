
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route("/mojastrona")
def mojastrona():
    return "To jest moja strona!"

@app.route('/hello', methods=['GET'])
def say_hello():
    name = request.args.get("name", "") 
    if name:
        resp = f"Hello {name}"
    else:
        resp = f"Hello"
    return resp

@app.route("/api/v1.0/predict", methods=["GET"])
def predict():
    num1 = request.args.get("num1", "") 
    num2 = request.args.get("num2", "")

    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if num1 + num2 > 5.8:
            output = 1
        else:
            output = 0
        
        return {"prediction": output, 
                "features": {
                    "num1": num1, 
                    "num2": num2
                    }
                }
            
    except ValueError:
        resp = {"error": "Invalid data"}
        return resp


if __name__ == "__main__":
    app.run()
