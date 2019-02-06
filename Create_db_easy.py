import sqlite3

db_filename = 'leerplandoelen_db.sqlite3'

conn = sqlite3.connect(db_filename)
c = conn.cursor()

with open('leerplandoelen_text.txt', 'r') as f:
    for line in f:
        if line.startswith("Competentie"):
            dashIndex = line.index('-')
            nummer = line[len('Competentie'):dashIndex]
            omschrijving = line[dashIndex+1:]
            print(f"C {nummer} {omschrijving}")
            #c.execute()
        elif line.startswith("Deelcompetentie"):
            print("D")
        else:
            if line.strip() == "":
                print("EMPTY")
            else:
                print("L")

conn.commit()
c.close