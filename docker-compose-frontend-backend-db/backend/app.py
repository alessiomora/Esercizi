from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"]
    )
    return conn

@app.route('/api/data')
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT message FROM greetings")
    rows = cur.fetchall()  # fetch all rows
    cur.close()
    conn.close()

    # Extract messages from rows (each row is a tuple like: ('Hello',))
    messages = [row[0] for row in rows]

    return jsonify({'messages': messages})


@app.route("/api/add", methods=["POST"])
def add_data():
    data = request.get_json()
    msg = data.get("message")
    if not msg:
        return jsonify({"error": "No message provided"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO greetings (message) VALUES (%s)", (msg,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "ok", "message": msg})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)