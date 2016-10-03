from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def mystery():
    response = app.make_response(render_template('mystery.html'))
    response.set_cookie('test1', value='best test')
    return response

@app.route('/puzzle2')
def puz():
    img_names = ["Avocado.jpg",
                 "Lighthouse.jpg",
                 "Iridescent.jpg",
                 "Night.jpg",
                 "Kiwi.jpg",
                 "Iphone.jpg",
                 "Strawberry.jpg",
                 "Navy.jpg",
                 "Oak.jpg",
                 "Truth.jpg",
                 "Earth.jpg",
                 "Night.jpg",
                 "Atom.jpg",
                 "Book.jpg",
                 "Laser.jpg",
                 "Emoji.jpg",
                 "Dna.jpg"]
    return render_template('puz2.html', entries=img_names)

@app.route('/robots.txt')
def serve_static():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/spacer.gif')
def secret():
    response = app.make_response(send_from_directory(app.static_folder, 'spacer.gif'))
    response.set_cookie('test3', value='banana test')
    return response
