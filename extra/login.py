username = 'bayar'
password = '123456'
attempts = 0
blocked = False

while True:
    if blocked:
        choice = input("Таны бүртгэл түгжигдсэн байна. Нууц үгээ сэргээхийг хүсч байна уу? (тийм/үгүй): ").strip().lower()
        if choice == 'тийм':
            new_pw = input("Шинэ нууц үгээ оруулна уу: ")
            second_new_pw = input("Шинэ нууц үгээ дахин оруулна уу: ")

            if new_pw == second_new_pw:
                password = new_pw    
                print("Таны нууц үг амжилттай шинэчлэгдлээ. Одоо нэвтрэхийг оролдож болно.")
                attempts = 0
                blocked = False 
            else:
                print("Нууц үг тохирсонгүй. Нууц үг солих үйлдэл цуцлагдлаа.")
            
        else:
            print("Нууц үг сэргээхийг цуцаллаа. Програмаас гарч байна...")
            break

    un = input("Хэрэглэгчийн нэрээ оруулна уу: ")
    pw = input("Нууц үгээ оруулна уу: ")

    if un == username and pw == password:
        print("Нэвтрэлт амжилттай!")
        break
    else:
        attempts += 1
        print(f"{attempts} дахь оролдлого: Хэрэглэгчийн нэр эсвэл нууц үг буруу байна.")

        if attempts >= 3:
            print("Хэт олон удаа буруу орууллаа. Таны бүртгэл түгжигдлээ.")
            blocked = True
