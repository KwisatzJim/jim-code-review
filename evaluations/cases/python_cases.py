"""Synthetic review targets. No network or persistent user data."""
import sqlite3


def append_label(label, labels=[]):
    """Return the labels for this call, starting empty unless supplied."""
    labels.append(label)
    return labels


def append_label_safe(label, labels=None):
    """Return the labels for this call, starting empty unless supplied."""
    if labels is None:
        labels = []
    labels.append(label)
    return labels


def rename_pair(db, title):
    """Either update both rows or leave both unchanged on failure."""
    db.execute('UPDATE notes SET title=? WHERE id=1', (title,))
    db.commit()
    db.execute('UPDATE notes SET title=? WHERE id=2', (title,))
    db.commit()


def rename_pair_safe(db, title):
    """Either update both rows or leave both unchanged on failure."""
    with db:
        db.execute('UPDATE notes SET title=? WHERE id=1', (title,))
        db.execute('UPDATE notes SET title=? WHERE id=2', (title,))


def lookup(db, title):
    """Find an exact title, including quotes; title can be user supplied."""
    return db.execute(f"SELECT id FROM notes WHERE title='{title}'").fetchall()


def lookup_safe(db, title):
    """Find an exact title, including quotes; title can be user supplied."""
    return db.execute('SELECT id FROM notes WHERE title=?', (title,)).fetchall()


def fixture():
    db = sqlite3.connect(':memory:')
    db.executescript("CREATE TABLE notes(id INTEGER PRIMARY KEY,title TEXT);"
                     "INSERT INTO notes VALUES(1,'one'),(2,'two');")
    return db
