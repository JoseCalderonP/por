from re import sub
import smtplib
import ssl
import os
from email.message import EmailMessage
from urllib import response
from flask import(
    Blueprint, render_template,request,redirect,url_for,current_app
)
import sendgrid
from sendgrid.helpers.mail import * 

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route('/mail', methods=['POST','GET'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if request.method == 'POST':
        send_email(name,email,message)
        return render_template('portfolio/sent_mail.html')
    
    return render_template('portfolio/sent_mail.html')

def send_email(name,email,message):
    mi_email  = 'joseegpecp@gmail.com'
    email_password = 'yzxtwhkhroderqfa'
    
    #asunto del correo
    subject = 'Mensaje enviado desde el Portafolio Mano!!'
    
    body = """
        Hola Jose Calderon P. Tiene un nuevo contacto desde la WEB:
        Nombre: %s
        Corre: %s
        Mensaje: %s
    """%(name,email,message)
    
    em = EmailMessage()
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(mi_email, email_password)
        smtp.sendmail(mi_email, mi_email, em.as_string())