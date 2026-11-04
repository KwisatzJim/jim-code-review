import sqlite3

def apply(label, labels=[]):
    """Return the labels for this call, starting empty unless supplied."""
    labels.append(label)
    return labels
