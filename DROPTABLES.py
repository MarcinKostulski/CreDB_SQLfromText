import sqlite3

db_filename = 'leerplandoelen_db.sqlite3'

conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute("DROP TABLE Competenties;")
c.execute("DROP TABLE Deelcompetenties;")
c.execute("DROP TABLE Leerplandoelen;")

conn.commit()
c.close