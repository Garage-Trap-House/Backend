from flask import Flask 

app = Flask(__name__)

@app.route("/testing")
def hello_world():
    return "The Garage Trap House says hi! :)"

# the host value allows traffic from anywhere to run this 
app.run(host = "0.0.0.0")