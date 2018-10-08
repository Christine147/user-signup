from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def display_form():
    return render_template('Index.html')

def blank(x):
    if len(x) > 0:
        return True
    else:
        return False

def correct_length(x):
    if len(x) >= 3 and len(x) <21:
        return True
    else:
        return False

def space_x(x):
    if " " in x:
        return True
    else:
        return False

def at_sign_email(x):
    if x.count('@') == 1:
        return True
    else:
        return False

def dot_in_email(x):
    if x.count('.') == 1:
        return True
    else:
        return False

@app.route("/", methods=['GET', 'POST'])
def verify_signup():

    username = request.form["username"] 
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if blank(username):
      username_error = "Username required" 
    elif not correct_length(username):
        username_error = "Username must be 3 - 20 characters"
    elif space_x(username):
        username_error = "No spaces allowed please"
    else:
        username = username

    if not blank(password):
        password_error = "Password is required."
        password = ''
        verify = verify
    elif not correct_length(password):
        password_error = "Password must be between 3-20 characters."
        password = ''
       
    elif space_x(password):
        password_error = "Password must not contain spaces."
        password = ''

    if not blank(verify):
        verify_error = "Password is required."
        verify = ''     

    elif not correct_length(verify):
        verify_error = "Password must be between 3-20 characters."
        verify = ''
       
    elif space_x(verify):
        verify_error = "Password must not contain spaces."
        verify = ''

    if not password_error and not verify_error:
        if password != verify
          password_error = "Passwords must match."
          verify_error = "Passwords must match."
          passwprd = ''
          verify = ''

    if blank(email):
        if space_x(email):
            email_error = "No spaces in email please"
            if not correct_length(email):
                email_error = "Email must be between 3 - 20 characters."
            
            if not at_sign_email(email):
                email_error = "Email must contain an @ sign"
            
            if not dot_in_email(email):
                email_error = "Email musst contain a ."

        else:
            email_error = ''
            email = email

        if not username_error and not password_error and not verify_error and not email_error: 
            username = username
            return redirect('/welcome?username={0}'.format(username))
        else:
            return render_template('Index.html', username_error=username_error, username=username, password_error=password_error, verify_error=verify_error, email_error=email_error, email=email)
      

    @app.route('/welcome')
    def welcome():
        username = request.args.get('username')
        return render_template('welcome.html', username=username)

    if __name__ == "__main__":
    app.run()