from flask import Flask, render_template 


app = Flask(__name__)

list_characters = """Станом на червень 2026 (патч 7.41), найсильніші герої мети в пабах виглядають приблизно так:

Juggernaut
Luna
Phantom Lancer
Spectre

Особливо сильні зараз Spectre та Wraith King за загальним вінрейтом у більшості рангів.

Sniper
Arc Warden
Tinker
Puck
🛡️ Офлейн (Pos 3)
Legion Commander
Axe
Dawnbreaker
Night Stalker
Mars

Legion Commander та Axe зараз входять до найстабільніших героїв для підняття MMR.

Rubick
Snapfire
Ogre Magi
🧙 Саппорт 5
Shadow Shaman
Witch Doctor
Lion
Bounty Hunter""" 

@app.route('/')
def home(): 
    return render_template("index.html")


@app.route('/characters') 
def meta_characters(): 
    return render_template("meta.html", text=list_characters)


@app.route("/patch741d")
def new_patch():
    return render_template("patch741d.html")

@app.route("/heroes")
def heroes():
    return render_template("heroes.html")


@app.route("/heroes_pos1")
def pos1():
    return render_template("heroes_pos1.html")


@app.route("/heroes_pos2")
def pos2():
    return render_template("heroes_pos2.html")


@app.route("/heroes_pos3")
def pos3():
    return render_template("heroes_pos3.html")


@app.route("/heroes_pos4")
def pos4():
    return render_template("heroes_pos4.html")


@app.route("/heroes_pos5")
def pos5():
    return render_template("heroes_pos5.html")


@app.route("/hero/<name>")
def hero_page(name):
    return render_template(f"hero_{name}.html")

if __name__ == "__main__": 
    app.run(debug=True)