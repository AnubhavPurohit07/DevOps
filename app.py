from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return f"""
    <html>
    <head><title>DevOps Task 1 - Dockerized App</title></head>
    <body style="font-family: sans-serif; text-align:center; margin-top: 60px;">
        <h1>Welcome to my container!!!</h1>
        <p>Container hostname: <b>{hostname}</b></p>
        <p>This confirms the app is running in an isolated container environment.</p>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
