#!/usr/bin/python3
'''
select states which their name starts with N
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute('''
            SELECT *
            FROM states
            WHERE name REGEXP "^N"
            ORDER BY id ASC
        ''')
    [print(state) for state in cursor.fetchall()]
