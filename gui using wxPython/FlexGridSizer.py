import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "FlexGridSizer exercise")
		self.fGridSizer = wx.FlexGridSizer(rows = 3, cols = 2, hgap = 5, vgap = 2) #same as GridSizer
		self.mainPanel = wx.Panel(self)
		#static text
		self.lname = wx.StaticText(self.mainPanel, label = "name: ")
		self.lemail = wx.StaticText(self.mainPanel, label = "email: ")
		self.ltext = wx.StaticText(self.mainPanel, label = "text: ")
		#textCTRL
		self.tname = wx.TextCtrl(self.mainPanel)
		self.temail = wx.TextCtrl(self.mainPanel)
		self.ttext = wx.TextCtrl(self.mainPanel)

		self.fGridSizer.Add(self.lname)
		self.fGridSizer.Add(self.tname, 0, wx.EXPAND)
		self.fGridSizer.Add(self.lemail)
		self.fGridSizer.Add(self.temail, 0, wx.EXPAND)
		self.fGridSizer.Add(self.ltext)
		self.fGridSizer.Add(self.ttext, 0, wx.EXPAND)

		self.fGridSizer.AddGrowableCol(1)
		self.fGridSizer.AddGrowableRow(2)

		self.mainPanel.SetSizer(self.fGridSizer)
if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()