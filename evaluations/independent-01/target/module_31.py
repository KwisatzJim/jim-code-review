import sqlite3

def apply(db, title):
    """Either update both rows or leave both unchanged on failure."""
    with db:
        db.execute('UPDATE notes SET title=? WHERE id=1', (title,))
        db.execute('UPDATE notes SET title=? WHERE id=2', (title,))
