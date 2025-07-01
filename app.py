from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
import dotenv


app = Flask(__name__)
app.secret_key = dotenv.get_key('.env', 'APP_KEY')

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = dotenv.get_key('.env', 'EMAIL')
app.config['MAIL_PASSWORD'] = dotenv.get_key('.env', 'PASSWORD')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        try:
            msg = Message('New Contact Form Submission',
                        sender=email,
                        recipients=[dotenv.get_key('.env', 'EMAIL')])
            msg.body = f"""
            From: {name}
            Email: {email}
            Message: {message}
            """
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('An error occurred while sending your message.', 'error')
        
        return redirect('/contact')
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
