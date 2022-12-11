from tkinter import *
from tkinter import ttk
from tkinter.font import ITALIC
from tkinter import messagebox
from tkcalendar import Calendar
from tkcalendar import *
import queries as sq
import ticket_page as tp
import history_page as hp

f = ('Times', 14)


class MenuPage:
    def __init__(self, app, userdata):
        app.geometry('1000x650')
        notebook = ttk.Notebook(app)
        tab_dashboard = Frame(notebook)
        notebook.add(tab_dashboard, text="Dashboard")
        tab_dashboard.config(bg="orange red")
        tab_profile = Frame(notebook)
        notebook.add(tab_profile, text="Profile")
        notebook.pack(expand=True, fill="both")
        tab_profile.config(bg="orange red")

        self.profileMenu(app, tab_profile, userdata)
        self.dashboardMenu(tab_dashboard, userdata[4], userdata[1], userdata)
        lbl = Label(app, font=('times', 12),
                    bg="orange red", foreground='black')
        lbl.pack(anchor='c')
        l1 = Label(app, text="Sistem Booking Lapangan Futsal",
                   bg="orange red", fg="black", font="times 12 italic")
        l1.pack(anchor='se')

        if __name__ == "__main__":
            app.mainloop()

    def dashboardMenu(self, tab_dashboard, province, email, userdata):
        frameholder_dashboard = Frame(
            tab_dashboard,
            relief=SOLID,
            padx=0,
            pady=0
        )
        frameholder_dashboard.place(x=120, y=45)
        menu2 = Frame(
            frameholder_dashboard,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=70,
            pady=10
        )
        menu2.grid(row=0, column=0, columnspan=2)

        self.data = sq.queryConnectField(province)

        self.variable_a = StringVar()
        self.variable_b = StringVar()

        self.optionmenu_a = OptionMenu(
            menu2, self.variable_a, *self.data.keys())
        self.optionmenu_b = OptionMenu(
            menu2, self.variable_b, 'Choose a City')
        self.optionmenu_a.config(
            width=23,
            font=('Times', 12)
        )
        self.optionmenu_a.grid(row=0, column=1, pady=10, padx=10)
        self.optionmenu_b.config(
            width=23,
            font=('Times', 12)
        )
        self.optionmenu_b.grid(row=0, column=3, pady=10, padx=10)

        self.variable_a.set('Select an Option')

        self.variable_a.trace('w', self.updateOption)

        Label(
            menu2,
            text="City", fg="black",
            bg='#CCCCCC',
            font=f).grid(row=0, column=0, sticky=W, pady=10)
        Label(
            menu2,
            text="Field", fg="black",
            bg='#CCCCCC',
            font=f).grid(row=0, column=2, sticky=W, pady=10)

        menu3 = Frame(
            frameholder_dashboard,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=50,
            pady=20)
        menu3.grid(row=1, column=0, sticky=NSEW)

        menu2hholder = LabelFrame(menu3, bd=0, bg='#CCCCCC',
                                  relief=SOLID, padx=5, pady=5)
        menu2hholder.pack()

        Label(
            menu2hholder,
            text="Date", fg="black",
            bg='#CCCCCC',
            font=f).grid(row=0, column=0, columnspan=2, sticky=W, pady=(0, 5))

        cal = Calendar(menu2hholder, selectmode='day',
                       year=2020, month=5, day=22)
        cal.grid(row=1, column=0, columnspan=2, pady=5, sticky=W)

        Label(menu2hholder, text="Time", fg="black", bg='#CCCCCC',
              font=f).grid(row=2, column=0,  pady=(10, 0), sticky=W)
        timeframe = LabelFrame(
            menu2hholder,
            bd=0,
            bg='#CCCCCC',
            relief=SOLID,
            padx=5,
            pady=5
        )
        timeframe.grid(row=3, column=0,  pady=5, sticky=W)
        hour_string = StringVar()
        min_sb = Spinbox(
            timeframe,
            from_=0,
            to=23,
            wrap=True,
            textvariable=hour_string,
            width=2,
            state="readonly",
            font=f,
            justify=CENTER
        )
        min_sb.grid(row=0, column=0)
        Label(timeframe, text=":", fg="black", bg='#CCCCCC',
              font=f).grid(row=0, column=1)
        min_string = StringVar()
        sec_hour = Spinbox(
            timeframe,
            from_=0,
            to=59,
            wrap=True,
            textvariable=min_string,
            font=f,
            width=2,
            justify=CENTER
        )
        sec_hour.grid(row=0, column=2)
        Label(menu2hholder, text="Duration", fg="black", bg='#CCCCCC',
              font=f).grid(row=2, column=1,  pady=(10, 0), sticky=W)
        durationframe = LabelFrame(
            menu2hholder,
            bd=0,
            bg='#CCCCCC',
            relief=SOLID,
            padx=5,
            pady=5
        )
        durationframe.grid(row=3, column=1,  pady=5, sticky=W)
        dur = StringVar()
        duration = Spinbox(
            durationframe,
            from_=0,
            to=59,
            wrap=True,
            textvariable=dur,
            font=f,
            width=2,
            justify=CENTER
        )
        duration.grid(row=0, column=0)
        Label(durationframe, text="Hour", fg="black", bg='#CCCCCC',
              font=f).grid(row=0, column=1)

        menu4 = Frame(
            frameholder_dashboard,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=50,
            pady=20
        )
        menu4.grid(row=1, column=1, sticky=NSEW)
        Label(menu4, text="Payment Method", fg="black", bg='#CCCCCC',
              font=f).pack(pady=5)
        pmethods = LabelFrame(menu4, bd=0, bg='#CCCCCC',
                              relief=SOLID, padx=5, pady=5)
        pmethods.pack(pady=5)
        payment = StringVar()
        varrmenu4 = {}
        payname = ["Debit Card", "Credit Card",
                   "E-Wallet A", "E-Wallet B", "Cash"]
        for i, value in enumerate(payname):
            varrmenu4[value] = Radiobutton(pmethods, text=value.capitalize(), bg='#CCCCCC',
                                           variable=payment, value=value, font=('Times', 12))
            varrmenu4[value].grid(row=i, column=0, pady=5, sticky=W)
        bookbtn = Button(
            menu4,
            width=15,
            text='Confirm Order',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=lambda: [sq.queryAddOrderData(email, self.variable_a.get(), cal.get_date(
            ), f"{hour_string.get().zfill(2)}:{min_string.get().zfill(2)}", dur.get(), payment.get(), self.variable_b.get())],
            padx=5,
            pady=5
        )
        bookbtn.pack(pady=(10, 5))

        bookbtn2 = Button(
            menu4,
            width=15,
            text='Show Receipt',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=lambda: tp.TicketPage(userdata, self.variable_b.get(), cal.get_date(
            ), f"{hour_string.get().zfill(2)}:{min_string.get().zfill(2)}", dur.get(), payment.get(), self.variable_a.get()),
            padx=5,
            pady=5
        )
        bookbtn2.pack(pady=(10, 5))
    # print(f"{self.variable_a.get()} {self.variable_b.get()} {cal.get_date()} {hour_string.get()} {min_string.get()}")

    def updateOption(self, *args):
        countries = self.data[self.variable_a.get()]
        self.variable_b.set(countries[0])
        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')
        for country in countries:
            menu.add_command(
                label=country, command=lambda nation=country: self.variable_b.set(nation))

    def profileMenu(self, app, frame, userdata):
        menu_profile = Frame(
            frame,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=40,
            pady=0
        )
        menu_profile.place(x=285, y=70)
        Label(frame, text="Profile", font=('Times', 20),
              bg="orange red").place(x=285, y=30)
        profilelabel = [["Name\t:  ", userdata[0], "changename"], ["E-mail\t:  ", userdata[1], "changeemail"], ["Contact\t: ",
                        userdata[2], "changecontact"], ["Gender\t: ", userdata[3], "changegender"], ["Address\t: ", userdata[4], "changeaddress"]]
        varrprofile = {}
        for i, row in enumerate(profilelabel):
            for j, item in enumerate(row):
                if j == 0:
                    Label(menu_profile, text=item, fg="black", bg='#CCCCCC',
                          font=f).grid(row=i, column=0, sticky=W, pady=10)
                elif j == 1:
                    Label(menu_profile, text=item, fg="black", bg='#CCCCCC', font=f).grid(
                        row=i, column=1, sticky=W, pady=10)
                else:
                    if i >= 3:
                        varrprofile[item] = Button(menu_profile, width=3, text=">", font=f, relief=SOLID,
                                                   cursor='hand2', command=lambda item=item: self.editWindow2(item[6:], userdata[1])).grid(row=i, column=2, sticky=W, pady=10, padx=15)
                    else:
                        varrprofile[item] = Button(menu_profile, width=3, text=">", font=f, relief=SOLID,
                                                   cursor='hand2', command=lambda item=item: self.editWindow(item[6:], userdata[1])).grid(row=i, column=2, sticky=W, pady=10, padx=15)

        b1 = Button(
            menu_profile,
            width=15,
            text='History',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=lambda: hp.HistoryPage(userdata)
        )
        b1.grid(row=5, column=1, pady=10, padx=10)
        b2 = Button(
            menu_profile,
            width=15,
            text='Exit',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=lambda: [app.destroy()]
        )
        b2.grid(row=6, column=1, pady=10, padx=10)

    def editWindow(self, context, id):
        editwindow = Tk()
        editwindow.title("Edit Profile")
        editwindow.geometry("293x155")
        editwindow.config(bg="orange red")
        editframe = Frame(editwindow, bd=2, bg='#CCCCCC',
                          relief=SOLID, padx=10, pady=0)
        editframe.place(x=1, y=1)
        Label(editframe, text=f"Edit {context}".title(), font=f, bg='#CCCCCC').grid(
            row=0, column=0, columnspan=2, pady=10, padx=10)
        changeinput = Entry(editframe, font=f, width=27)
        changeinput.grid(
            row=1, column=0, columnspan=2, pady=10, padx=10)
        okbtn = Button(editframe, width=5, text='OK', font=f,
                       relief=SOLID, cursor='hand2', command=lambda: [sq.updateData(context, changeinput.get(), id), messagebox.showinfo(
                           'Edit Status', 'Success!\nExit to see changes'), editwindow.destroy()] if changeinput.get() != '' else messagebox.showerror('Edit Status', 'Error\nValue cannot be empty!'))
        okbtn.grid(row=2, column=0, pady=10, padx=2)
        cancelbtn = Button(editframe, width=5, text='Cancel', font=f,
                           relief=SOLID, cursor='hand2', command=editwindow.destroy)
        cancelbtn.grid(row=2, column=1, pady=10, padx=2)

    def editWindow2(self, context, id):
        editwindow = Toplevel()
        editwindow.title("Edit Profile")
        editwindow.geometry("300x165")
        editwindow.config(bg="orange red")
        editwindow.resizable(False, False)
        editframe = Frame(editwindow, bd=2, bg='#CCCCCC',
                          relief=SOLID, padx=22, pady=0)
        editframe.place(x=1, y=1)
        Label(editframe, text=f"Edit {context}".title(), font=f, bg='#CCCCCC').grid(
            row=0, column=0, columnspan=2, pady=10, padx=10)
        if context == 'gender':
            var = StringVar()
            var.set('others')
            genderframe = LabelFrame(editframe, bg='#CCCCCC', padx=0, pady=0)
            genderframe.grid(row=1, column=0, columnspan=2, pady=10, padx=20)
            varname = ['radmale', 'radfemale', 'radothers']
            varr = {}
            for value in varname:
                varr[value] = Radiobutton(genderframe, text=value[3:].capitalize(), bg='#CCCCCC',
                                          variable=var, value=value[3:], font=('Times', 12))
                varr[value].pack(expand=True, side=LEFT)
            okbtn = Button(editframe, width=5, text='OK', font=f,
                           relief=SOLID, cursor='hand2', command=lambda: [sq.updateData(context, var.get(), id), messagebox.showinfo(
                               'Edit Status', 'Success!\nExit to see changes'), editwindow.destroy()] if var.get() != '' else messagebox.showerror('Edit Status', 'Error\nValue cannot be empty!'))
            okbtn.grid(row=2, column=0, pady=10, padx=2)
        else:
            variable = StringVar()
            variable.set("Select an Option")
            provinces = ['Banten', 'DKI Jakarta', 'Jawa Barat',
                         'Jawa Tengah', 'DI Yogyakarta', 'Jawa Timur']
            optmenu = OptionMenu(editframe, variable, *provinces)
            optmenu.config(width=23, font=('Times', 12))
            optmenu.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
            okbtn = Button(editframe, width=5, text='OK', font=f,
                           relief=SOLID, cursor='hand2', command=lambda: [sq.updateData("province", variable.get(), id), messagebox.showinfo(
                               'Edit Status', 'Success!\nExit to see changes'), editwindow.destroy()] if variable.get() != '' else messagebox.showerror('Edit Status', 'Error\nValue cannot be empty!'))
            okbtn.grid(row=2, column=0, pady=10, padx=2)
        cancelbtn = Button(editframe, width=5, text='Cancel', font=f,
                           relief=SOLID, cursor='hand2', command=editwindow.destroy)
        cancelbtn.grid(row=2, column=1, pady=10, padx=2)


if __name__ == "__main__":
    profiledata = ["Achmad Fahri", "a.fahrialhamdi@gmail.com",
                   "081517736131", "male", "Jawa Timur"]
    rootapp = Tk()
    rootapp.title('BookBall')
    rootapp.geometry('1000x600')
    rootapp.config(bg="orange red")

    menupage = MenuPage(rootapp, profiledata)
