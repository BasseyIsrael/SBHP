import tkinter as tm
from tkinter import ttk
from ttkthemes import themed_tk as tk


window = tk.ThemedTk()
window.get_themes()
window.set_theme("plastik")

window.iconbitmap('pyc.ico')

window.geometry("390x350")
window.title("i-SIBHP 2019")

menu=tm.Menu(window)
window.config(menu=menu)


def exit1():
	exit()

subm1=tm.Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit")

subm2=tm.Menu(menu)
menu.add_cascade(label="View", menu=subm2)
subm2.add_command(label="Exit")
subm2=tm.Menu(menu)
menu.add_cascade(label="About", menu=subm2)
subm2.add_command(label="About the developer")
subm2.add_command(label="Exit")

global fn
fn=tm.StringVar()

#label1 = tm.Label(window,text="i-SIBHP",font=("Colonna MT",19,"bold")).pack()
label2 = tm.Label(window,text="Welcome to SIBHP calculation module.",font=("Bradley Hand ITC",12, "bold")).place(x=50,y=20)
label3 = tm.Label(window,text="Please input your name:", font=("Trebuchet MS",12)).place(x=100,y=75)
label4 = tm.Label(window,text="Method:",font=("Trebuchet MS",12)).place(x=50,y=200)



entry1 = ttk.Entry(window,textvar=fn).place(x=130,y=135)

