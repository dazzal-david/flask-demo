from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test():
    value = ""
    if request.method == 'POST':
        value = request.form.get('name')
    return render_template('index.html', name=value)



if __name__ == '__main__':
   app.run()
