from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from model import probe_model_5l_profit

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages

# Folder to store uploaded files
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def upload_file():
    return render_template("upload.html")


@app.route("/submit", methods=["POST"])
def submit_file():
    # Check if the file part is present in the request
    if "file" not in request.files:
        flash("No file part in the request.")
        return redirect(request.url)

    file = request.files["file"]

    # Check if the user has uploaded a file
    if file.filename == "":
        flash("No selected file.")
        return redirect(request.url)

    # Check if the file is a JSON file
    if not file.filename.endswith(".json"):
        flash("Invalid file type. Please upload a JSON file.")
        return redirect(request.url)

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, "data.json")
    file.save(file_path)

    try:
        # Process the file using model.py
        with open(file_path, "r") as f:
            data = json.load(f)

        # Check if 'data' key exists in the JSON
        if "data" not in data:
            flash("Invalid JSON structure: 'data' key is missing.")
            return redirect(request.url)

        results = probe_model_5l_profit(data["data"])

    except json.JSONDecodeError:
        flash("Error decoding JSON. Please ensure your file is valid.")
        return redirect(request.url)
    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return redirect(request.url)

    return render_template("results.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
