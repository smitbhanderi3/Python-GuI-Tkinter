from tkinter import *
from tkinter import messagebox
from tkinter import *
import tkinter

calculator=Tk()
calculator.title("Calculator")

# Output Frame ----------------------
calculator.geometry("459x304+460+40")
calculator.resizable(width=False, height=False)
coverframe = Frame(calculator, bd=20, pady=2, relief=RIDGE)
coverframe.grid()


# Click btn ---------------------
def click(number):
    display.insert(tkinter.END, number)

# Insert . 
    
    
# Click operators--------------------

def operator(number):
    get_value=display.get()
    if get_value[0]=='+' or get_value[0]=='-' or get_value[0]=='×' or get_value[0]=='÷' :
        display.delete(0)

    if get_value.endswith('+') or get_value.endswith('-') or get_value.endswith('÷') or get_value.endswith('×'):
        display.delete(len(get_value)-1,tkinter.END)
        display.insert(tkinter.END, number)
    else:
          display.insert(tkinter.END, number )

# Replacing------------------------
def ans():
    replacing = display.get()
    replacing = replacing.replace('×','*')
    replacing = replacing.replace('÷','/')
    final_str = eval(replacing)
    display.delete(0, tkinter.END)
    display.insert(tkinter.END, final_str )

# clearing Last index value------------------------

def clear(number):
    clearing=display.get()
    display.delete(len(clearing)-1,tkinter.END)

# deleteting whole value ------------------------
def deleting(number):
    deleting=display.get()
    display.delete(0,tkinter.END)

# Removing signs from index[0]--------------------
def removing_sign(number):
    rsign=display.get()
    if rsign.startswith('-') or rsign.startswith('+') or rsign.startswith('÷') or rsign.startswith('×') : display.delete(0,1)
    else: display.insert(0,'-')


def def_float():
    rsign=display.get()
    try:
        d_i = rsign.rfind('.')
        for i in '+-÷×':
            o_i = rsign.rfind(i)
            if o_i == d_i == -1:
                display.insert(tkinter.END, '.')
                break
            if o_i == -1:
                continue
            if o_i != -1:
                if d_i < o_i:
                    if o_i != len(rsign)-1:
                        display.insert(tkinter.END, '.')
                        break
                    else:
                        break
            else:
                if d_i == -1:
                    display.insert(tkinter.END, '.')
                    break
                else:
                    break



    except:
        display.insert(tkinter.END, rsign )



# First Row------------------------
# 7
b7= Button(calculator, text="7", font=('Aerialbold') ,bg="#403434", fg="#c2baba", width=7, height=2, command=lambda : click(7))
b7.place(x=2,y=43)

# 8
b8= Button(calculator, text="8", font=('Aerialbold'),bg="#403434", fg="#c2baba", width=7, height=2, command=lambda : click(8))
b8.place(x=91,y=43)

# 9
b9= Button(calculator, text="9", font=('Aerialbold'),bg="#403434", fg="#c2baba", width=7, height=2, command=lambda : click(9))
b9.place(x=180,y=43)

# ×
b_multi= Button(calculator, text="×", font=('Aerialbold'),bg="#FF6600", fg="#c2baba", width=7, height=2, command=lambda : operator('×'))
b_multi.place(x=269,y=43)

# 🢀
b_clear=Button(calculator, text="🢀", font=('Aerialbold'),bg="#6b5757", fg="#c2baba", width=8, height=2, command=lambda : clear('🢀'))
b_clear.place(x=358,y=43)

# Second Row------------------------
# 4
b4= Button(calculator, text="4", font=('Aerialbold'), bg="#403434", fg="#c2baba", width=7, height=2, command=lambda : click(4))
b4.place(x=2,y=108)

# 5
b5= Button(calculator, text="5", font=('Aerialbold'), bg="#403434",fg="#c2baba", width=7, height=2, command=lambda : click(5))
b5.place(x=91,y=108)

# 6
b6= Button(calculator, text="6", font=('Aerialbold'), bg="#403434", fg="#c2baba", width=7, height=2, command=lambda : click(6))
b6.place(x=180,y=108)

# -
b_subt= Button(calculator, text="-", font=('Aerial,bold'), bg="#FF6600", fg="#c2baba", width=7, height=2, command=lambda : operator('-'))
b_subt.place(x=269,y=108)

# ␡
b_del= Button(calculator, text="AC", font=('Aerial,bold'), bg="#6b5757", fg="#c2baba", width=8, height=2, command=lambda : deleting('␡'))
b_del.place(x=358,y=108)

# Last row ------------------

b1= Button(calculator, text="1", font=('Aerialbold'), bg="#403434", fg="#c2baba", width=7, height=2, command=lambda : click(1))
b1.place(x=2,y=173)

# 2
b2= Button(calculator, text="2", font=('Aerialbold'), bg="#403434", fg="#c2baba", width=7, height=2, command=lambda : click(2))
b2.place(x=91,y=173)

# 3
b3= Button(calculator, text="3", font=('Aerialbold'), bg="#403434", fg="#c2baba", width=7, height=2, command=lambda : click(2))
b3.place(x=180,y=173)

# +
b_add= Button(calculator, text="+", font=('Aerialbold'), bg="#FF6600", fg="#c2baba", width=7, height=2,command=lambda : operator('+'))
b_add.place(x=269,y=173)

# Fourth row--------------------------
# ÷
b_div= Button(calculator, text="÷", font=('Aerialbold'), bg="#FF6600", fg="#c2baba", width=7, height=2, command=lambda : operator('÷'))
b_div.place(x=2,y=238)

# 0
b0= Button(calculator, text="0", font=('Aerialbold'), bg="#403434", fg="#c2baba", width=7, height=2, command=lambda : click(0))
b0.place(x=91,y=238)

# .
b_float= Button(calculator, text=".", font=('Aerialbold'), bg="#6b5757", fg="#c2baba", width=7, height=2, command=lambda : def_float()) 
b_float.place(x=180,y=238)

# =
b_equal= Button(calculator, text="=", font=('Aerialbold'), bg="#FF6600", fg="#c2baba", width=7, height=2, command= lambda : ans())
b_equal.place(x=269,y=238)


# Display--------------------------------

display= Entry(calculator, font = ('Aerialbold',25), bg="#c2baba", fg="#403434", width=25, justify='right')
display.place(x=3)


calculator.mainloop()

