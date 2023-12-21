# main.py
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

@app.before_request
def initialize():
    create_directory(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploaded_images')
def show_uploaded_images():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('uploaded_images.html', images=images)

@app.route('/processed_images')
def show_processed_images():
    # 画像処理済み画像の一覧を取得するロジックをここに追加
    processed_images = os.listdir('static/processed')  # 画像処理済み画像のディレクトリを指定

    return render_template('processed_images.html', images=processed_images)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        print(f"Uploaded: {file.filename}")
        return render_template('index.html', filename=file.filename)

    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
