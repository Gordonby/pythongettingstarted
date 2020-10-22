from flask import Flask, send_file, jsonify
import requests
app = Flask(__name__) 
  
@app.route('/', methods=['GET']) 
def index():
    return jsonify({'success': 'false',
                    'message': 'please PUT the image binary or uri'})

@app.route('/canary')
def canary():
    return jsonify({'success': 'true',
                    'message': 'HTTP 200. All ok.'})

@app.route('/imagedl', methods=['GET','PUT'])
def create_record():
    
    sampleimageurl='https://gordon.byers.me/assets/img/die-bart-die.png'
    imagefile = requests.get(sampleimageurl)
    open('/tmp/localimage.png', 'wb').write(imagefile.content)

    return send_file('/tmp/localimage.png', mimetype='image/png')

if __name__ == "__main__": 
    app.run(host = '0.0.0.0', port = 5001, debug = True)  
