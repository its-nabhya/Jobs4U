from flask import Flask, render_template,jsonify

app = Flask(__name__)
Jobs =[ 
{
    'id': 'IB1',
    'title': 'Data Science Intern',
    'location': 'Bengaluru',
    # 'Salary' : 'Stipend of 10K/month '
},
{
    'id': 'JB1',
    'title': 'ML Engineer',
    'location': 'Bengaluru',
    'Salary' : 'Rs. 14LPA CTC '
}, 
{
    'id': 'JH2',
    'title': 'Software Developer 1',
    'location': 'Hyderabad',
    'Salary' : 'Rs. 16 LPA CTC '
},
{
    'id': 'JD3',
    'title': 'Backend Engineer',
    'location': 'Delhi',
    'Salary' : 'Rs. 23 LPA CTC '
},
{
    'id': 'JSF1',
    'title': 'SWE 1',
    'location': 'San Fransisco',
    'Salary' : '$ 300K LPA CTC'
}
]




# route basically provides the URL or path after the domain 
@app.route("/") # Empty route- basically home page 
# by doing this we ask flask to execute hello_world() when  url is domain/  i.e. our landing page
def home_Jobs4U():
    
    return render_template('home.html',Jobs=Jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)


print(__name__)
if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=True)