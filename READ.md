Bu dastur to-do app bo'lib unda vazifalarni saqlash ko'rish va o'chirish mumkin.
Vazifalar sqlite dan foydalanib info.db da saqlanadi, o'qiladi va o'zgartiriladi. 
Kod ikkita modulga bo'lib yozilgan ilova.py va vazifa.py. ilova.py da asosiy menyu ishlaydi vazifa.py da esa funksiylalar yozilgan va ularni ilova.py da import qilish orqali ishlatamiz.

Dasturdan foydalanish:
1, 2, 3, 0 raqamlaridan foydalangan holda kerakli amal tanlanadi va unga mos jarayon sodir bo'ladi

1. Vazifa qo'shish: add_vazifa() funksiyasi chaqiriladi va matn ko'rinishida vazifa kiritiladi agar hech narsa kiritilmasa xatolik sodir bo'ladi va vazifa kiritilgunicha qayta-qayta so'ryveradi, vazifa kiritilgach esa unga mos id ni biriktirgan holatda info.db ga saqlaydi.

2. Ro'yxatni ko'rish: show_vazifalar() funksiyasi chaqiriladi va info.db dagi barcha vazifalar ro'yxati ko'rsatiladi.

3. Vazifani o'chirish: delete_vazifa() funksiyasi chaqiriladi va id so'raladi agar id xato kiritilsa yoki kiritilmasa shunga mos xabar beriladi va to'g'ri id kiritilguncha shu jarayon takrorlanadi, id kiritilgach agar id mavjud bo'lsa shu id ga mos vazifa o'chiriladi agar bunday id mavjuid bo'lmasa bu haqida xabar beriladi va asosiy oynaga qaytiladi.

0. Chiqish: agar 0 tanlansa break yordamida sikl to'xtatiladi va "Dasturdan chiqildi!" degan xabar ko'rsatiladi.
   
8-bosqich uchun o'zgartirish kiritildi!
