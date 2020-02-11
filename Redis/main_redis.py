import sys
sys.path.insert(1, 'D:\Code\Python-Matrice\Redis\'')

import 00_get_put.py
import 01_exists.py
import 02_delete.py
import 03_incr.py

def main():
    database = {}

    put("toto", "tata")
    get("toto")


if __name__ == '__main__':
    main()
