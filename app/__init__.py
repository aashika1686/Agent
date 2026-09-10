import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from app.gmail import(
    is_email_command,
    extract_email,
    create_gmail_url,
    generate_email_with_gemini
)

from app.youtube import youtube_bp

def create_app():

    app = Flask(__name__)
    CORS(app)

#youtube
    app.register_blueprint(youtube_bp, url_prefix="/youtube")

#home
    @app.route("/")
    def home():
        return render_template("index.html")

#HTML
    @app.route("/html")
    def html():
        return render_template("index.html")

#health
    @app.route("/health")
    def health():
        return jsonify({"status":"ok",
