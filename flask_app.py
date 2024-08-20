from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/embeddio')
def embeddio():
    return render_template('embeddio.html')

@app.route('/preview')
def embeddio_preview():
    link = request.args.get("link")
    if link == None:
        return "Not enough args"
    link.replace('%2F', '/')
    link.replace('%3A', ':')
    return render_template('embeddio-preview.html', img=link)
