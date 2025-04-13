from tkinter import *
import os
import sqlite3
from tkinter import ttk
from tkinter import messagebox

def img(file_name):
    return PhotoImage(file=os.path.join(os.path.dirname(__file__), file_name))

class sweet_hours:
    cartlist = [["5 Pepper", "Medium", "02", 770]]  # dummy data
    amount = 770

    def main(sf):
        sf.scr = Tk()
        sf.scr.geometry("1366x768")
        sf.scr.title("Welcome to the world of sweet")
        sf.scr.iconbitmap(os.path.join(os.path.dirname(__file__), 'icon.ico'))

        sf.main_frame1 = Frame(sf.scr, height=100, width=1366)
        sf.logo = img("1.png")
        sf.Label = Label(sf.main_frame1, image=sf.logo)
        sf.Label.place(x=0, y=0)
        sf.main_frame1.pack(fill=BOTH, expand=1)

        sf.main_frame2 = Frame(sf.scr, height=668, width=1366)
        sf.canvas = Canvas(sf.main_frame2, height=610, width=1366)
        sf.canvas.pack()
        sf.back = img("2.png")
        sf.canvas.create_image(683, 284, image=sf.back)

        # Button to directly open pay_page
        sf.lab_button = Button(
            sf.main_frame2,
            text="WELCOME to \n the World of HAPPINESS",
            command=lambda: sf.pay_page("deli"),
            cursor="hand2",
            bd=10,
            font=("cooper black", 30, 'bold'),
            fg="white",
            bg="#0b1335"
        )
        sf.lab_button.place(x=410, y=200)
        sf.main_frame2.pack(fill=BOTH, expand=1)

        sf.scr.mainloop()

    def pay_page(sf, x):
        sf.x = x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title("Welcome to the world of sweet")
        sf.scr.geometry("1366x768")
        sf.scr.iconbitmap(os.path.join(os.path.dirname(__file__), 'icon.ico'))

        sf.order_f1 = Frame(sf.scr, height=100, width=1366)
        sf.logo = img("1.PNG")
        Label(sf.order_f1, image=sf.logo, height=150).place(x=0, y=0)
        sf.order_f1.pack(fill=BOTH, expand=1)

        sf.order_f2 = Frame(sf.scr, height=618, width=1366)
        sf.canvas = Canvas(sf.order_f2, height=618, width=1366)
        sf.canvas.pack()
        sf.logo1 = img("a3.png")
        sf.canvas.create_image(683, 309, image=sf.logo1)

        sf.home = Button(sf.order_f1, text="Log Out", command=lambda: print("Logout Clicked"), bg="#0b1335", cursor="hand2", fg="white", bd=5, font=("default", 16, 'bold'))
        sf.home.place(x=1100, y=60)

        sf.log_order = Label(sf.order_f2, text="SCAN FOR PAYMENT", bg="saddlebrown", fg="beige", width=18, font=("Cooper Black", 22, 'bold'))
        sf.log_order.place(x=880, y=26)

        sf.canvas.create_rectangle(1325, 90, 825, 500, fill="burlywood", outline="black", width=6)
        sf.amt = sf.amount
        sf.text = "Total : " + str(sf.amt)

        sf.tot = Label(sf.order_f2, text=sf.text, bg="#f2da9d", width=12, font=("Cooper Black", 22, 'bold'))
        sf.tot.place(x=950, y=510)

        # Dummy bindings
        sf.Address = lambda x: messagebox.showinfo("Pay", "Order placed via Delivery!")
        sf.orderpay = lambda x: messagebox.showinfo("Pay", "Order placed for Pickup!")
        sf.menulist = lambda x: messagebox.showinfo("Menu", "Redirect to Menu!")

        if sf.x == "deli":
            sf.y = sf.Address
        elif sf.x == "pick":
            sf.y = sf.orderpay

        sf.qr_img = img("qrcode.png")  # 🔁 Your QR image
        sf.canvas.create_image(1075, 290, image=sf.qr_img)

        sf.pay_btn = Button(
        sf.order_f2,
        text="I have paid",
        command=lambda: sf.payment_done(sf.x),
        bg="#0f3603",
        fg="white",
        font=("default", 16, 'bold'),
        bd=5,
        cursor="hand2"
        )
        sf.pay_btn.place(x=660, y=390)
        sf.canvas.create_text(1080, 105, font=("cooper black", 18))
        
        sf.add_button = Button(sf.order_f2, text="Add more", command=lambda: sf.menulist(sf.x), bg="#0b1335", cursor="hand2", fg="white", bd=5, font=("default", 16, 'bold'))
        sf.add_button.place(x=660, y=450)

        sf.order_f2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

# 🔥 Entry point
if __name__ == "__main__":
    app = sweet_hours()
    app.main()
