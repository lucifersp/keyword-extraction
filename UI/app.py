from flask import Flask, render_template
from werkzeug import secure_filename

import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')
ALLOWED_EXTENSIONS = set(['txt'])

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Register the controllers
app.register_blueprint(controllers.main)

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    # app.run(host='0.0.0.0', port=3000, debug=True)
    app.run(debug=True)
