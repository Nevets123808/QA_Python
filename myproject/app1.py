from flask import Flask

app = Flask(__name__)

@app.route('/<int:number>')
def values(number):
    return f'{number**2}'

if __name__ == "__main__":
    app.run()