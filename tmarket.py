from tkinter import *
root = Tk()

def Get_db(event):
	from requests import request
	app = e1.get()
	t = request('GET', 'http://192.168.0.118/tmarket/' + app + ".py").text
	with open(app + '.py', 'w', encoding='utf-8') as f:
		f.write(t)

l1 = Label(text="Tmarket")
e1 = Entry()
b1 = Button(text="Download")

b1.bind("<Button-1>", Get_db)

l1.pack(expand=1)
e1.pack(padx=20)
b1.pack(expand=1)

root.mainloop()