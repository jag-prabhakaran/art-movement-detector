from flask import Flask, render_template, request
from predict import query

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    output = query(image_path)
    #print(output)
    top_label = max(output, key=lambda x: x['score'])['label']
    #print(top_label)
    return render_template('index.html', prediction=top_label)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
