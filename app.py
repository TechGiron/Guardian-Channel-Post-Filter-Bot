from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bharat'

def run_bot():
    print("Bot Started 👍 Powered By @unicornguardian")
    Bot().run()

if __name__ == "__main__":
    app.run
