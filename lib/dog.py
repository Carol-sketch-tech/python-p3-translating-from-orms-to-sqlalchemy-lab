from models import Dog

def create_table(base):
    sql = '''
            CREATE TABLE dogs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT,
            age INTEGER) '''
    CONN.execute(sql)
    CONN.commit()
    pass

def save(session, dog):
    pass

def get_all(session):
    pass

def find_by_name(session, name):
    pass

def find_by_id(session, id):
    pass

def find_by_name_and_breed(session, name, breed):
    pass

def update_breed(session, dog, breed):
    pass