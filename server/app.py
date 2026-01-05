from flask import Flask

app = Flask(__name__)


# 1. Index View
# This is the only view that keeps the <h1> tags as per instructions
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# 2. String Parameter View
# The test expects raw text, not HTML tags
@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter


# 3. Count View
# The test expects newline characters (\n) rather than HTML line breaks (<br/>)
@app.route("/count/<int:parameter>")
def count(parameter):
    output = ""
    for i in range(parameter):
        output += f"{i}\n"
    return output


# 4. Math View
# The test expects a plain string representation of the number
@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    result = 0
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        # Result will be a float (e.g., 1.0)
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return str(result)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
