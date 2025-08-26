import sqlite3
from vazifa import add_vazifa, show_vazifalar, delete_vazifa, get_connection


with get_connection() as conn:
    cur=conn.cursor()
    cur.execute("""create table if not exists vazifalar(
                id integer primary key autoincrement,
                matn text)
                """)
        

while True:
    tanlov=input("""
1. Vazifa qo'shish
2. Ro'yxatni ko'rish
3. Vazifani o'chirish
0. Chiqish
""")


    if tanlov=='1':
        add_vazifa()

    elif tanlov=='2':
        show_vazifalar()
    
    elif tanlov=='3':
        delete_vazifa()
    
    elif tanlov=='0':
        print("Dasturdan chiqildi!")
        break






