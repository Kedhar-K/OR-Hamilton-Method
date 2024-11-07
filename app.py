from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get matrix size from form
            size = int(request.form['size'])
            return render_template('index.html', size=size)
        except ValueError:
            return "Invalid matrix size. Please enter a valid integer."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


