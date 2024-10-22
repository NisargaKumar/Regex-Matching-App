from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']

    # Find all matches
    matches = re.findall(regex_pattern, test_string)

    return render_template('results.html', matches=matches, test_string=test_string, regex=regex_pattern)

@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        # Regex pattern for validating an Email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid = re.match(email_pattern, email) is not None
        return render_template('validate_email.html', email=email, is_valid=is_valid)

    return render_template('validate_email.html', email='', is_valid=None)

if __name__ == '__main__':
    app.run(debug=True)
