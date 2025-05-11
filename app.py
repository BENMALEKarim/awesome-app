from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Get config from environment variables
MESSAGE = "Hello from version: " + os.getenv("APP_VERSION")
BACKGROUND_COLOR = os.getenv("BACKGROUND_COLOR")

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <title>Flask App</title>
  <style>
    body {
      background-color: {{ bg_color }};
      color: #333;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      font-size: 2rem;
    }
  </style>
</head>
<body>
  {{ message }}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(
        TEMPLATE,
        message=MESSAGE,
        bg_color=BACKGROUND_COLOR
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
