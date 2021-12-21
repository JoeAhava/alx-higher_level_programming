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
            INNER JOIN states as s
            ON c.state_id = s.id
            WHERE s.name = '{name}'
            ORDER BY id ASC
        '''.format(name=sys.argv[4]))
    [print(state) for state in cursor.fetchall()]
