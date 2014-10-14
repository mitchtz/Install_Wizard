#Code by Mitch Zinser
import tkinter as tk
from tkinter import *

from subprocess import check_call
#import os
from tkinter import messagebox
import urllib
from urllib.request import urlopen, URLopener #imports urlopen, urlopener
from platform import machine #for platform machine version to detect OS architecture
	
master = tk.Tk()
####IOError catches can't find file
#Variables for program checkbox variables. 0 is unchecked, 1 is checked
chrome = tk.IntVar()
firefox = tk.IntVar()
skype = tk.IntVar()
vlc = tk.IntVar()
java = tk.IntVar()
zip = tk.IntVar()
reader = tk.IntVar()
mbam = tk.IntVar()
dropbox = tk.IntVar()


#Test string for test output
text1 = tk.StringVar()

#Changes the title of the tkinter window
master.title("")
try: #Try to import logo, if moved or renamed will fail. Place logo in same folder as program or program launcher
	#Changes the logo of the tkinter window
	master.iconbitmap('MM_Logo.ico')
except:
	text1.set("Icon import error")

#Get online installer and run file once downloaded
def online_install():
	#Create url
	url = urlCreate()
	#Create object to open url
	ninite = URLopener()
	#Download file from url and save as installer.exe
	try:
		ninite.retrieve(url, 'ninite.exe')
	except: #Error in retrieving website
		text1.set('Ninite website could\nnot be accessed')
	#Run the file
	try:
		check_call('ninite.exe', shell=True)
	except: #Error in running file
		text1.set('Error running ninite file')

#Creates url to get ninite file from, checks all check boxes
def urlCreate():
	#URL for ninite must be alphabetical and have - between words. Must add /ninite.exe to dl properly
	url = "https://ninite.com/"
	#Check for state of checkboxes
	if zip.get():
		url += '7zip-'
	if chrome.get():
		url += 'chrome-'
	if dropbox.get():
		url += 'dropbox-'
	if firefox.get():
		url += 'firefox-'
	if java.get():
		url += 'java-'
	if mbam.get():
		url += 'malwarebytes-'
	if reader.get():
		url += 'reader-'
	if skype.get():
		url += 'skype-'
	if vlc.get():
		url += 'vlc-'
	
	#Remove extra - (or extra / if nothing checked)
	url = url[:-1]
	url += '/ninite.exe'
	#text1.set(url)
	return url

#Get and run local installer (takes in 
def local_install():
	if messagebox.askokcancel("Warning", "This process will start each installer one after another\nThis program will be unresponsive during installs\nDon't exit the program or installs will stop"):	
		#Check for state of checkboxes
		#Old method of using check_call('filepath') create pop up console, subprocess.check_call doesn't
		text1.set(str(machine()))
		if zip.get():
			#Run the file
			#check_call('Installers\zip_32bit.exe', shell=True)
			#text1.set(machine())
			if machine() == 'AMD64':
				try:
					check_call('Installers\zip_64bit.msi', shell=True)
				except:
					text1.set('7_Zip local install error')
				
			####add other if statements for other systems if necessary
			else:
				try:
					check_call('Installers\zip_32bit.exe', shell=True)
				except:
					text1.set('7-Zip local install error')
		if chrome.get():
			#Run the file
			try:
				check_call('Installers\chrome.exe', shell=True)
			except:
				text1.set('Chrome local install error')
		if dropbox.get():
			#Run the file
			try:
				check_call('Installers\dropbox.exe', shell=True)
			except:
				text1.set('Dropbox local install error')
		if firefox.get():
			#Run the file
			try:
				check_call('Installers\firefox.exe', shell=True)
			except:
				text1.set('Firefox local install error')
		if java.get():
			#Run the file
			try:
				check_call('Installers\jre_7u67_32bit.exe', shell=True)
			except:
				text1.set('Java_32 local install error')
			if machine() == 'AMD64':
				try:
					check_call('Installers\jre_7u67_x64.exe', shell=True)
				except:
					text1.set('Java_64 local install error')
		if mbam.get():
			#Run the file
			try:
				check_call('Installers\mbam.exe', shell=True)
			except:
				text1.set('Mbam local install error')
		if reader.get():
			#Run the file
			try:
				check_call('Installers\pdf_adobe11.exe', shell=True)
			except:
				text1.set('Reader local install error')
		if skype.get():
			#Run the file
			try:
				check_call('Installers\skype.exe', shell=True)
			except:
				text1.set('Skype local install error')
		if vlc.get():
			#Run the file
			try:
				check_call('Installers\media_vlc_32bit.exe', shell=True)
			except:
				text1.set('VLC local install error')

