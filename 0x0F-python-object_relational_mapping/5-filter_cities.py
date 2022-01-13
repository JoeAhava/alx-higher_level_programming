#!/usr/bin/python3
'''
select city by state
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
            SELECT c.id, c.name, s.name
            FROM cities as c
            LEFT JOIN states as s
            ON c.state_id = s.id
            WHERE s.name = '{name}'
            ORDER BY id ASC
        '''.format(name=sys.argv[4]))
    result = cursor.fetchall()
    count = 0
    for state in result:
        if count == len(result) - 1:
            print(state[1], end="")
            break
        print(state[1], end=", ")
        count += 1

    print()
