#!/usr/bin/python3
'''
    script that lists all states from the database hbtn_0e_0_usa
'''

if __name__ == '__main__':
    import MySQLdb
    import sys


    # recuperation des arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # connection a la base de données
    db = MySQLdb.connect(host='localhost', port=3306, user=user, passwd=passwd, db=db)

    # creation de l'objet cursor
    cur = db.cursor()

    # execution de la requête SQL
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # recuperation des resultats
    results = cur.fetchall()

    # for et print pour afficher les resultats
    for row in results:
        print(row)
