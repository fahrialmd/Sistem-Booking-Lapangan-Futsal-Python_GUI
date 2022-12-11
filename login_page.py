from tkinter import *
from tkinter import messagebox
import queries as sq
import menu_page as mp

f = ('Times', 14)


class LoginPage:
    def __init__(self, app):
        # self.appPage = app
        self.indicator = False
        labelnameRF = ["Enter Name", "Enter E-mail", "Contact Number",
                       "Select Gender", "Select province", "Enter Password", "Re-Enter Password"]
        labelnameLF = ["E-mail", "Password"]
        varrRF = ['register_name', 'register_email', 'register_mobile', 'gender_frame', 'male_rb', 'female_rb',
                  'others_rb', 'register_province', 'register_pwd', 'pwd_again', 'register_btn']
        varrLF = ["email_tf", "pwd_tf", "login_btn"]
        varr = {}
        var = StringVar()
        var.set('male')
        provinces = sq.getProvince()
        variable = StringVar()
        variable.set(provinces[5])
        
        tleft_frame = Frame(
            app,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=10,
            pady=1
        )
        tleft_frame.place(x=130, y=90)
        Label(
            tleft_frame,
            text="SISTEM BOOKING\nLAPANGAN FUTSAL", fg="black",
            bg='#CCCCCC',
            font="TIMES 20 bold").grid(row=0, column=0, sticky=W, pady=69, padx=18)
        left_frame = Frame(
            app,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=12,
            pady=26
        )
        left_frame.place(x=130, y=299)
        for i, labelname in enumerate(labelnameLF):
            Label(left_frame, text=labelname, bg='#CCCCCC', font=f).grid(
                row=i, column=0, sticky=W, pady=10)
        for i, varname in enumerate(varrLF):
            if i == 2:
                varr[varname] = Button(
                    left_frame, width=15, text='Login', font=f, relief=SOLID, cursor='hand2', command=lambda: self.loginResponse(app, varr))
                varr[varname].grid(row=i, column=1, pady=10, padx=20)
            else:
                varr[varname] = Entry(left_frame, font=f,
                                      show='*' if i == 1 else '')
                varr[varname].grid(row=i, column=1, pady=10, padx=20)
        right_frame = Frame(
            app,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=10,
            pady=10
        )
        right_frame.place(x=460, y=90)
        for x in labelnameRF:
            Label(
                right_frame,
                text=x,
                bg='#CCCCCC',
                font=f).grid(row=labelnameRF.index(x), column=0, sticky=W, pady=10)
        for i, varname in enumerate(varrRF):
            if 0 <= i <= 2 or 8 <= i <= 9:
                varr[varname] = Entry(right_frame, font=f,
                                      show='*' if 8 <= i <= 9 else '')
                varr[varname].grid(row=i-3 if 8 <= i <= 9 else i,
                                   column=1, pady=10, padx=20)
            elif 3 <= i <= 6:
                if i == 3:
                    varr[varname] = LabelFrame(
                        right_frame, bg='#CCCCCC', padx=0, pady=0)
                    varr[varname].grid(row=i, column=1, pady=10, padx=20)
                else:
                    varr[varname] = Radiobutton(varr['gender_frame'], text=varname[:-3].capitalize(), bg='#CCCCCC',
                                                variable=var, value=varname[:-3], font=('Times', 10))
                    varr[varname].pack(expand=True, side=LEFT)
            elif i == 7:
                varr[varname] = OptionMenu(right_frame, variable, *provinces)
                varr[varname].config(width=23, font=('Times', 10))
                varr[varname].grid(row=i-3, column=1, pady=10, padx=20)
            else:
                varr[varname] = Button(right_frame, width=15, text='Register', font=f,
                                       relief=SOLID, cursor='hand2', command=lambda: self.insertRecord(var, variable, varr))
                varr[varname].grid(row=7, column=1, pady=10, padx=20)

    def insertRecord(self, var, variable, varr):
        check_counter = 0
        warn = ""
        if varr["register_name"].get() == "":
            warn = "Name can't be empty"
        else:
            check_counter += 1
        if varr["register_email"].get() == "":
            warn = "Email can't be empty"
        else:
            check_counter += 1
        if varr["register_mobile"].get() == "":
            warn = "Contact can't be empty"
        else:
            check_counter += 1
        if var.get() == "":
            warn = "Select Gender"
        else:
            check_counter += 1
        if variable.get() == "":
            warn = "Select province"
        else:
            check_counter += 1
        if varr["register_pwd"].get() == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1
        if varr["pwd_again"].get() == "":
            warn = "Re-enter password can't be empty"
        else:
            check_counter += 1
        if varr["register_pwd"].get() != varr["pwd_again"].get():
            warn = "Passwords didn't match!"
        else:
            check_counter += 1
        if check_counter == 8:
            sq.insertQuery(varr["register_name"], varr["register_email"],
                           varr["register_mobile"], var, variable, varr["register_pwd"])
        else:
            messagebox.showerror('Error', warn)

    def loginResponse(self, app, varr):
        logindata = sq.queryConnect()
        check_counter = 0
        if varr["email_tf"].get() == "":
            warn = "Username can't be empty"
        else:
            check_counter += 1
        if varr["pwd_tf"].get() == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1
        if check_counter == 2:
            check = False
            for row in logindata:
                if varr["email_tf"].get() == row[1] and varr["pwd_tf"].get() == row[5]:
                    check = True
                    messagebox.showinfo(
                        'Login Status', 'Success')
                    mp.MenuPage(app, row)
                    # self.windowDestroyer()
            if not check:
                print("error:\n", varr["email_tf"].get(), " == ",
                      row[1], varr["pwd_tf"].get(), " == ", row[5])
                messagebox.showerror(
                    'Login Status', 'Invalid username or password')
        else:
            messagebox.showerror(
                'Alert', warn)

    # def windowDestroyer(self):
    #     self.appPage.destroy()
