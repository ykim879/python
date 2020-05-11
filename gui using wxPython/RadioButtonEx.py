import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "RadioButton Example")
		self.mainPanel = wx.Panel(self)
		self.mainSizer = wx.StaticBoxSizer(wx.VERTICAL, self.mainPanel, label = "Color")

		#upper Panel
		self.upperPanel = wx.Panel(self.mainPanel)
		self.upperSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.rRed = wx.RadioButton(self.upperPanel, label = "Red", style = wx.RB_GROUP)
		self.rBlue = wx.RadioButton(self.upperPanel, label = "Blue")
		self.rGreen = wx.RadioButton(self.upperPanel, label = "Green")
		self.upperSizer.Add(self.rRed, wx.ALL)
		self.upperSizer.Add(self.rBlue, wx.ALL)
		self.upperSizer.Add(self.rGreen, wx.ALL)
		self.upperPanel.SetSizer(self.upperSizer)

		self.Bind(wx.EVT_RADIOBUTTON, self.Red, self.rRed)
		self.Bind(wx.EVT_RADIOBUTTON, self.Blue, self.rBlue)
		self.Bind(wx.EVT_RADIOBUTTON, self.Green, self.rGreen)
		#under Panel
		self.underPanel = wx.Panel(self.mainPanel)

		self.rEnable = wx.RadioButton(self.underPanel, label = "Enable", style = wx.RB_GROUP)
		self.rDiable = wx.RadioButton(self.underPanel, label = "Disable")

		self.underSizer = wx.BoxSizer(wx.HORIZONTAL)
	
		self.underSizer.Add(self.rEnable, wx.ALL)
		self.underSizer.Add(self.rDiable, wx.ALL)

		self.underPanel.SetSizer(self.underSizer)

		self.Bind(wx.EVT_RADIOBUTTON, self.Disable, self.rDiable)
		self.Bind(wx.EVT_RADIOBUTTON, self.Enable, self.rEnable)

		#add on mainSizer
		self.mainSizer.Add(self.upperPanel, wx.ALL|wx.EXPAND)
		self.mainSizer.Add(self.underPanel, wx.ALL|wx.EXPAND)
		self.mainPanel.SetSizer(self.mainSizer)


	def Red(self, e):
		self.mainPanel.SetBackgroundColour(wx.RED)
		self.mainPanel.Refresh()
	def Blue(self, e):
		self.mainPanel.SetBackgroundColour(wx.BLUE)
		self.mainPanel.Refresh()
	def Green(self, e):
		self.mainPanel.SetBackgroundColour(wx.GREEN)
		self.mainPanel.Refresh()
	def Disable(self, e):
		self.rRed.Enable(False)
		self.rGreen.Enable(False)
		self.rBlue.Enable(False)
	def Enable(self, e):
		self.rRed.Enable(True)
		self.rGreen.Enable(True)
		self.rBlue.Enable(True)

if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()