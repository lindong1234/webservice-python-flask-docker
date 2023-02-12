from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return str("Hello, World!")

#if __name__ == "__main__":
#    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the flask application on IP 0.0.0.0 and port 5000
