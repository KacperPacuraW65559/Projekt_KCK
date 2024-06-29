from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                difficulty TEXT NOT NULL
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS bookmarks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson_id INTEGER,
                FOREIGN KEY (lesson_id) REFERENCES lessons (id)
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS completed_lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson_id INTEGER,
                FOREIGN KEY (lesson_id) REFERENCES lessons (id)
            );
        """)
    conn.close()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM lessons")
    lessons = cur.fetchall()
    return render_template('lessons.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>')
def lesson_detail(lesson_id):
    return render_template(f'lesson{lesson_id}.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/chords')
def chords():
    chords = [
        {"name": "C-dur", "image": "static/images/C_major_chord.png"},
        {"name": "G-dur", "image": "static/images/G_major_chord.png"},
        {"name": "A-mol", "image": "static/images/A_minor_chord.png"},
    ]
    return render_template('chords.html', chords=chords)

@app.route('/scales')
def scales():
    scales = [
        {"name": "Skala durowa C", "image": "static/images/C_major_scale.png"},
        {"name": "Skala molowa A", "image": "static/images/A_minor_scale.png"},
        {"name": "Pentatonika E", "image": "static/images/E_pentatonic_scale.png"},
    ]
    return render_template('scales.html', scales=scales)

@app.route('/add_bookmark/<int:lesson_id>')
def add_bookmark(lesson_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE lessons SET bookmarked = 1 WHERE id = ?", (lesson_id,))
    conn.commit()
    return redirect(url_for('lessons'))

@app.route('/remove_bookmark/<int:lesson_id>')
def remove_bookmark(lesson_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE lessons SET bookmarked = 0 WHERE id = ?", (lesson_id,))
    conn.commit()
    return redirect(url_for('lessons'))

@app.route('/complete_lesson/<int:lesson_id>')
def complete_lesson(lesson_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE lessons SET completed = 1 WHERE id = ?", (lesson_id,))
    conn.commit()
    return redirect(url_for('lessons'))

@app.route('/uncomplete_lesson/<int:lesson_id>')
def uncomplete_lesson(lesson_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE lessons SET completed = 0 WHERE id = ?", (lesson_id,))
    conn.commit()
    return redirect(url_for('lessons'))

@app.route('/metronome')
def metronome():
    return render_template('metronome.html')

if __name__ == '__main__':
    app.run(debug=True)
