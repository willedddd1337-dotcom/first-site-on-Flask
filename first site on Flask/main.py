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


if __name__ == "__main__": 
    app.run(debug=True)