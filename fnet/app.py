from flask import Flask, jsonify
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
def create_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

if __name__ == "__main__": 
    app.run(host = '0.0.0.0', port = 5001, debug = True)  
