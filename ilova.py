import sqlite3

def get_connection():
    return sqlite3.connect("info.db")

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



    def add_vazifa():
        while True:
            matn=input("Vazifa matnini kiriting:")
            if matn:
                with get_connection() as conn:
                    cur=conn.cursor()
                    cur.execute("insert into vazifalar(matn) values (?)" ,(matn,))
                    conn.commit()
                    print("Vazifa saqlandi!")
                break

    def show_vazifalar():
        with get_connection() as conn:
            cur=conn.cursor()
            cur.execute("select * from vazifalar")
            vazifalar=cur.fetchall()
            for _ in vazifalar:
                print(_) 
        return None

    if tanlov=='1':
        add_vazifa()

    elif tanlov=='2':
        show_vazifalar()






