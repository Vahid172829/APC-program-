# Import Tkinter Module
from tkinter import *
import sqlite3
import datetime
from PIL import ImageTk
from tkinter import ttk

conn=sqlite3.connect('FTMS.db')
crsr=conn.cursor()

crsr.execute("DELETE FROM QUOTATIONS WHERE B_ID = 'Buyer_1' AND CROP_ID = 2")

conn.commit()
conn.close()
