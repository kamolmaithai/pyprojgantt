from flask import Flask, jsonify, render_template, request, send_from_directory
import json
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/',methods=[ "GET",'POST'])
def listproject():
    relevant_path = "web/static/data/"
    included_extensions = ['xml']
    file_names = [fn for fn in os.listdir(relevant_path)
                  if any(fn.endswith(ext) for ext in included_extensions)]
    return render_template('index.html', file_names=file_names)

@app.route('/upload',methods=[ "GET",'POST'])
def upload():
    isthisFile=request.files.get('file')
    #print(isthisFile)
    #print(isthisFile.filename)
    isthisFile.save("web/static/data/"+isthisFile.filename)
    resp = jsonify(success=True)
    return resp

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)