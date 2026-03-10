from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    selected_encoding = None
    input_text = ""

    # if request.method == "POST":
    #     selected_coding = request.form.get("operation")
    #     # input_text = request.form.get
    #     # type = request.form.get
    #
    #     if selected_coding == "encoding":
    #         print("")
    #
    #     print(selected_coding)

    return render_template(
            "index.html",
        encoding=selected_encoding,
        text=input_text
    )

if __name__ == "__main__":
    app.run(debug=True)



def encoding_seleted(method , msg):
   return


def encryption_selected(method,type,private_key,msg):
    return