from pyrecord import Record
from pyrecord import Records
from pycategory import Category
from datetime import*
import sys                               #class Record:
import tkinter
import tkinter.ttk as ttk
global category ,records
records=Records()
category=Category(records.l)


def add_record():
    try:
        ddate=date_str.get()
        ccategory=category_option.get().split()
        ddes=des_str.get()
        aamount=amount_str.get()
        y=ddate +' '+ ccategory[0][1::] +' '+ ddes +' '+ aamount
        s=y.split()

        if len(s)==4:
            if category.category_valid(s[1],category.category) == True:
                records.add(y)
            else:
                print('The specified category is not in category list.')
                print('You can check the category list by command "view categories".\nFail to add a record.')
                
        else:
            if category.category_valid(s[0],category.category) == True:
                records.add(y)
            else:
                print('The specified category is not in category list.')
                print('You can check the category list by command "view categories".\nFail to add a record.')

    except IndexError:
        print('The format of a record should be like:meal dinner -30.\nFail to add a record.')
    except ValueError:
        print('Invalid value for money.\nFail to add a record.')
    reset()



def delete_record():
    d=records_box.get(records_box.curselection())
    records.delete(d)
    reset()

def find_record():
    category_input=find_str.get()
    category.find_cate(category_input,category.category)
    records_box.delete(0,tkinter.END)

    for i,v in enumerate(category.ll):
        records_box.insert(i,'{:<15} {:<15} {:<12} {:<5}'.format(v[0],v[1],v[2],v[3]))
    b=0                     #b為計算紀錄的$$
    for i in category.ll:
        b=b+i[3]
    total=b               #total為全部有多少$$
    delete_label=tkinter.Label(frame, text='Now you have '+str(total) +' dollars',justify=tkinter.LEFT,font=('Consolas',20))
    delete_label.grid(row=9,column=0,columnspan=3,sticky=tkinter.W)


def reset():
    records_box.delete(0,tkinter.END)    
    for i,v in enumerate(records.l):
        records_box.insert(i,'{:<15} {:<15} {:<12} {:<5}'.format(v[0],v[1],v[2],v[3]))
    b=0                     #b為計算紀錄的$$
    for i in records.l:
        b=b+i[3]
    total=records.a+b               #total為全部有多少$$
    delete_label=tkinter.Label(frame, text='Now you have '+str(total) +' dollars',justify=tkinter.LEFT,font=('Consolas',20))
    delete_label.grid(row=9,column=0,columnspan=3,sticky=tkinter.W)
    des_entry.delete(0, 'end')
    amount_entry.delete(0, 'end')    
    category_option.set('')
    find_entry.delete(0, 'end')

def update():
    records.a=int(initial_str.get())
    reset()


root= tkinter.Tk()
frame = tkinter.Frame(root,borderwidth=10)
frame.grid(row=0,column=0)

find_label = tkinter.Label(frame, text='Find category',justify=tkinter.LEFT,font=('Consolas',20))
find_label.grid(row=0,column=0)
find_str=tkinter.StringVar()
find_entry=tkinter.Entry(frame,textvariable=find_str,font=('Consolas',20))
find_entry.grid(row=0,column=1)
find_but=tkinter.Button(frame,text='Find',font=('Consolas',20),command=find_record)
find_but.grid(row=0,column=2,sticky=tkinter.E)
re_but=tkinter.Button(frame,text='Reset',font=('Consolas',20),command=reset)
re_but.grid(row=0,column=3,sticky=tkinter.E)




initial_label=tkinter.Label(frame, text='Inital money',justify=tkinter.LEFT,font=('Consolas',20))
initial_label.grid(row=1,column=4,sticky=tkinter.E)
initial_str=tkinter.StringVar()
initial_str.set(records.a)
initial_entry=tkinter.Entry(frame,textvariable=initial_str,font=('Consolas',20),width=25)
initial_entry.grid(row=1,column=5)
initial_but=tkinter.Button(frame,text='Update',font=('Consolas',20),command=update)
initial_but.grid(row=2,column=5,sticky=tkinter.E)


space_label=tkinter.Label(frame, text='',justify=tkinter.LEFT,font=('Consolas',20))
space_label.grid(row=3,column=4,columnspan=2,sticky=tkinter.E)

date_label=tkinter.Label(frame, text='Date',justify=tkinter.LEFT,font=('Consolas',20))
date_label.grid(row=4,column=4,sticky=tkinter.E)
date_str=tkinter.StringVar()
date_str.set(str(date.today()))
date_entry=tkinter.Entry(frame,textvariable=date_str,font=('Consolas',20),width=25)
date_entry.grid(row=4,column=5)

root.option_add("*TCombobox*Listbox*Font",('Consolas',20))

category_label=tkinter.Label(frame, text='Category',justify=tkinter.LEFT,font=('Consolas',20))
category_label.grid(row=5,column=4,sticky=tkinter.E)

item=category.view(category.category)
item.reverse()
category_option=ttk.Combobox(frame,values=[i for i in item ],font=('Consolas',20),height=10,cursor='circle',width=25)
category_option.grid(row=5,column=5) 


des_label=tkinter.Label(frame, text='Description',justify=tkinter.LEFT,font=('Consolas',20))
des_label.grid(row=6,column=4,sticky=tkinter.E)
des_str=tkinter.StringVar()
des_entry=tkinter.Entry(frame,textvariable=des_str,font=('Consolas',20),width=25)
des_entry.grid(row=6,column=5)

amount_label=tkinter.Label(frame, text='Amount',justify=tkinter.LEFT,font=('Consolas',20))
amount_label.grid(row=7,column=4,sticky=tkinter.E)
amount_str=tkinter.StringVar()
amount_entry=tkinter.Entry(frame,textvariable=amount_str,font=('Consolas',20),width=25)
amount_entry.grid(row=7,column=5)

add_but=tkinter.Button(frame,text='Add a record',font=('Consolas',20),command=add_record)
add_but.grid(row=8,column=5,sticky=tkinter.E)


delete_but=tkinter.Button(frame,text='Delete',font=('Consolas',20),command=delete_record)
delete_but.grid(row=9,column=3,sticky=tkinter.E)




records_box=tkinter.Listbox(frame,font=('Consolas',20),width=50)
records_box.grid(row=1,column=0,columnspan=4,rowspan=8,sticky=tkinter.W)

for i,v in enumerate(records.l):
    records_box.insert(i,'{:<15} {:<15} {:<12} {:<5}'.format(v[0],v[1],v[2],v[3]))
b=0                     #b為計算紀錄的$$
for i in records.l:
    b=b+i[3]
total=records.a+b               #total為全部有多少$$
delete_label=tkinter.Label(frame, text='Now you have '+str(total) +' dollars',justify=tkinter.LEFT,font=('Consolas',20))
delete_label.grid(row=9,column=0,columnspan=3,sticky=tkinter.W)

root.mainloop()
records.exit()