def secondwin():
	windo = tk.ThemedTk()

	windo.get_themes()
	windo.set_theme("plastik")

	windo.iconbitmap('pyc.ico')

	windo.geometry("700x600")
	windo.title("i-SIBHP 2019")

	menu = tm.Menu(windo)
	windo.config(menu=menu)
	separator = ttk.Separator(windo, orient=tm.HORIZONTAL).pack()

	whpres1 = tm.IntVar()
	whtemp1 = tm.IntVar()
	tgrad1 = tm.DoubleVar()
	pgrad1 = tm.IntVar()
	sgr1 = tm.DoubleVar()
	gwr1 = tm.IntVar()
	depth1 = tm.IntVar()

	def exit1():
		exit()
	def calculate():
		import math
		import itertools
		#print("Good day")
		#name = input("Please enter your name: ")
		#print("Welcome ", name)
		#global whtemp
		# data at the surface
		global whtemp
		whtemp = whtemp1.get()
		#whtemp = eval(input("Please input your wellhead temperature (degR): "))
		# htemp = 534
		global whpres
		whpres = whpres1.get()
		#whpres = eval(input("Please input your wellhead pressure (psia): "))
		# whpres = 2300
		iniwhpres = whpres
		global tgrad
		tgrad=tgrad1.get()
		#tgrad = eval(input("Please input your temperature gradient data (degR/500ft): "))
		# tgrad = 1.9
		global depth
		depth = depth1.get()
		#depth = eval(input("Please input your well depth: "))
		# depth = 9000
		step = depth / 500
		global sgi
		# sgi = eval(input("Please input your measured gas gravity: "))
		sgi = 0.7
		# gwr = eval(input("Please input your measured gas-water ratio: "))
		gwr = gwr1.get()
		global tpci
		tpci = float(168 + 325 * sgi - 125 * sgi ** 2)
		global ppci
		ppci = float(677 + 15 * sgi - 37.5 * sgi ** 2)
		print("gas gravity is: ", sgi)
		print("Critical temperature = ", tpci)
		print("Critical pressure= ", ppci)
		p = whpres
		t = whtemp
		intnews = []

		def first():
			global ppri
			ppri = whpres / ppci
			global tpri
			tpri = whtemp / tpci

			# print("Your Pseudo-Reduced pressure is: ", ppri,  "and Pseudo-Reduced temperature is: ", tpri)
			# newtemp = whtemp + tgrad
			# print("new temperature = ", newtemp)
			# tpci = float(168+325*sgi-125*sgi**2)
			# ppci = float(677+15*sgi-37.5*sgi**2)
			# print("gas gravity is: ", sgi)
			# print("Critical temperature = ", tpci)
			# print("Critical pressure= ", ppci)
			# ppri = whpres/ppci
			# tpri = whtemp/tpci
			# print("Your Pseudo-Reduced pressure is: ", ppri,  "and Pseudo-Reduced temperature is: ", tpri)
			# print("Find compressibility factor")
			def z_factor():
				pres = p
				global temp
				temp = t
				global sg
				sg = sgi

				tpc = 168 + (325 * sg) - (125 * (sg ** 2))
				ppc = 677 + (15 * sg) - (37.5 * (sg ** 2))
				ppr = pres / ppc
				tpr = temp / tpc
				print(tpr)
				print(temp)
				print(pres)
				densir = (0.27 * ppr) / tpr
				a1 = 0.3265
				a2 = -1.07
				a3 = -0.5339
				a4 = 0.01569
				a5 = -0.05165
				a6 = 0.5475
				a7 = -0.7361
				a8 = 0.1844
				a9 = 0.1056
				a10 = 0.6134
				a11 = 0.7210
				r1 = a1 + (a2 / tpr) + (a3 / (tpr ** 3)) + (a4 / (tpr ** 4)) + (a5 / (tpr ** 5))
				# print(r1)
				r2 = (0.27 * ppr) / tpr
				# print(r2)
				r3 = a6 + (a7 / tpr) + (a8 / (tpr ** 2))
				# print(r3)
				r4 = a9 * ((a7 / tpr) + (a8 / tpr ** 2))
				# print(r4)
				r5 = a10 / tpr ** 3
				# print(r5)
				densir = (0.27 * ppr) / (tpr)
				tim = math.exp(-a11 * (densir ** 2))

				# print(tim)
				def factor():
					fpr = 1 + (r1 * densir) - (r2 / densir) + (r3 * (densir ** 2)) - (r4 * (densir ** 5)) + (
								r5 * (1 + (a11 * (densir ** 2)))) * tim
					# print("The function= ", fpr)

					fprime = r1 + (r2 / densir ** 2) + (2 * r3 * densir) - (5 * r4 * (densir ** 4)) + (
								2 * r5 * densir) * math.exp((-a11 * densir ** 2) * (
								(1 + 2 * a11 * (densir ** 3)) - (a11 * (densir ** 2)) * (1 + a11 * (densir ** 2))))
					# print("The derivative= ", fprime)
					global hfac
					hfac = fpr / fprime
					# print("h= ", abs(hfac))
					global densir1
					densir1 = densir - hfac

				# print("The new reduced density = ", densir1)

				factor()
				while abs(hfac) >= 0.0000000000001:
					densir = densir1
					factor()
					continue
				global zfactor
				zfactor = (0.27 * ppr) / (densir1 * tpr)

			# print("Final compressibility= ", zfactor)
			z_factor()
			# zfactor = eval(input("Please enter your compressiblity factor read from the chart: "))
			int = ((zfactor * whtemp) / whpres) + (199.33 / gwr)
			# print("Integral= ",int )
			int1 = int
			deltap = (((sgi / 53.34) + (86.26 / gwr)) * (depth / (step * (int + int1))))
			# print("First change in pressure = ", deltap)
			# global whpres
			global nwhpres
			nwhpres = whpres + deltap
			global nwhtemp
			nwhtemp = whtemp + tgrad

			# print("Your new Pseudo-Reduced pressure is: ", ppri,  "and new Pseudo-Reduced temperature is: ", tpri)
			def pressure():
				p = nwhpres
				t = nwhtemp
				z_factor()
				# ppri = nwhpres / ppci
				# tpri = nwhtemp / tpci
				# print("Your new Pseudo-Reduced pressure is: ", ppri, "and new Pseudo-Reduced temperature is: ", tpri)
				# global zfactor
				zfactornew = zfactor
				# print("z factor= ", zfactornew)
				# print("Find new compressibility factor from the chart")
				# zfactornew = eval(input("Please enter your new compressiblity factor read from the chart: "))
				global intnew
				intnew = ((zfactornew * nwhtemp) / nwhpres) + (199.33 / gwr)
				# print("New Integral= ",intnew)
				deltap = (((sgi / 53.34) + (86.26 / gwr)) * (depth / (step * (int + intnew))))
				# print("Change in pressure=", deltap)
				global nnwhpres
				nnwhpres = deltap + whpres
				#  print("The new presure= ", nnwhpres)
				global err
				err = nnwhpres - nwhpres

			#    print("Error = ", err)
			pressure()
			while err >= 0.001:
				nwhpres = nnwhpres
				int = intnew
				pressure()
				continue
			# print("convergence reached")
			#  print("The pressure = ", nnwhpres)
			#    print("The final integral = ", intnew)
			intnews.append(intnew)
			return locals()

		first()

		for i in range(0, int(depth), 500):
			whpres = nnwhpres
			whtemp = nwhtemp + tgrad
			# intnews.append(intnew)
			first()
		# print("Final Pressure = ", nnwhpres)
		print("The Calculated integrals are: ", intnews)
		# for i in intnews:
		even_ints = list(itertools.islice(intnews, 1, len(intnews) - 1, 2))
		# print(even_ints)
		odd_ints = list(itertools.islice(intnews, 2, len(intnews) - 2, 2))
		# print(odd_ints)
		ini_i = intnews[1]
		final_i = intnews[-1]
		my = sum(even_ints)
		yu = sum(odd_ints)
		# other = (1*step*((0.05624*sgi*gwr)+258.766))/(ini_i+(4*my)+(2*yu)+final_i)
		other = ((depth * step) * ((0.05624 * sgi * gwr) + 258.780)) / (gwr * (ini_i + (4 * my) + (2 * yu) + final_i))
		# print(other)
		p_final = other
		print("The final pressure and SIBHP= ", p_final)

	# print  (2300+(112.5*0.6*5790)/(178+(4*191)+203))

	# def z_factor():
	#   wb = openpyxl.load_workbook("Hall-Yarborough-Z.xlsm")
	# z_factor()
	subm1 = tm.Menu(menu)
	menu.add_cascade(label="File", menu=subm1)
	subm1.add_command(label="Exit")

	subm2 = tm.Menu(menu)
	menu.add_cascade(label="View", menu=subm2)
	subm2.add_command(label="Exit")
	subm2 = tm.Menu(menu)
	menu.add_cascade(label="About", menu=subm2)
	subm2.add_command(label="About the developer")
	subm2.add_command(label="Exit")
	#windo = tm.Frame(root).place(relwidth=1, relheight=1)
	label1 = tm.Label(windo, text="Hi There " + fn.get(), font=("Bradley Hand ITC", 13, "bold")).pack()

	separ = tm.Frame(windo, bd=2, relief="ridge").place(relx=0.01, rely=0.09, relwidth=0.48, relheight=0.40)
	separ1 = tm.Frame(windo, bd=2, relief="ridge").place(relx=0.49, rely=0.09, relwidth=0.5, relheight=0.44)
	label2 = tm.Label(windo, text="Well Parameters", relief="flat", font=("Bradley Hand ITC", 12, "bold")).place(
		x=10, y=40)
	label3 = tm.Label(windo, text="Wellhead Pressure(psi):", font=("Trebuchet MS", 9)).place(x=10, y=75)
	label13 = tm.Label(windo, text="Wellhead Temperature(degR):", font=("Trebuchet MS", 9)).place(x=10, y=105)
	label4 = tm.Label(windo, text="Temperature Gradient(degR/100ft):", font=("Trebuchet MS", 9)).place(x=10, y=135)
	label5 = tm.Label(windo, text="Pressure Gradient(psi/100ft):", font=("Trebuchet MS", 9)).place(x=10, y=165)
	label12 = tm.Label(windo, text="Measured gas specific gravity(-):", font=("Trebuchet MS", 9)).place(x=10, y=195)
	label6 = tm.Label(windo, text="Produced Gas-Oil ratio(scf/stb):", font=("Trebuchet MS", 9)).place(x=10, y=225)
	label15 = tm.Label(windo, text="Well depth:", font=("Trebuchet MS", 9)).place(x=10, y=255)
	separ2 = tm.Frame(windo, bd=2, relief="ridge").place(relx=0.01, rely=0.55, relwidth=0.48, relheight=0.36)
	label7 = tm.Label(windo, text="Initial Parameters", relief="groove", bg="grey",
	                  font=("Bradley Hand ITC", 12, "bold")).place(x=10, y=310)
	# separ2 = tm.Frame(window, bd = 2, relief = "ridge").place(relx = 0.01, rely = 0.5, relwidth = 0.48, relheight = 0.40)
	label8 = tm.Label(windo, text="Iterables (Results)", relief="flat", font=("Bradley Hand ITC", 12, "bold")).place(x=400, y=40)
	label9 = tm.Label(windo, text="Integral values:", font=("Trebuchet MS", 9)).place(x=400, y=75)
	label0 = tm.Label(windo, text="Gas Gravity values", font=("Trebuchet MS", 9)).place(x=400, y=150)
	label11 = tm.Label(windo, text="Pressures (psi):", font=("Trebuchet MS", 9)).place(x=400, y=225)
	separ3 = tm.Frame(windo, bd=2, relief="ridge").place(relx=0.49, rely=0.55, relwidth=0.5, relheight=0.36)
	label14 = tm.Label(windo, text="Final Parameters", relief="groove", bg="grey",
	                   font=("Bradley Hand ITC", 12, "bold")).place(x=400, y=310)
	sep = ttk.Separator(windo, orient='horizontal').pack(side='top')

	entry1 = ttk.Entry(windo, textvar=whpres1, width=12).place(x=210, y=75)
	entry6 = ttk.Entry(windo, textvar=whtemp1, width=12).place(x=210, y=105)
	entry5 = ttk.Entry(windo, textvar=tgrad1, width=12).place(x=210, y=135)
	entry4 = ttk.Entry(windo, textvar=pgrad1, width=12).place(x=210, y=165)
	entry3 = ttk.Entry(windo, textvar=sgr1, width=12).place(x=210, y=195)
	entry2 = ttk.Entry(windo, textvar=gwr1, width=12).place(x=210, y=225)
	entry10 = ttk.Entry(windo, textvar=depth1, width=12).place(x=210, y=255)
	entry7 = tm.Text(windo, width=34, height=3).place(x=400, y=100)
	entry8 = tm.Text(windo, width=34, height=3).place(x=400, y=250)
	entry9 = tm.Text(windo, width=34, height=3).place(x=400, y=175)
	# entry8 = tm.Text(window,textvar=gwr, width = 12).place(x=400,y=250)
	# entry9 = tm.Text(window,textvar=gwr, width = 12).place(x=400,y=175)
	def plotwin():
		windo = tk.ThemedTk()
		windo.get_themes()
		windo.set_theme("plastik")

		windo.iconbitmap('pyc.ico')

		windo.geometry("390x200")
		windo.title("i-SIBHP 2019")

		menu = tm.Menu(windo)
		windo.config(menu=menu)

		def exit1():
			exit()

		subm1 = tm.Menu(menu)
		menu.add_cascade(label="File", menu=subm1)
		subm1.add_command(label="Exit")

		subm2 = tm.Menu(menu)
		menu.add_cascade(label="View", menu=subm2)
		subm2.add_command(label="Exit")
		subm2 = tm.Menu(menu)
		menu.add_cascade(label="About", menu=subm2)
		subm2.add_command(label="About the developer")
		subm2.add_command(label="Exit")

		label1 = ttk.Label(windo, text="Please select parameters to plot", font=('Bradley Hand ITC', 12, 'bold')).pack()
		label2 = ttk.Label(windo, text="x-axis:", font=('Trebuchet MS', 11, 'bold')).place(x=80, y=40)
		label3 = ttk.Label(windo, text="y-axis:", font=('Trebuchet MS', 11, 'bold')).place(x=280, y=40)

		var = tm.StringVar()
		list1 = ["", "Pressure Profile", "Integrals", "Compressibility Factors", "Time"]
		droplist = ttk.OptionMenu(windo, var, *list1).place(x=65, y=80)
		var.set("Select x-axis")

		yvar = tm.StringVar()
		list1 = ["", "Pressure Profile", "Integrals", "Compressibility Factors", "Depth"]
		droplist = ttk.OptionMenu(windo, yvar, *list1).place(x=265, y=80)
		yvar.set("Select y-axis")

		b11 = ttk.Button(windo, text="Plot", width=5, ).place(x=15, y=145)
		b22 = ttk.Button(windo, text="Exit", width=8, command=windo.destroy).place(x=320, y=145)

	b1 = ttk.Button(windo, text="Plot", width=5, command = plotwin).place(x=10, y=550)
	b3 = ttk.Button(windo, text="Solve", width=12, command = calculate ).place(x=530, y=550)
	b2 = ttk.Button(windo, text="Quit", width=8, command=windo.destroy).place(x=630, y=550)

b1 = ttk.Button(window, text="Go", width=5, command = secondwin).place(x=175,y=245)

b2 = ttk.Button(window, text="Exit", width=12, command=exit1).place(x=152,y=275)


var= tm.StringVar()
list1 = ["With gas gravity profile", "Without gas gravity profile", "With gas gravity profile"]
droplist =ttk.OptionMenu(window,var,*list1).place(x=140,y=200)
var.set("Select Method")

window.mainloop()