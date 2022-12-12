# Jika terdapat error babel.core.UnknownLocaleError: unknown locale 'en_ID'
# buka folder C:\Users\andro\anaconda33\Lib\site-packages\babel\locale-data
# duplicate en.bat dan rename menjadi en_ID.bat
# error ini maksudnya babel tidak menemukan locale en_ID

from tkinter import *
from tkinter.font import ITALIC
import login_page as lp

f = ('Times', 14)

rootapp = Tk()
rootapp.title('BookBall')
rootapp.geometry('1000x600')
rootapp.config(bg="orange red")
lp.LoginPage(rootapp)
rootapp.resizable(False, False)
rootapp.mainloop()
