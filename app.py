from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    level = request.form.get('level')
    zone = request.form.get('zone')
    wallet = request.form.get('wallet')

    # Perform your calculation here based on the values

    result = f"Level: {level}, Zone: {zone}, Wallet: {wallet}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
