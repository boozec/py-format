from flask import make_response, jsonify, abort, request, render_template
from flask_mail import Message

from functools import wraps
from datetime import datetime


def send_email(sender, 
               
               email, 
               activation_code, title,
               template):
    msg = Message(title, sender=sender, recipients=[email])

    rest_link = 'http://localhost:8080/app'
    msg.html = render_template(template, link=rest_link, code=activation_code)
    mail.send(msg)


def http_call(data, status):
    return make_response(jsonify({"status": status, "result": data}), status)
