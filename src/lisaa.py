from database_connection import get_database_connection

con = get_database_connection()

cur = con.cursor()

cur.execute("INSERT INTO users (username) VALUES ('mrjaahas')")

con.commit()

con.close