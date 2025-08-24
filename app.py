from flask import Flask, render_template

app = Flask(__name__)

# route basically provides the URL or path after the domain 
@app.route("/") # Empty route- basically home page 
# by doing this we ask flask to execute hello_world() when  url is domain/  i.e. our landing page
def hello_world():
    
    return render_template('home.html')


print(__name__)
if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=True)