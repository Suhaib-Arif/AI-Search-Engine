from flask import Flask, render_template, request, flash, redirect, url_for
from backgroundManager import BackgroundManager
from AI_ResponseManager import AI_Manager
from openai.error import InvalidRequestError


app = Flask(__name__)

app.secret_key ='hjgfjgfjgfjgf'


img = BackgroundManager()
gpt = AI_Manager()


@app.route("/", methods=["GET", "POST"])
def home_page():
    background = img.get_image()
    if request.method == "POST":
        query = request.form.get("query")

        reply = gpt.get_reply(query)
        return render_template("reply.html", reply=reply, back_image=background)

    return render_template("index.html", back_image=background)


@app.route("/image", methods=["GET", "POST"])
def image_generation():
    description = ""
    if request.method == "POST":
        description = request.form.get("description")
        try:
            url=gpt.generate_image(description)
        except InvalidRequestError:
            flash(
                    message="The request has violated openai terms of service.We cannot show the requested image",
                    category="error"
                  )
            url = None
            description = "Cannot show image"

        return render_template("images1.html",url=url, description=description)

    return render_template("images1.html",description=description)


if __name__ == "__main__":
    app.run(debug=True)
