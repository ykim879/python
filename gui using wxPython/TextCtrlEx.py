import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "TextCtrl Example")
		self.SetSize(250,100)
		#Panel
		self.mainPanel = wx.Panel(self)
		self.mainPanel.SetSize(250, 100)
		self.leftPanel = wx.Panel(self.mainPanel)
		self.leftPanel.SetMinSize(wx.Size(125, 100))
		self.rightPanel = wx.Panel(self.mainPanel)
		self.rightPanel.SetMinSize(wx.Size(125,100))
		
		self.leftSizer = wx.BoxSizer(wx.VERTICAL)
		self.lRed = wx.StaticText(self.leftPanel,label = "Red:")
		self.lGreen = wx.StaticText(self.leftPanel, label = "Green:")
		self.lBlue = wx.StaticText(self.leftPanel, label = "Blue:")
		self.leftSizer.Add(self.lRed, wx.ALL)
		self.leftSizer.Add(self.lGreen, wx.ALL)
		self.leftSizer.Add(self.lBlue, wx.ALL)
		self.leftPanel.SetSizer(self.leftSizer)

		self.rightSizer = wx.BoxSizer(wx.VERTICAL)
		self.tRed = wx.TextCtrl(self.rightPanel, value = '255')
		self.tGreen = wx.TextCtrl(self.rightPanel, value = '255')
		self.tBlue = wx.TextCtrl(self.rightPanel, value = '255')
		self.rightSizer.Add(self.tRed, wx.EXPAND|wx.ALL)
		self.rightSizer.Add(self.tGreen, wx.EXPAND|wx.ALL)
		self.rightSizer.Add(self.tBlue, wx.EXPAND|wx.ALL)
		self.rightPanel.SetSizer(self.rightSizer)

		self.Bind(wx.EVT_TEXT, self.Color, self.tRed)
		self.Bind(wx.EVT_TEXT, self.Color, self.tGreen)
		self.Bind(wx.EVT_TEXT, self.Color, self.tBlue)
		self.ChangeColor()

		self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.mainSizer.Add(self.leftPanel)
		self.mainSizer.Add(self.rightPanel)
		self.mainPanel.SetSizer(self.mainSizer)
	
	def Color(self, e):
		self.ChangeColor()

	def ChangeColor(self):
		r = self.tRed.GetValue()
		b = self.tBlue.GetValue()
		g = self.tGreen.GetValue()
		self.mainPanel.SetBackgroundColour(wx.Colour(int(r, base = 10),int(g, base = 10),int(b, base = 10)))
		self.mainPanel.Refresh()


if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
