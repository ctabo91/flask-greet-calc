# Put your app in here.

from flask import *
from operations import *

app = Flask(__name__)


@app.route('/add')
def addition():
    """adds a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = add(a, b)

    return str(result)



@app.route('/sub')
def subtraction():
    """subtracts a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = sub(a, b)

    return str(result)


@app.route('/mult')
def multiplication():
    """multiplies a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = mult(a, b)

    return str(result)


@app.route('/div')
def division():
    """divides a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = div(a, b)

    return str(result)


# Further Study

math_ops = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route('/math/<operation>')
def do_math(operation):
    """does specified math operation on a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = math_ops[operation](a, b)

    return str(result)
