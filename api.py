from flask import Flask

app = Flask(__name__)

@app.route('/')
def ab():
    return 'hey! akshay is a good Data Scientist.'



