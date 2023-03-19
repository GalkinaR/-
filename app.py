from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def zz():
    return render_template("zz.html")

@app.route('/aries')
def aries():
    return render_template("aries.html")

@app.route('/taurus')
def taurus ():
    return render_template("taurus.html")

@app.route('/gemini')
def gemini ():
    return render_template("gemini.html")

@app.route('/cancer')
def cancer():
    return render_template("cancer.html")

@app.route('/leo')
def leo():
    return render_template("leo.html")

@app.route('/virgo')
def virgo():
    return render_template("virgo.html")

@app.route('/libra')
def libra():
    return render_template("libra.html")

@app.route('/scorpio')
def scorpio():
    return render_template("scorpio.html")

@app.route('/sagittarius')
def sagittarius():
    return render_template("sagittarius.html")

@app.route('/capricorn')
def capricorn():
    return render_template("capricorn.html")

@app.route('/aquarius')
def aquarius():
    return render_template("aquarius.html")
    
@app.route('/pisces')
def pisces():
    return render_template("pisces.html")

@app.route("/authorization", methods=['GET', 'POST'])
def authorization():
    zz = ['Овен', 'Весы', 'Дева', 'Водолей', 'Стрелец', 'Скорпион', 'Козерог', 'Телец', 'Близнецы', 'Рак', 'Рыбы',
        'Лев']
    data = [item for item in reversed(list(open("info_users.txt", encoding='utf-8')))]
    if request.method == 'POST':
        Name = request.form.get("name")
        znak = request.form.get("znak")
        with open('info_users.txt', 'a', encoding='utf-8') as f:
            f.write(f'{Name} {znak}\n')
    return render_template('authorization.html', zz=zz, data=data)


if __name__=="__main__":
    app.run(debug=True)

