import sqlite3

class Not_id(Exception):
    pass
class Vazifa_except(Exception):
    pass

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
            try:
                matn=input("Vazifa matnini kiriting:")
                if not matn.strip():
                    raise Vazifa_except("Vazifa bo'sh bo'lishi mumkin emas!")
                with get_connection() as conn:
                    cur=conn.cursor()
                    cur.execute("insert into vazifalar(matn) values (?)" ,(matn,))
                    conn.commit()
                    print("Vazifa saqlandi!")
                    break
            except Exception as e:
                print(e)
            

    def show_vazifalar():
        with get_connection() as conn:
            cur=conn.cursor()
            cur.execute("select * from vazifalar")
            vazifalar=cur.fetchall()
            print("""
<<Vazifalar>>""")
            for id,task in vazifalar:
                print(f"{id}. {task}") 
        return None


    def delete_vazifa():
        try:
            while True:
                try:
                    id=input("O'chirmoqchi bo'lgan vazifangiz id sini kiriting:")
                    if not id.strip():
                        raise Not_id("ID kiritilmagan!")
                    elif not id.isdigit():
                        raise Not_id("Iltimos raqam kiriting!")
                    break

                except Exception as e:
                    print(e)
            
            with get_connection() as conn:
                cur=conn.cursor()
                cur.execute("select id from vazifalar")
                result=[]
                for i in cur.fetchall():
                    result.append(i[0])
                if not int(id) in result:
                    raise Not_id("Bu id mavjud emas!")
                
                cur.execute("delete from vazifalar where id=?", (id,))
                conn.commit()
                print("Vazifa o'chirildi!")
        except Exception as e:
            print(e)

    if tanlov=='1':
        add_vazifa()

    elif tanlov=='2':
        show_vazifalar()
    
    elif tanlov=='3':
        delete_vazifa()






