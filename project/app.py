from flask import Flask,render_template
app=Flask('__main__',template_folder='templates')
@app.route('/index')
def index():
    return render_template('color.html')

@app.route('/')
def submit():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)