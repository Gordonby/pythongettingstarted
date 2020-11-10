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

@app.route('/', methods=['PUT'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
        file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed')
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/testimagedl', methods=['GET'])
def create_record():
    sampleimageurl='https://gordon.byers.me/assets/img/die-bart-die.png'
    imagefile = requests.get(sampleimageurl)
    open('/tmp/localimage.png', 'wb').write(imagefile.content)

    return send_file('/tmp/localimage.png', mimetype='image/png')


if __name__ == "__main__": 
    app.run(host = '0.0.0.0', port = 5001, debug = True)  
