from tkinter import *

window = Tk()
window.title("BKI Calculator")
window.minsize(width=250, height=250)

#Kilo Label
weight_label = Label(text="Enter your weight (kg)",
                    font=("Arial", 12, "normal"),
                    padx=20,
                    pady=20)
weight_label.pack()

#Kilo Input
weight_entry = Entry(
    width=10
)
weight_entry.pack()

#Uzunluk Label
height_label = Label(text="Enter your height (cm)",
                    font=("Arial", 12, "normal"),
                    padx=20,
                    pady=20)
height_label.pack()

#Uzunluk Input
height_entry = Entry(
    width=10
)
height_entry.pack()

#Sonuc Label
result_ticket = Label(text="")
result_ticket.pack(side="bottom")

#BKI Hesaplama Fonksiyonu
def calculate_bki():
    weight_input = int(weight_entry.get())
    height_input = int(height_entry.get())
    # BKI hesaplama formülü
    bki = weight_input / ((height_input / 100) ** 2)
    result_ticket.config(text="Sonuç: " + str(bki))

    if bki <= 18.5:
        result_ticket.config(text="Çok zayifsiniz. " + str(bki))
    elif bki > 18.5 and bki < 24.9:
        result_ticket.config(text="Normal kilodasiniz. " + str(bki))
    elif bki > 25 and bki < 29.9:
        result_ticket.config(text="Aşiri kilodasiniz. " + str(bki))
    elif bki > 30 and bki < 34.9:
        result_ticket.config(text="Obez durumdasiniz dikkatli olun! " + str(bki))
    elif bki > 35 and bki < 39.9:
        result_ticket.config(text="Morbid obez durumdasiniz acil olarak doktora görünün! ! " + str(bki))
    else:
        result_ticket.config(text="Yanliş Değerler Girdiniz.")

#Hesaplama butonu
calculate_btn = Button(text="Calculate",
                        width=7,
                        height=3,
                        bg="black",
                        fg="white",
                        command=calculate_bki)
calculate_btn.pack(side="bottom")



window.mainloop()
