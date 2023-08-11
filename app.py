# app.py
from flask import Flask, render_template

app = Flask(__name__)

def print_ascii_cake():
    cake = r"""
        🎂🍰🎂🍰🎂
      🍰           🍰
    🎂  H A P P Y  🎂
      🍰     B I R T H D A Y   🍰
        🎂         🎂
    """
    return cake

@app.route('/')
def wish_birthday():
    cake = print_ascii_cake()
    message = f"Happy Birthday, {person_name}! 🎉🎈"
    return render_template('index.html', cake=cake, message=message)

if __name__ == '__main__':
    person_name = "Emily"
    app.run(host='0.0.0.0', port=80)
