from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def display_form():
    return render_template('Index.html')

@app.route('/', methods=['POST'])
def verify():

    username = request.form['username'] 
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if len(username) < 3 or len(username) >20 or " " in username:
        username_error = "Username must be 3 - 20 characters and No spaces allowed please"


    if len(password)  < 3 or len(password) >20 or " " in password:
        password_error = "Password must be 3 - 20 characters and No spaces allowed please"
        password = ''

    if len(verify)  < 3 or len(verify) >20 or " " in verify:
        verify_error = "Password must be 3 - 20 characters and No spaces allowed please"
        verify = ''    
          
    if verify == " ":
        verify_error = "Password is required." 
        verify = '' 

    elif verify != password:
        verify_error = "Password and verify must match."
        verify = ''

    if email != "" and len(email) < 3 or len(email) > 20 or " " in email:
        email_error = "Email must be 3 - 20 characters"          
    elif email != "" and ("@" not in email or "." not in email):
        email_error = "Email must contain an @ sign and Email must contain a ."

      
    if not username_error and not password_error and not verify_error and not email_error: 
        username=username
        return redirect('/Welcome?username={0}'.format(username))
    else:
        return render_template('Index.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, email=email)
    #hello  #goodbye

@app.route('/Welcome')
def Welcome():
    username = request.args.get('username')
    return render_template('Welcome.html', username=username)

if __name__ == "__main__":
    app.run()