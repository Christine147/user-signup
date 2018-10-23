from flask import Flask, request, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def display_form():
    return render_template('Index.html')

@app.route('/verify', methods=['POST'])
def verify():

    username = request.form['username'] 
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = " "
    password_error = " "
    verify_error = " "
    email_error = " "

    if len(username) < 3 and len(username) >20 or username == " ":
        username_error = "Username must be 3 - 20 characters and No spaces allowed please"


    if len(password)  < 3 and len(password) >20 or password == " ":
        password_error = "Password must be 3 - 20 characters and No spaces allowed please"
        password = ''

  
    if verify == " ":
        verify_error = "Password is required." 
        verify = '' 

    elif verify != password:
        verify_error = "Password and verify must match."
        verify = ''

    if email != " " and len(email) < 3 and len(email) > 20:
        email_error = "Email must be 3 - 20 characters"          
    elif email != " " and ("@" not in email or "." not in email):
            email_error = "Email must contain an @ sign and Email must contain a ."

      
    if not username_error and not password_error and not verify_error and not email_error: 
        return render_template('Welcome.html', username = username)
    else:
        return render_template('Index.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, email=email)
    #hello  #goodbye

    @app.route('/Welcome')
    def Welcome():
        username = request.args.get('username')
        return render_template('Welcome.html', username=username)

if __name__ == "__main__":
    app.run()