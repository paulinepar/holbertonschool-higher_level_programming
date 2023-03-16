#!/usr/bin/python3
'''
    script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
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

    # requete SQL pour selectionner les eats qui commencent par la lettre N
    filter = "SELECT * FROM states WHERE states.name \
              LIKE BINARY 'N%' ORDER BY states.id ACS"

    # execution de la requête SQL
    cur.execute(filter)

    # recuperation des resultats
    results = cur.fetchall()

    # for et print pour afficher les resultats
    for row in results:
        print(row)
