from flask import Flask, render_template, request, redirect, url_for
from Functions import Hungarian

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = int(request.form['n'])
        return redirect(url_for('matrix', n=n))
    return render_template('index.html')

@app.route('/matrix/<int:n>', methods=['GET', 'POST'])
def matrix(n):
    if request.method == 'POST':
        matrix = []
        
        for i in range(n):
            row = [int(request.form[f'cell_{i}_{j}']) for j in range(n)]
            matrix.append(row)

        obj = Hungarian(matrix,n)
        di,t = obj.main()
        data_dict = di[t][-1]

        
        return render_template('table.html', data_dict=data_dict)
    
    return render_template('matrix.html', n=n)

if __name__ == '__main__':
    app.run(debug=True)
