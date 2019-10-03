from flask import Flask, redirect
from pylti.flask import lti


app = Flask(__name__)

app.config['SECRET_KEY'] = 'app_secretkey'  # Nothing to do with Moodle
app.config['PYLTI_CONFIG'] = {
    'consumers': {
        'lticonsumerkey': {  # Set this key in Moodle
            'secret': 'ltisecretkey',  # Set this key in Moodle
        },
    },
}


@app.route('/lti', methods=['POST'])
@lti(request='initial', app=app)
def lti_initial(lti):
    return redirect(".", code=302)


@app.route('/', methods=['GET'])
@lti(request='session', app=app)
def index(lti):
    return f'''This is a protected contents.<br>
<ul>
    <li>lti.name={lti.name}</li>
    <li>lti.user_id={lti.user_id}</li>
    <li>lti.key={lti.key}</li>
    <li>lti.role={lti.role}</li>
</ul>
'''
