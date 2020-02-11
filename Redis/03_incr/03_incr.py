database = {}

def put(key, value):
    database[key] = value

def get(key):
    return(database.get(key))

def exists(key):
    if key in database:
        return(True)
    return(False)
    
def delete(key):
    del database[key]

def incrby(key, delta=1):
    if exists(key) and isinstance(database[key], (int, float)) and isinstance(delta, (int, float)):
        database[key] += delta

def main():
    print("main")
    
if __name__ == '__main__':
    main()