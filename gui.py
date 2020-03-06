from tkinter import *
from tkinter import filedialog
from hexagonify import hexagonify

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	
	
	"""Opens a file chooser dialog to select a picture"""
	def browsefunc(self):
		filename = filedialog.askopenfilename()
		self.PATHLABEL.config(text=filename)
	
	"""Hexagonifies the image and shows it to the user"""
	def generateImage(self):
		if str.isdigit(self.HEX_SIZE.get()) and self.PATHLABEL.cget("text") is not "":
			hex_size = int(self.HEX_SIZE.get())
			file = self.PATHLABEL.cget("text")
			self.im = hexagonify(file, hex_size)
			self.im.show()
	
	"""Opens a file saver dialog and saves image"""
	def saveIm(self):
		files = [("PNG","*.png"),("JPEG", "*.jpg"),("All Files", "*.*")]
		filename = filedialog.asksaveasfilename(filetypes = files, defaultextension = files)
		if filename:
			self.im.save(filename, quality = 100, subsampling=0)
	
	"""Sets up the GUI"""
	def createWidgets(self):
		self.BROWSEBUTTON = Button(self, text="Browse", command=self.browsefunc)
		self.BROWSEBUTTON.grid(row=0, column=1)
		
		self.PATHLABEL = Label(self)
		self.PATHLABEL.grid(row=0,column=0)
		
		self.HEX_SIZE = Entry(self,textvariable=StringVar(self,value="20"))
		self.HEX_SIZE.grid(row=1,column=1)
		
		self.HEX_LABEL = Label(self,text="Hexagon size")
		self.HEX_LABEL.grid(row=1,column=0)
		
		self.GENERATEBUTTON = Button(self, text="Generate Image", command = self.generateImage)
		self.GENERATEBUTTON.grid(row=2,column=0)
		
		self.SAVEBUTTON = Button(self, text="Save", command=self.saveIm)
		self.SAVEBUTTON.grid(row=2,column=1)
		
		
	
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()