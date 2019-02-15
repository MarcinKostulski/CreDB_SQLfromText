import sqlite3

db_filename = 'leerplandoelen_db.sqlite3'

conn = sqlite3.connect(db_filename)
c = conn.cursor()

c.execute("CREATE TABLE Competentie(nummer INTEGER, omschrijving TEXT);")
c.execute("CREATE TABLE Deelconpetenties(nummer INTEGER, omschrijving TEXT);")
c.execute("CREATE TABLE Leerplandoelen(nummer INTEGER, omschrijving TEXT)")

with open('leerplandoelen_text.txt', 'r') as f:
    for line in f:
        if line.startswith("Competentie"):
            table = "Competentie"
            dashIndex = line.index('-')
            nummer = line[len('Competentie'):dashIndex]
            omschrijving = str(line[dashIndex+1:])
            print(f"C {nummer} {omschrijving}")
            c.execute(f"INSERT INTO {table} VALUES({nummer}, {omschrijving})")

        elif line.startswith("Deelcompetentie"):
            table = "Deelcompetenties"
            dashIndex = line.index('-')
            nummer = line[len('Deelcompetentie'):dashIndex]
            omschrijving = str(line[dashIndex+1:])
            print(f"D {nummer} {omschrijving}")
            c.execute(f"INSERT INTO {table} VALUES({nummer}, {omschrijving})")

        else:
            if line.strip() == "":
                print("EMPTY")
            else:
                table = "Leerplandoelen"
                nummer = line[0:5]
                omschrijving = str(line[len(nummer):])
                print(f"L {nummer} {omschrijving}")
                c.execute(f"INSERT INTO {table} VALUES({nummer}, {omschrijving})")

    conn.commit()
c.close