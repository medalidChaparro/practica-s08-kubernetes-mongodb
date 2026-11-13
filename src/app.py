import os
from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mongo-service")
DB_NAME = os.getenv("DB_NAME", "practica_s08")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASS", "MongoS08_2026")

MONGO_URI = (
    f"mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:27017/"
    f"{DB_NAME}?authSource=admin"
)

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client[DB_NAME]

@app.route("/")
def home():
    return jsonify({
        "application": "Practica S08 - Backend API",
        "database": DB_NAME,
        "message": "Backend desplegado correctamente en Kubernetes",
        "status": "Running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/db")
def database():
    try:
        client.admin.command("ping")
        return jsonify({
            "connection": "successful",
            "database": DB_NAME,
            "message": "Conexion con MongoDB exitosa"
        })
    except PyMongoError as error:
        return jsonify({
            "connection": "failed",
            "message": str(error)
        }), 503

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("APP_PORT", "5000"))
    )

