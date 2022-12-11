import sqlite3
from tkinter import messagebox

dbpath = 'database/maindata.db'

con = sqlite3.connect(dbpath)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS accountdata(
                    name text,
                    email text,
                    contact number,
                    gender text,
                    province text,
                    password text
                )
            ''')
con.commit()
con.close()

con = sqlite3.connect(dbpath)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS fielddata(
                    province text,
                    city text,
                    field text,
                    fieldid text
                )
            ''')
con.commit()
con.close()

con = sqlite3.connect(dbpath)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS orderdata(
                    orderid text,
                    fieldid text,
                    email text,
                    city text,
                    date text,
                    hour text,
                    duration text,
                    method text
                )
            ''')
con.commit()
con.close()


def insertQueryUser(name, email, contact, gender, province, password):
    capname = name.get()
    capname = capname.title()
    try:
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute("INSERT INTO accountdata VALUES (:name, :email, :contact, :gender, :province, :password)", {
            'name': capname,
            'email': email.get(),
            'contact': contact.get(),
            'gender': gender.get(),
            'province': province.get(),
            'password': password.get()
        })
        con.commit()
        con.close()
        messagebox.showinfo('confirmation', 'accountdata Saved')
    except Exception as ep:
        messagebox.showerror('ERROR', ep)


def insertQueryField(province, city, field, fid):
    try:
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute("INSERT INTO fielddata VALUES (:province, :city, :field)", {
            'province': province.get(),
            'city': city.get(),
            'field': field.get(),
            'fieldid': fid.get()
        })
        con.commit()
        con.close()
        # messagebox.showinfo('confirmation', 'fielddata Saved')
    except Exception as ep:
        messagebox.showerror('ERROR', ep)


def queryConnect():
    try:
        con = sqlite3.connect(dbpath)
        cursor = con.execute(
            "SELECT * FROM accountdata")
        logindata = [row for row in cursor]
        con.commit()
        return logindata

    except Exception as ep:
        messagebox.showerror('', ep)


def updateData(column, value, id):
    try:
        con = sqlite3.connect(dbpath)
        con.cursor().execute(
            f"UPDATE accountdata set {column} = '{value}' WHERE email = '{id}'")
        con.commit()

    except Exception as ep:
        messagebox.showerror('', ep)


def queryConnectField(province):
    def convert(tup):
        di = {}
        for a, b in tup:
            di.setdefault(a, []).append(b)
        return di
    try:
        con = sqlite3.connect(dbpath)
        cursor = con.execute(
            f"SELECT city, field FROM fielddata WHERE province = '{province}'")
        tempdata = [row for row in cursor]
        dict = convert(tempdata)
        con.commit()
        return dict
    except Exception as ep:
        messagebox.showerror('', ep)


def deleteTable(table):
    con = sqlite3.connect(dbpath)
    con.execute(f"DROP TABLE {table}")
    con.commit()
    con.close()


def queryAddOrderData(email, city, date, hour, duration, method, field):
    orderid = createOrderId(email, city, field)
    fieldid = getFieldid(field)
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    cur.execute("INSERT INTO orderdata VALUES (:orderid, :fieldid, :email, :city, :date, :hour, :duration,  :method)", {
        "orderid": orderid,
        "fieldid": fieldid,
        "email": email,
        "city": city,
        "date": date,
        "hour": hour,
        "duration": duration,
        "method": method
    })
    con.commit()
    con.close()
    messagebox.showinfo("Success", "Order Success!")


def queryGetOrderNum():
    con = sqlite3.connect(dbpath)
    cursor = con.execute(f"SELECT * FROM orderdata")
    data = [row for row in cursor]
    count = str(len(data)).zfill(3)
    con.commit()
    return count


def deleterow(table, column, context):
    con = sqlite3.connect(dbpath)
    mycursor = con.cursor()
    if context == "all":
        sql = f"DELETE FROM {table}"
    else:
        sql = f"DELETE FROM {table} WHERE {column} = '{context}'"
    mycursor.execute(sql)
    con.commit()


def getFieldid(field):
    con = sqlite3.connect(dbpath)
    cursor = con.execute(
        f"SELECT fieldid FROM fielddata WHERE field = '{field}'")
    for row in cursor:
        return row[0]


def getField(id):
    con = sqlite3.connect(dbpath)
    cursor = con.execute(
        f"SELECT field FROM fielddata WHERE fieldid = '{id}'")
    for row in cursor:
        return row[0]


def createOrderId(email, city, field):
    emailcut = email.split("@")[0].upper()
    citycut = city[0:3].upper()
    fieldid = getFieldid(field)
    orderid = f"{queryGetOrderNum()}{emailcut}{citycut}{fieldid}"
    return orderid


def getOrderData(id):
    con = sqlite3.connect(dbpath)
    cursor = con.execute(f"SELECT * FROM orderdata WHERE orderid = '{id}'")
    data = [row for row in cursor]
    con.commit()
    for row in data:
        return row


def getUserOrderHistory(email):
    con = sqlite3.connect(dbpath)
    cursor = con.execute(f"SELECT * FROM orderdata WHERE email = '{email}'")
    data = [row for row in cursor]
    con.commit()
    return data


def findOrderId(email, city, date, hour, duration, method):
    con = sqlite3.connect(dbpath)
    cursor = con.execute(
        f"SELECT orderid FROM orderdata WHERE email='{email}' and city='{city}' and date='{date}' and hour='{hour}' and duration='{duration}' and method='{method}'"
    )
    data = [row for row in cursor]
    con.commit()
    for row in data:
        return row[0]


def getUserData(email):
    con = sqlite3.connect(dbpath)
    cursor = con.execute(
        f"SELECT * FROM accountdata WHERE email = '{email}'")
    data = [row for row in cursor]
    con.commit()
    return data[0]


def getProvince():
    con = sqlite3.connect(dbpath)
    cursor = con.execute(
        f"SELECT province FROM fielddata")
    data = [row for row in cursor]
    con.commit()
    data = list(dict.fromkeys(data))
    newdata = []
    for row in data:
        newdata.append(row[0])
    return newdata


if __name__ == "__main__":
    print('')
    print(getProvince())
