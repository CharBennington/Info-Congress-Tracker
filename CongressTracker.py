# SETUP: This section includes imports and other configuration needed for flask to operate
from flask import Flask

app = Flask(__name__)





#Routes: Flask routes; nothing too fancy


@app.route("/", methods=["GET"])
def main():
    return "Hey, hello, hola world"






# Functions: Where most of the magic happens











if __name__ == "__main__":
    app.run()
