import os
import json

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# Get the values of the environment variables
openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.api_key = os.getenv('OPENAI_API_KEY_LATEST')
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_version = os.getenv('OPENAI_API_VERSION')
# openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=generate_prompt(animal),
        #     temperature=0.6,
        # )
        response = openai.ChatCompletion.create(
                        engine="chat",
                        messages = generate_prompt(animal),
                        temperature=0.7,
                        max_tokens=800,
                        top_p=0.95,
                        frequency_penalty=0,
                        presence_penalty=0,
                        stop=None)

        reply = response['choices'][0]['message']['content']
        # return redirect(url_for("index", result=response.choices[0].text))
        return redirect(url_for("index", result=reply))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    json_file = "prompt.json"
    with open(json_file,"r") as file:
        msg_arr = json.load(file)

    msg_arr.append({"role":"user","content":animal})
    return msg_arr
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )
