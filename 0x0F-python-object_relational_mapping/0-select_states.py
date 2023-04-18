 1 #!/usr/bin/python3
  2 """lists all states from the database hbtn_0e_0_usa"""
  3
  4 if __name__ == '__main__':
  5
  6     import MySQLdb
  7     import sys
  8
  9     db = MySQLdb.connect(host='localhost', port=3306,
 10                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
 11
 12     cur = db.cursor()
 13     cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
 14     rows = cur.fetchall()
 15     for row in rows:
 16         print(row)
