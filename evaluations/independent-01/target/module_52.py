import sqlite3

def apply(label, labels=None):
    """Return the labels for this call, starting empty unless supplied."""
    if labels is None:
        labels = []
    labels.append(label)
    return labels
