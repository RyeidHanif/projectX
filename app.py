from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Mapping dictionary
session_map = {
    "mj": "s",
    "on": "w",
    "fm": "m"
}

# Subject to code mapping
subject_codes = {
    "math": "9709",
    "cs": "9618",
    "chem": "9701",
    "chemistry": "9701",
    "phy": "9702",
    "physics": "9702"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form['subject'].lower()
        ans = request.form['ans'].lower()
        session = request.form['session'].lower()
        year = request.form['year']
        paper = request.form['paper']

        code = subject_codes.get(subject)

        if not code or session not in session_map:
            return render_template('error.html')

        refined_session = session_map[session] + year
        url = f"https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/{code}_{refined_session}_{ans}_{paper}.pdf"
        
        return render_template('redirecting.html', url=url)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
