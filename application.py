import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
from psycopg2 import paramstyle

load_dotenv()

app = Flask(__name__)

engine = create_engine("postgresql://postgres:5tq60Dyaze1ni8KBKavL@containers-us-west-47.railway.app:6686/railway")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    leer = text("SELECT * FROM flights")
    flights = db.execute(leer).fetchall()
    return render_template("index.html", flights=flights)


@app.route("/agregar", methods=["POST","GET"])
def agregar():
    return render_template("crud.html")

@app.route("/crud", methods=["POST","GET"])
def crud():
    origen = request.form.get("origen")
    destino = request.form.get("destino")
    duracion = request.form.get("tiempo")
    agregar = text("INSERT INTO flights (origin, destination, duration) VALUES (?, ?, ?)")
    db.execute(agregar, {"origin": origen, "destination": destino, "duration": duracion})
    
    db.commit()
    db.close()
        