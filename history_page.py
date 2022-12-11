from tkinter import *
import queries as sq
import ticket_page as tp

f = ("Times", 12)

class HistoryPage:
    def __init__(self, userdata):
        root = Tk()
        root.title('History Page')
        root.geometry("430x300")
        root.resizable(False, False)

        # Create A Main Frame
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame,  bg='#CCCCCC')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = Scrollbar(
            main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
            scrollregion=my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas,  bg='#CCCCCC')

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        historydata = sq.getUserOrderHistory(userdata[1])
        # orderdata = sq.getOrderData()

        varr = {}
        # (sq.getOrderData(row[0])[0]

        Label(second_frame, text=f"User : {userdata[0]}", fg="black",
              bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W)
        for i, row in enumerate(historydata):
            Label(second_frame, text=f"ID: {row[0]}", bg='#CCCCCC', font=f).grid(
                row=i+1, column=0, sticky=W, padx=5)
            Label(second_frame, text=f"Date: {row[4]}", bg='#CCCCCC', font=f).grid(
                row=i+1, column=1, sticky=W, padx=5)
            varr[row[0]] = Button(second_frame, text="Show Receipt", command=lambda row=row: tp.TicketPage(userdata, sq.getField(sq.getOrderData(row[0])[1]), sq.getOrderData(row[0])[4], sq.getOrderData(row[0])[5], sq.getOrderData(row[0])[6], sq.getOrderData(row[0])[7], sq.getOrderData(row[0])[3])).grid(
                row=i+1, column=2, pady=10, padx=10, sticky=W)
        print(varr)
        # for thing in range(100):
        #     Button(second_frame, text=f'Button {thing} Yo!').grid(
        #         row=thing, column=0, pady=10, padx=10, command=)

        root.mainloop()


if __name__ == "__main__":
    userdata = ['Tulus', 'tulus@email.com',
                88265187481, 'male', 'Jawa Timur', '1212Abc']
    cal = HistoryPage(userdata)
