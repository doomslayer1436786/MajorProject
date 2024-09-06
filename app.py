from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from PIL import Image, ImageOps
import justimagedetection

app = Flask(__name__)

# Folder to store uploaded images
UPLOAD_FOLDER = 'static/uploads/'
# Folder to store processed images
DETECTION_FOLDER = 'detections/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DETECTION_FOLDER'] = DETECTION_FOLDER

# Allowed extensions for file upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        # If no file is selected
        if file.filename == '':
            return "No selected file"
        # Check if the file is allowed
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Process the image and save it in the detections folder
            processed_image_path = process_image(file_path, filename)

            return redirect(url_for('display_image', filename=filename))

    return render_template('index.html')

def process_image(image_path, filename):
    processed_image_path = justimagedetection.processImage(image_path)
    return processed_image_path


@app.route('/display/<filename>')
def display_image(filename):
    # Display the processed image
    filename = filename.split('/')[-1] 
    return render_template('display.html', filename=filename)

@app.route('/detections/<filename>')
def send_detection_image(filename):
    # Serve the processed image from the detections folder
    return send_from_directory(app.config['DETECTION_FOLDER'], filename)

if __name__ == '__main__':
    # Create the folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['DETECTION_FOLDER'], exist_ok=True)
    app.run(debug=True)
