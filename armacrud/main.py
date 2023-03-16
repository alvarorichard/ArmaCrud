from flask import Flask, request
import psycopg2
from psycopg2.extras import RealDictCursor
from uuid import uuid4
import hashlib
app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )


@app.route("/read")
def read():
    try:
        conn = get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    except:
        return {
            "error": 1
        }


@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor) 
    senha = hashlib.md5((data['update']["pass"]).encode("utf-8")).hexdigest() 
    cur.execute(
        f"UPDATE users SET username = '{data['update']['user']}', password = '{senha}' WHERE id = '{data['uuid']}'")
    conn.commit()
    cur.close()
    conn.close()
    return {
        "error": 0,
        "message": f"Updated {data['uuid']}"
    }


@app.route('/create', methods=["POST"])
def create():
    data = request.get_json()
    try:
        conn = get_conn()
        cur = conn.cursor()
        senha = hashlib.md5((data["pass"]).encode("utf-8")).hexdigest()
        id_val = uuid4()
        cur.execute(
            f"INSERT INTO users (id, username, password) VALUES ('{id_val}', '{data['user']}', '{senha}')")
        conn.commit()
        cur.close()
        conn.close()
        return {
            "error": 0
        }
    except:
        return {
            "error": 1
        }


@app.route("/delete", methods=["POST"])
def delete():
    data = request.get_json()
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM users WHERE id = '{data['id']}'")
        conn.commit()
        cur.close()
        conn.close()
        return {
            "error": 0,
            "message": f"deleted {data['id']}"

        }
    except:
        return {
            "error": 1
        }





def main():
    app.run()
