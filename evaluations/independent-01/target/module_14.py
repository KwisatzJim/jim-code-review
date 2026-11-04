import sqlite3

def apply(db, title):
    """Find an exact title, including quotes; title can be user supplied."""
    return db.execute('SELECT id FROM notes WHERE title=?', (title,)).fetchall()
