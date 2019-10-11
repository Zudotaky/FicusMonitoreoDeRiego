
from flask import Flask
from backend.Phyton.Api.Api import api

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app = Flask(__name__)  # , template_folder="templates"
    api.init_app(app)
    app.run(debug=True)
    # app.  run(host='0.0.0.0',port=5000)