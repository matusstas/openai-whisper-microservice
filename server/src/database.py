from tinydb import TinyDB, Query

def get_db():
    """
    Connect to TinyDB.
    """
    db = TinyDB("db/models.json")
    return db
