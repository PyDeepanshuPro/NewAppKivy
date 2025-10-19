from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'नमस्ते, यह मेरी पहली फ्लास्क वेबसाइट है!'

if __name__ == '__main__':
    app.run(debug=True)
    