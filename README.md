# crossxxclashautorefresh
this is just a simple flask script you can run locally so that you dont have to update
[crossxx-labs](https://github.com/crossxx-labs/free-proxy)'s free clash proxy subscription url so often. lwk they making things harder for me maybe theres other people doin ts too which is why 😭

i currently run this via render with uptimerobot using gunicorn

# setup
its recommended to install the required libraries under a virtual environment to prevent clutter
`pip install -r requirements.txt`

# running
for personal use you can run via flask
`flask run` or `python -m flask run`

if you wish to run on a server, a better alternative is [gunicorn](https://flask.palletsprojects.com/en/stable/deploying/gunicorn/)