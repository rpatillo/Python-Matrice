database = {}

def put(key, value):
    database[key] = value

def get(key):
    database.get(key)

def exists(key):
    if key in database:
        return(True)
    return(False)
    
def delete(key):
    del database[key]