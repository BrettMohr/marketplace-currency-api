from flask import Flask
from resources.rate import get_rate
from resources.convert import get_conversion

app = Flask(__name__)

app.register_blueprint(get_rate)
app.register_blueprint(get_conversion)


