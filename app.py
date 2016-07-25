from flask import Flask, render_template, request, session
import controllers.controller1
import controllers.url_controller

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def main():
	return controllers.url_controller.root_url()    

@app.route("/<label_name>")
def label_redirect(label_name):
	response = controllers.url_controller.url_label(label_name)
	return response

@app.route('/<label_name>', methods=['POST'])
def input_redirect(label_name):
	response = controllers.url_controller.url_label(label_name)
	return response

if __name__ == "__main__":
    app.run()
