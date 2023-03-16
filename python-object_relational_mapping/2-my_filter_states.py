#!/usr/bin/python3
'''
    script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
'''
import MySQLdb
import sys

if __name__ == '__main__':

    # connection a la base de données
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    # creation de l'objet cursor
    cur = db.cursor()

    # execution de la requête SQL
    cur.execute("SELECT * FROM states WHERE name LIKE INARY '{:s}' \
                ORDER BY states.id ASC".format(sys.argv[4]))

    # recuperation des resultats
    values = cur.fetchall()

    # for et print pour afficher les resultats
    for row in values:
        print(row)
