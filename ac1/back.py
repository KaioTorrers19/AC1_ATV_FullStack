from flask import Flask, request

app = Flask(_name_)


@app.route('/media', methods=['POST'])
def media():
    nota1 = request.form['nota1']
    nota2 = request.form['nota2']
    media = (float(nota1) + float(nota2)) / 2
    return str(media)


if _name_ == '_main_':
    app.run()
