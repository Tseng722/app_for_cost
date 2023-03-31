from datetime import*
import sys
import tkinter

global category ,records
class Record:
    """No longer used"""
    def __init__(self,category,des,amount,today=date.today()):

        self._date=today
        self._category=category
        self._des=des
        self._amount=amount


    @property
    def amount(self):
        return int(self._amount)

    @property
    def date(self):
        if type(self._date) != str:
            self._date=str(self._date)
        date.fromisoformat(self._date)
        return self._date


class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        try:
            fh=open('records.txt','r')                          #fh為read mode 的handle
            error_root10=tkinter.Tk()
            eframe10 = tkinter.Frame(error_root10,borderwidth=10)
            eframe10.grid(row=0,column=0)
            error_label10 = tkinter.Label(eframe10, text="welcome back!",justify=tkinter.LEFT,font=('Consolas',20))
            error_label10.grid(row=0,column=0)
            error_but10=tkinter.Button(eframe10,text='OK',font=('Consolas',20),command=error_root10.destroy)
            error_but10.grid(row=1,column=0)
            error_root10.mainloop()
            fh.seek(0)                                          #一切從頭開始
            l=[]                                                #l為暫存record的變數
            w=''                                                #w為了讀檔案的暫存變數
            ss=fh.readlines()
            for i in ss[1::]:                                   #ss[0]為最一開始的$$
                w=''
                for string in i:
                    if not string in set([')','(','\n',"'",',']) :
                        w=w+string
                s=w.split()
                record=Record(s[1],s[2],s[3],s[0])
                e=(record.date,record._category,record._des,record.amount)
                l.extend([e])
            a=int(ss[0])                                        #a為integer的最一開始$$
        except FileNotFoundError as err:
            error_root=tkinter.Tk()
            eframe = tkinter.Frame(error_root,borderwidth=10)
            eframe.grid(row=0,column=0)
            error_label = tkinter.Label(eframe, text='There does no file exist',justify=tkinter.LEFT,font=('Consolas',20))
            error_label.grid(row=0,column=0)
            error_but=tkinter.Button(eframe,text='OK',font=('Consolas',20),command=error_root.destroy)
            error_but.grid(row=1,column=0)
            error_root.mainloop()
            #print('There does no file exist')
            x=str(0)
            with open('records.txt','w') as wh:                 #wh為write mode 的handle
                wh.write(x)
                wh.write('\n')
            try:
                a=int(x)
            except ValueError:
                print('Invalid value for momey.Set to 0 by default.')
                a=int(0)
            l=[]
        except IndexError:
            error_root1=tkinter.Tk()
            eframe1 = tkinter.Frame(error_root1,borderwidth=10)
            eframe1.grid(row=0,column=0)
            error_label1 = tkinter.Label(eframe1, text="There's no record in file.",justify=tkinter.LEFT,font=('Consolas',20))
            error_label1.grid(row=0,column=0)
            error_but1=tkinter.Button(eframe1,text='OK',font=('Consolas',20),command=error_root1.destroy)
            error_but1.grid(row=1,column=0)
            error_root1.mainloop()

            print("There's no record in file.")
            x=str(0)
            with open('records.txt','w') as wh:
                wh.write(x)
                wh.write('\n')
            a=int(x)
            l=[]

        except ValueError:
            error_root2=tkinter.Tk()
            eframe2 = tkinter.Frame(error_root2,borderwidth=10)
            eframe2.grid(row=0,column=0)
            error_label2 = tkinter.Label(eframe2, text="Invalid value for money in record.",justify=tkinter.LEFT,font=('Consolas',20))
            error_label2.grid(row=0,column=0)
            error_but2=tkinter.Button(eframe2,text='OK',font=('Consolas',20),command=error_root2.destroy)
            error_but2.grid(row=1,column=0)
            error_root2.mainloop()

            print('Invalid value for money in record.')
            x=str(0)
            with open('records.txt','w') as wh:
                wh.write(x)
                wh.write('\n')
            a=int(x)
            l=[]
        self.l=l
        self.a=a
    def add(self,y):                 #y為花費紀錄
        """add records description amount"""
        s=y.split()
        try:
            if len(s)==4:
                record=Record(s[1],s[2],s[3],s[0])
            else:
                record=Record(s[0],s[1],s[2])
            e=(record.date,record._category,record._des,record.amount)
            self.l.extend([e])
            b=0                     #b為計算紀錄的$$
            for i in self.l:
                b=b+i[3]
            total=self.a+b               #total為全部有多少$$
            #print('Now you have %d dollars ' %(total))
            #if total <0:
               # error_root=tkinter.Tk()
               # eframe = tkinter.Frame(error_root,borderwidth=10)
               # eframe.grid(row=0,column=0)
               # error_label = tkinter.Label(eframe, text='You have spent all money.So poor QQ',justify=tkinter.LEFT,font=('Arial',20))
               # error_label.grid(row=0,column=0)
               # error_but=tkinter.Button(eframe,text='OK',font=('Arial',20),command=error_root.destroy)
               # error_but.grid(row=1,column=0)
               # error_root.mainloop()

        except ValueError:
            error_root3=tkinter.Toplevel()
            eframe3 = tkinter.Frame(error_root3,borderwidth=10)
            eframe3.grid(row=0,column=0)
            error_label3 = tkinter.Label(eframe3, text='The format of date should be YYYY-MM-DD.',justify=tkinter.LEFT,font=('Consolas',20))
            error_label3.grid(row=0,column=0)
            error_label13 = tkinter.Label(eframe3, text='Fail to add a record.',justify=tkinter.LEFT,font=('Consolas',20))
            error_label13.grid(row=1,column=0)
            error_but3=tkinter.Button(eframe3,text='OK',font=('Consolas',20),command=error_root3.destroy)
            error_but3.grid(row=2,column=0)
            #error_root3.mainloop()
    def view(self):
        """view all record"""
        try:
            print("Here's your expense and income records:")
            print('   Date     Category  Description    Amount')
            print('__________  ________  ___________    ______')
            b=0
            for i in self.l:
                print('%5s %8s %10s %12d' %(i[0],i[1],i[2],i[3]))
                b=b+i[3]
            total=self.a+b
            print('___________________________________________')
            print('Now you have %d dollars ' %(total))
            if total <0:
                print('You have spent all money.So poor QQ')
        except TypeError:
            print('Try again!')
    def delete(self,d):
        """delete specificed record"""
        if self.l==[]:
            print('The record is empty.Please add some records.')
        else:
            try:
                dd=d.split()
                dd[3]=int(dd[3])
                #record=Record(d)
                if tuple(dd) in self.l:
                    self.l.pop(self.l.index(tuple(dd)))
                else:
                    print(f'There is no record with "{d}".Fail to delete a record.')
            except IndexError:
                print('Invalid format.\nFail to delete a record.')
            except ValueError:
                print('Invalid value for money.\nFail to delete a record.')
    def exit(self):
        """save and exit"""
        with open('records.txt','w') as wh:             #儲存記錄到records.txt
            wh.write(str(self.a))
            wh.write('\n')
            for i in self.l:
                wh.writelines([str(i)])
                wh.write('\n')

