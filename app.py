from flask import Flask, render_template

app = Flask(__name__)
JOBS =[
    {
        'id' : 1,
        'title' : 'Software Engineer',
        'location' : 'San Francisco, CA',
        'salary' : '$100,000'
    },
    {
        'id' : 2,
        'title' : 'Data Scientist',
        'location' : 'Seattle, WA',
        'salary' : '$90,000'
    },
    {
        'id' : 3,
        'title' : 'Front End Developer',
        'location' : 'Remote',
        'salary' : '$95,000'
    },
    {
        'id' : 4,
        'title' : 'Back End Developer',
        'location' : 'Dallas, TX',
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs = JOBS,
                           person_name = "Karim's")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)
