from tkinter import *
import random
#--------------choose_num-----------
user_choose=random.randint(0,10)

#----------------compare----------------
def control(guess_num, user_num):
    if int(guess_num)==user_num:
        check_label.config(text="Congratulations")
    elif int(guess_num)<user_num:
        check_label.config(text="More Up")
    elif int(guess_num)>user_num:
        check_label.config(text="More Down")

def start_compare():
    num=guess_number.get()
    control(int(num), user_choose)

#---------------------GUI-----------------------
window=Tk()
window.minsize(width=275, height=130)
window.title("Sayı Tahmin Oyunu")

sayi_gir_label=Label(text="1-10 arasında sayı giriniz.", font=("Times New Roman",20,"bold"))
sayi_gir_label.grid(row=0,column=0)

guess_number=Entry(width=15)
guess_number.grid(row=1,column=0)

check_num_button=Button(text="Kontrol", font=("Times New Roman",12,"bold"), width=10, command=start_compare)
check_num_button.grid(row=2, column=0)

check_label=Label(bg="black", fg="white", text="I am here", font=("Times New Roman",12,"bold"))
check_label.grid(row=3, pady=5)

window.mainloop()

