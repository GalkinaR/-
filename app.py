from flask import Flask, render_template

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

if __name__=="__main__":
    app.run()