#def messageWindow():
#    win = Toplevel()
#    win.title('warning')
#    message = "This will delete stuff"
#    Label(win, text=message).pack()
#    Button(win, text='Button1', command=).pack()

def zip_check():
	win = Toplevel()
	win.title('7-Zip version')
	Label(win, text='Which 7-Zip version do you want?').pack()
	Button(win, text='64 bit', command=check_call('Installers\zip_64bit.exe')).pack()
	Button(win, text='32 bit', command=check_call('Installers\zip_32bit.exe')).pack()
	

#Checkbox for Chrome
ch = Checkbutton(master, text="Chrome", variable=chrome)
#Position the button (sticky = 'w' makes the box align to left of column its in)
ch.grid(row = 0, column = 0, sticky='w')

#Checkbox for Firefox
fi = Checkbutton(master, text="Firefox", variable=firefox)
#Position the button (sticky = 'w' makes the box align to left of column its in)
fi.grid(row = 0, column = 1, sticky='w')

#Checkbox for Skype
sk = Checkbutton(master, text="Skype", variable=skype)
#Position the button (sticky = 'w' makes the box align to left of column its in)
sk.grid(row = 1, column = 0, sticky='w')

#Checkbox for VLC
vl = Checkbutton(master, text="VLC", variable=vlc)
#Position the button (sticky = 'w' makes the box align to left of column its in)
vl.grid(row = 1, column = 1, sticky='w')

#Checkbox for Java
ja = Checkbutton(master, text="Java", variable=java)
#Position the button (sticky = 'w' makes the box align to left of column its in)
ja.grid(row = 2, column = 0, sticky='w')

#Checkbox for 7-Zip
zi = Checkbutton(master, text="7-Zip", variable=zip)
#Position the button (sticky = 'w' makes the box align to left of column its in)
zi.grid(row = 2, column = 1, sticky='w')

#Checkbox for Reader
re = Checkbutton(master, text="Reader", variable=reader)
#Position the button (sticky = 'w' makes the box align to left of column its in)
re.grid(row = 3, column = 0, sticky='w')

#Checkbox for Malwarebytes
ma = Checkbutton(master, text="Mbam", variable=mbam)
#Position the button (sticky = 'w' makes the box align to left of column its in)
ma.grid(row = 3, column = 1, sticky='w')

#Checkbox for Dropbox
dr = Checkbutton(master, text="Dropbox", variable=dropbox)
#Position the button (sticky = 'w' makes the box align to left of column its in)
dr.grid(row = 4, column = 0, sticky='w')

#Button for Ninite installer, calls command online_open
ni = Button(master, text = "Ninite", command = online_install)
#Position the button (sticky = 'w' makes the box align to left of column its in)
ni.grid(row = 5, column = 0)

#Button for local installers, calls command local_install
lo = Button(master, text = "Local", command = local_install)
#Position the button (sticky = 'w' makes the box align to left of column its in)
lo.grid(row = 5, column = 1)

#Displays the queue in top, using a text variable so that the list can update in real time
State1 = Label(master, textvariable = text1)
#Position the label
State1.grid(row = 6, column = 0, columnspan = 2)

#run main loop
master.mainloop()