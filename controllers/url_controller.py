from flask import Flask, render_template
import controllers.login_controller

def url_label(label_name):
	if "login" in label_name:
		return  getattr(controllers.login_controller, label_name)()
	
def url_post(label_name):
	if "login" in label_name:
		return getattr(controllers.login_controller, label_name)()

