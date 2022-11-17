import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="telemedicina2123"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM post.dati_famigliari")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#inserisco nuovi record
nome=input("inserisci nome: ")
cognome=input("inserisci cogome: ")
peso=input("inserisci peso: ")
altezza=float(input("inserisci l'altezza: "))
mycursor = mydb.cursor()
sql = "INSERT INTO post.dati_famigliari(nome,cognome,peso,altezza)VALUES (%s,%s,%s,%s);" 
val = (nome,cognome,peso,altezza)
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


