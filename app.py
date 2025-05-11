from flask import Flask, render_template
import os

app = Flask(__name__)

# Get config from environment variables
MESSAGE = "Hello from version: " + os.getenv("APP_VERSION")
BACKGROUND_COLOR = os.getenv("BACKGROUND_COLOR")

@app.route('/')
def index():
    return render_template("index.html", message=MESSAGE, bg_color=BACKGROUND_COLOR)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
