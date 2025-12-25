import mysql.connector

try:
    conn=mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    user='root',
    password='krishna@138',
    database='movies'
    )

    if conn.is_connected():
        print('DB connection successfully')

    cur=conn.cursor()
    # cur.execute('show databases;')
    # cur.execute('show tables;')
    # cur.execute('describe movies;')
    cur.execute('select*from movies;')

    for db in cur:
        movie_name = list(db)[1]
        if movie_name == 'magadheera':
            print(db)
    cur.close()
    conn.close()
except mysql.connector.Error as a:
    print('connection failed',a)
