import sqlite3

db_filename = 'leerplandoelen_db.sqlite3'

conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute("CREATE TABLE Competenties(nummer TEXT PRIMARY KEY, omschrijving TEXT);")
c.execute("CREATE TABLE Deelcompetenties(nummer TEXT PRIMARY KEY, omschrijving TEXT);")
c.execute("CREATE TABLE Leerplandoelen(nummer TEXT PRIMARY KEY, omschrijving TEXT)")

with open('leerplandoelen_text.txt', 'r') as f:
    for line in f:
        if line.startswith("Competentie"):
            dashIndex = line.index('-')
            nummer = line[len('Competenties'):dashIndex]
            omschrijving = str(line[dashIndex+1:])
            print(f"C {nummer} {omschrijving}")
            c.execute(f"INSERT INTO Competenties VALUES('{nummer}', '{omschrijving}')")

        elif line.startswith("Deelcompetentie"):
            dashIndex = line.index('-' )
            nummer = line[len('Deelcompetentie'):dashIndex]
            omschrijving = str(line[dashIndex+1:])
            print(f"D {nummer} {omschrijving}")
            c.execute(f"INSERT INTO Deelcompetenties VALUES('{nummer}', '{omschrijving}')")

        else:
            if line.strip() == "":
                print("EMPTY")
            else:
                nummer = line[0:6]
                omschrijving = str(line[len(nummer):])
                print(f"L {nummer} {omschrijving}")
                c.execute(f"INSERT INTO Leerplandoelen VALUES('{nummer}', '{omschrijving}')")

    conn.commit()
c.close