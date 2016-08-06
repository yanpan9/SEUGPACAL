from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("SEU GPA CALCULATOR")
root.geometry()

def openfile():
	root.filename =  filedialog.askopenfilename(initialdir = "~/Study/python",title = "Select your file",filetypes = (("html files","*.html"),("all files","*.*")))	
def calculate():
	score=['Your Score:']
	try:
		with open(root.filename,'r') as file:
			for line in file.readlines():
				temp=re.findall('0%</span>"&gt;</span>(.*)&amp;nbsp',line)
				for x in temp:
					score.append(x)
	except:
		openfile()
	score.pop(0)
	score.pop()
	sum=0
	credit=0
	n=3
	while n<len(score):
		if score[n]!='补考' and score[n+1] =='' and score[n-1]!='通过':
			if score[n-1]=='及格':
				sum+=float(score[n-2])*1.5
				credit+=float(score[n-2])
			elif score[n-1]=='中':
				sum+=float(score[n-2])*2.5
				credit+=float(score[n-2])
			elif score[n-1]=='良':
				sum+=float(score[n-2])*3.5
				credit+=float(score[n-2])
			elif score[n-1]=='优':
				sum+=float(score[n-2])*4.5
				credit+=float(score[n-2])
			elif int(score[n-1])<60:
				credit+=float(score[n-2])
			elif int(score[n-1])>=60 and int(score[n-1])<63:
				sum+=float(score[n-2])*1.0
				credit+=float(score[n-2])
			elif int(score[n-1])>=63 and int(score[n-1])<66:
				sum+=float(score[n-2])*1.5
				credit+=float(score[n-2])
			elif int(score[n-1])>=66 and int(score[n-1])<70:
				sum+=float(score[n-2])*1.8
				credit+=float(score[n-2])
			elif int(score[n-1])>=70 and int(score[n-1])<73:
				sum+=float(score[n-2])*2.0
				credit+=float(score[n-2])
			elif int(score[n-1])>=73 and int(score[n-1])<76:
				sum+=float(score[n-2])*2.5
				credit+=float(score[n-2])
			elif int(score[n-1])>=76 and int(score[n-1])<80:
				sum+=float(score[n-2])*2.8
				credit+=float(score[n-2])
			elif int(score[n-1])>=80 and int(score[n-1])<83:
				sum+=float(score[n-2])*3.0
				credit+=float(score[n-2])
			elif int(score[n-1])>=63 and int(score[n-1])<86:
				sum+=float(score[n-2])*3.5
				credit+=float(score[n-2])
			elif int(score[n-1])>=86 and int(score[n-1])<90:
				sum+=float(score[n-2])*3.8
				credit+=float(score[n-2])
			elif int(score[n-1])>=90 and int(score[n-1])<93:
				sum+=float(score[n-2])*4.0
				credit+=float(score[n-2])
			elif int(score[n-1])>=93 and int(score[n-1])<96:
				sum+=float(score[n-2])*4.5
				credit+=float(score[n-2])
			elif int(score[n-1])>=96 and int(score[n-1])<=100:
				sum+=float(score[n-2])*4.8
				credit+=float(score[n-2])
		n+=5
	t.insert(1.0,"your GPA is:")
	t.insert('2.0',sum/credit)
	t.insert('3.0',"\n")
frame=Frame(root)
Button(frame, text="openfile", command = openfile).pack(side=LEFT)
Button(frame, text="calculate", command = calculate).pack(side=RIGHT)
frame.pack()
t = Text()
t.pack()
root.mainloop()
