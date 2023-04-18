from flask import Flask, render_template, request
from backgroundManager import BackgroundManager
from AI_ResponseManager import AI_Manager


app = Flask(__name__)

img = BackgroundManager()
gpt = AI_Manager()

@app.route("/", methods=["GET", "POST"])
def home_page():

    background = img.get_image()
    print(background)
    if request.method == "POST":

        query = request.form.get("query")
        reply = gpt.get_reply(query)
        return render_template("reply.html", reply=reply, back_image=background)

    return render_template("index.html",back_image=background)

if __name__ == "__main__":
    app.run(debug=True)