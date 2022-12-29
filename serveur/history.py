import cgi 
import sqlite3
import json


dict_result= {}

form = cgi.FieldStorage()


print(form.getvalue("nom"))

name = form.getvalue("nom") 




print(form.getvalue("vie"))

vie = form.getvalue("vie") 




print(form.getvalue("xp"))

xp = form.getvalue("xp") 



print(form.getvalue("mana"))

mana = form.getvalue("mana") 




connection = sqlite3.connect('ma_base.db')



cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT,
         xp TEXT,
         mana TEXT, 
         vie TEXT

    )
""")


cursor.execute("""INSERT INTO users (name, xp, vie, mana) VALUES (?, ?, ?, ?)
""", (name,xp,vie,mana))



cursor.execute("""SELECT * FROM users """)





names = cursor.fetchall() 


for name in names :
        dict_result[name[0]] = (
        {
            "nom": name[1], 
            "mana":name[2], 
            "vie":name[3],
            "xp":name[4]

        }
    )


json_result = json.dumps(dict_result, indent = 4)
print(json_result)


connection.commit()



connection.close()

