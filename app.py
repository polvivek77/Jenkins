from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "My name is Vivek Pol. Please do like share and subscribe to my YouTube Channel - BetterCallPol"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)