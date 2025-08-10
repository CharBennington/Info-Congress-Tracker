# SETUP: This section includes imports and other configuration needed for flask to operate
from flask import Flask, render_template, request

app = Flask(__name__)





#Routes: Flask routes; nothing too fancy


@app.route("/", methods=["GET"])
def main():
    if request.method == "GET":
    	return render_template("home.html")






# Functions: Where most of the magic happens











if __name__ == "__main__":
    app.run()
