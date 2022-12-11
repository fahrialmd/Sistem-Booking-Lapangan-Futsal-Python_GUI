from tkinter import *
from tkcalendar import *
import queries as sq

f = ("Times", 14)
f1 = ("Times", 12)


class TicketPage:
    def __init__(self, userdata, field, date, hour, dur, method, city):
        app = Tk()
        app.title("Tiket")
        app.config(bg="#cd950c")
        app.resizable(False, False)

        email = userdata[1]
        name = userdata[0]
        contact = userdata[2]
        address1 = userdata[4]
        checkin = f"{date} {hour}"

        orderid = sq.findOrderId(email, city, date, hour, dur, method)

        ticket = Frame(app, bd=2, bg='#CCCCCC', relief=SOLID, padx=40, pady=40)
        ticket.pack()
        Label(ticket, text="PAYMENT DETAIL", fg="Black", bg='#CCCCCC', font=f).grid(
            row=0, column=0, columnspan=10, sticky=W, pady=(10, 0))

        Label(ticket, text="Order ID", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=1, column=0, sticky=W, pady=5)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=1, column=1, sticky=W, pady=5)
        Label(ticket, text=orderid, fg="Black", bg='#CCCCCC',
              font=f1).grid(row=1, column=2, sticky=W, pady=5)

        Label(ticket, text="Method", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=2, column=0, sticky=W, pady=5)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=2, column=1, sticky=W, pady=5)
        Label(ticket, text=method, fg="Black", bg='#CCCCCC',
              font=f1).grid(row=2, column=2, sticky=W, pady=5)

        Label(ticket, text="BOOKER DETAIL", fg="Black", bg='#CCCCCC', font=f).grid(
            row=3, column=0, columnspan=10, sticky=W, pady=10)

        Label(ticket, text="Name", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=4, column=0, sticky=W, pady=5)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=4, column=1, sticky=W, pady=5)
        Label(ticket, text=name, fg="Black", bg='#CCCCCC',
              font=f1).grid(row=4, column=2, sticky=W, pady=5)

        Label(ticket, text="Email", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=5, column=0, sticky=W, pady=10)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=5, column=1, sticky=W, pady=5)
        Label(ticket, text=email, fg="Black", bg='#CCCCCC',
              font=f1).grid(row=5, column=2, sticky=W, pady=5)

        Label(ticket, text="Contact", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=4, column=3, sticky=W, pady=5)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=4, column=4, sticky=W, pady=5)
        Label(ticket, text=contact, fg="Black", bg='#CCCCCC',
              font=f1).grid(row=4, column=5, sticky=W, pady=5)

        Label(ticket, text="Address", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=5, column=3, sticky=W, pady=5)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=5, column=4, sticky=W, pady=5)
        Label(ticket, text=address1, fg="Black", bg='#CCCCCC',
              font=f1).grid(row=5, column=5, sticky=W, pady=5)

        Label(ticket, text="FIELD DETAIL", fg="Black", bg='#CCCCCC', font=f).grid(
            row=6, column=0, columnspan=10, sticky=W, pady=10)

        Label(ticket, text="Field", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=7, column=0, sticky=W, pady=5)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=7, column=1, sticky=W, pady=5)
        Label(ticket, text=field, fg="Black", bg='#CCCCCC',
              font=f1).grid(row=7, column=2, sticky=W, pady=5)

        Label(ticket, text="Address", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=8, column=0, sticky=W, pady=5)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=8, column=1, sticky=W, pady=5)
        Label(ticket, text=city, fg="Black", bg='#CCCCCC',
              font=f1).grid(row=8, column=2, sticky=W, pady=5)

        Label(ticket, text="Check-in", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=7, column=3, sticky=W, pady=5)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=7, column=4, sticky=W, pady=5)
        Label(ticket, text=checkin, fg="Black", bg='#CCCCCC',
              font=f1).grid(row=7, column=5, sticky=W, pady=5)

        Label(ticket, text="Duration", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=8, column=3, sticky=W, pady=5)
        Label(ticket, text=":", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=8, column=4, sticky=W, pady=5)
        Label(ticket, text=f"{dur} Hour", fg="Black", bg='#CCCCCC',
              font=f1).grid(row=8, column=5, sticky=W, pady=5)

        if __name__ == "__main__":
            app.mainloop()


if __name__ == "__main__":
    TicketPage("002TULUSBATTB001")
