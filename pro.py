from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *

def f1():
	root.withdraw()
	adst.deiconify()
def f2():
	adst.withdraw()
	root.deiconify()
def f3():
	stViewData.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con=None
	try:
		con=connect("system/abc12345")
		cursor=con.cursor()
		sql="select rno,name,marks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+"rno = "+ str(d[0]) + "name =" + str(d[1]) +"marks="+str(d[2])  +"\n"
		stViewData.insert(INSERT,msg)
	except DatabaseError as e:
		messagebox.showerror("galat kiya",e)
	finally:
		if con is not None:
			con.close()
def f4():
	vist.withdraw()
	root.deiconify()

def f5():
	name=entAddName.get()
	if (len(name) < 2 or not name.isalpha()):
		messagebox.showerror("WRONG","INVALID NAME")
		entAddName.delete(0,END)
		entAddName.focus()
		return
	rno=int(entAddRno.get())
	if (rno<0):
		messagebox.showerror("WRONG","INVALID ROLLNO")
		entAddRno.delete(0,END)
		entAddRno.focus()
		return
	marks=int(entAddMarks.get())
	if((marks>100) or (marks<0)):
		messagebox.showerror("WRONG","INVALID marks")
		entAddMarks.delete(0,END)
		entAddMarks.focus()
		return
		

	con=None	
	try:
		con=connect("system/abc12345")
		rno=int(entAddRno.get())
		name=entAddName.get()
		marks=int(entAddMarks.get())
		args=(rno,name,marks)

		cursor=con.cursor()
		sql="insert into students values('%d','%s','%d')"
		
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("sahi kiya ",str(cursor.rowcount)+"rows inserted")
		
	except DatabaseError as e:
		messagebox.showerror("galat kiya",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddMarks.delete(0,END)

def f9():
	win.withdraw()
	root.deiconify()
def f100():
	root.withdraw()
	win.deiconify()

def f6():
	con=None
	
	#r=int(entUpdateRno.get())
	#name=entUpdateName.get()
	#marks=int(entUpdateMarks.get())
	name=entUpdateName.get()
	if (len(name) < 2 or not name.isalpha()):
		messagebox.showerror("WRONG","INVALID NAME")
		entUpdateName.delete(0,END)
		entUpdateName.focus()
		return
	r=int(entUpdateRno.get())
	if (r<0):
		messagebox.showerror("WRONG","INVALID ROLLNO")
		entUpdateRno.delete(0,END)
		entUpdateRno.focus()
		return
	marks=int(entUpdateMarks.get())
	if((marks>100) or (marks<0)):
		messagebox.showerror("WRONG","INVALID marks")
		entUpdateMarks.delete(0,END)
		entUpdateMarks.focus()
		return

	try:
		#root.withdraw()
		#win.deiconify()
		con=connect("system/abc12345")
		
		#name=entUpdateName.get()
		#marks=int(entUpdateMarks.get())
		#args=(r,name,marks)
		
		cursor=con.cursor()
		sql=("update students set marks='%d' where rno='%d'")
		args=(marks,r)
		cursor.execute(sql%args)
		con.commit()
		messagebox.showinfo("update kiya ",str(cursor.rowcount)+"rows updated")
		
	except DatabaseError as e:
		messagebox.showerror("galat kiya",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entUpdateRno.delete(0,END)
		entUpdateName.delete(0,END)
		entUpdateMarks.delete(0,END)



def f7():
	root.withdraw()
	paw.deiconify()


def f10():
	ro=int(entRno.get())
	con=None
	
	if (ro<0):
		messagebox.showerror("WRONG","INVALID ROLLNO")
		entRno.delete(0,END)
		return
	
	try:
		con=connect("system/abc12345")
		cursor=con.cursor()
		sql="Delete from students where rno='%d'"
		args=ro
		cursor.execute(sql % args)
		con.commit()
		#print(cursor.rowcount,"rows delted")
		messagebox.showinfo("delete kiya ",str(cursor.rowcount)+"rows deleted")
	except DatabaseError as e:
		messagebox.showerror("galat kiya",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entRno.delete(0,END)
def f11():
	paw.withdraw()
	root.deiconify()

def retrieve_input():
	import bs4
	import requests
	res=requests.get("http://www.brainyquote.com/quotes_of_the_day.html")
	#print(res)
	soup=bs4.BeautifulSoup(res.text,'lxml')
	quote=soup.find('img',{"class":"p-qotd"})
	#print(quote)
	msg=quote['alt']
	return msg
	#print("message of day the day",msg)
	'''photo_url="https://www.brainyquote.com/" +quote['data-img-url']
	res=requests.get(photo_url)
	import datetime
	date=datetime.datetime.now().date()
	file_name=str(date)+".jpeg"
	with open(file_name,"wb") as f:
		f.write(res.content)'''


		
def f35():
	import socket
	import requests
	socket.create_connection( ("www.google.com",80))
	#print("u are connected")
	#city=input("enter the  location name") 
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2= "&q=" + "mumbai"
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address=a1+a2+a3
	res1=requests.get(api_address)
	#print(res1)
	data=res1.json()
	
	main=data['main']
		
	temp=main['temp']
	return temp
		

def f67():
	import csv
	import matplotlib.pyplot as plt
	import pandas as pd
	import cx_Oracle
	 #con = cx_Oracle.connect('username/password@[ipaddress or hostname]/SID')
	 #for example con = cx_Oracle.connect('scott/tiger@127.0.0.1/orcl')
	con = cx_Oracle.connect("system/abc12345")
	cur = con.cursor()
	cur.execute('select marks,name from students order by marks')
	bb = open("bb.csv", "w")
	writer = csv.writer(bb)
	writer.writerow(["MARKS","NAMES"])
	for row in cur:
    		bb.write(str(row[0])+ ',' + row[1] + '\n')
	bb.close()
	cur.close()
	con.close()
	#print("File successfully exported")	
	import pandas as pd
	import cx_Oracle
	
	'''con = cx_Oracle.connect("system/abc12345")
	cursor = con.cursor()
	cursor.execute('select marks,name from students')
	rows=cursor.fetchall()
	print(rows)'''
	




	data=pd.read_csv("bb.csv")
	marks=data['MARKS'].tolist()
	names=data['NAMES'].tolist()
	#print(marks)
	marks.sort(reverse=True)
	high=marks[0]
	medium=marks[1]
	low=marks[2]
	pp=names[-1]
	cc=names[-2]
	ff=names[-3]	
	pc=[high,medium,low]
	games=[pp,cc,ff]	
	'''for i in zip(pc,rows):
		games.append[i]'''
	#print(games)
	#xy=["highest","low","lowest"]
	plt.bar(games,pc,width=0.30,label='STUDENTS')
	plt.title("top 3")
	#plt.xticks(x,xy)
	plt.xlabel("NAMES")
	plt.ylabel("MARKS")
	plt.legend()
	plt.grid()
	plt.show()

'''cc= open("cc.csv", "a")
	for row in cur:
		cc.write(str(row[0]) +  '\n')
	cc.close()
	cur.close()
	con.close()
	print("File successfully exported")
	data=pd.read_csv("cc.csv")
	marks=data['A'].tolist()
	print(marks)'''

	



root=Tk()
root.title(" S M s ")
root.geometry("500x400+200+200")

btnAdd=Button(root,text="Add",font=("arial",18,'bold'),width=10,command=f1)
btnView=Button(root,text="View",font=("arial",18,'bold'),width=10,command=f3)
btnUpdate=Button(root,text="update",font=("arial",18,'bold'),width=10,command=f100)
btnDelete=Button(root,text="delete",font=("arial",18,'bold'),width=10,command=f7)
btnGraph=Button(root,text="graph",font=("arial",18,'bold'),width=10,command=f67)
T = Text(root, height=2, width=30)
F= Text(root, height=2, width=30)
T.insert(CURRENT,  retrieve_input())
F.insert(CURRENT,"mumbai")
F.insert(END,f35())

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
T.pack(pady=10)   
F.pack(pady=10)
adst=Toplevel(root)
adst.title("Add st.")
adst.geometry("500x400+200+200")
adst.withdraw()
lblAddRno=Label(adst,text="enter rmo ",font=("arial",18,'bold'))
entAddRno=Entry(adst,bd=10,font=("arial",18,'bold'))
lblAddName=Label(adst,text="enter name ",font=("arial",18,'bold'))
entAddName=Entry(adst,bd=10,font=("arial",18,'bold'))
lblAddMarks=Label(adst,text="enter marks ",font=("arial",18,'bold'))
entAddMarks=Entry(adst,bd=10,font=("arial",18,'bold'))
btnAddSave=Button(adst,text="Save",font=("arial",18,'bold'),width=10,command=f5)
btnAddBack=Button(adst,text="Back",font=("arial",18,'bold'),width=10,command=f2)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

vist=Toplevel(root)
vist.title("View st ")
vist.geometry("500x400+200+200")
vist.withdraw()
stViewData=scrolledtext.ScrolledText(vist,width=30,height=10)
btnViewBack=Button(vist,text="Back",font=("arial",18,'bold'),command=f4)
stViewData.pack(pady=10)
btnViewBack.pack(pady=10)

win=Toplevel(root)
win.title("update st.")
win.geometry("500x400+200+200")
win.withdraw()
lblUpdateRno=Label(win,text="enter rno ",font=("arial",18,'bold'))
entUpdateRno=Entry(win,bd=10,font=("arial",18,'bold'))
lblUpdateName=Label(win,text="enter name ",font=("arial",18,'bold'))
entUpdateName=Entry(win,bd=10,font=("arial",18,'bold'))
lblUpdateMarks=Label(win,text="enter marks ",font=("arial",18,'bold'))
entUpdateMarks=Entry(win,bd=10,font=("arial",18,'bold'))
btnUpdateAdd=Button(win,text="Update",font=("arial",18,'bold'),width=10,command=f6)
btnUpdateBack=Button(win,text="Back",font=("arial",18,'bold'),width=10,command=f9)
lblUpdateRno.pack(pady=10)
entUpdateRno.pack(pady=10)
lblUpdateName.pack(pady=10)
entUpdateName.pack(pady=10)
lblUpdateMarks.pack(pady=10)
entUpdateMarks.pack(pady=10)
btnUpdateAdd.pack(pady=10)
btnUpdateBack.pack(pady=10)


paw=Toplevel(root)
paw.title("delete st.")
paw.geometry("500x400+200+200")
paw.withdraw()
lblRno=Label(paw,text="enter rno ",font=("arial",18,'bold'))
entRno=Entry(paw,bd=10,font=("arial",18,'bold'))
btnSave=Button(paw,text="Save",font=("arial",18,'bold'),width=10,command=f10)
btnBack=Button(paw,text="Back",font=("arial",18,'bold'),width=10,command=f11)
lblRno.pack(pady=10)
entRno.pack(pady=10)
btnSave.pack(pady=10)
btnBack.pack(pady=10)




root.mainloop()




'''str="update voter set name='%s' where eno='%d'"
args=(name,eno)
try:
        c.execute(str % args)
        conn.commit()'''
