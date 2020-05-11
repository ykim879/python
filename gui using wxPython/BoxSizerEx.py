import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "Box Sizer Example")

		self.mainPanel = wx.Panel(self)
		self.upperPanel = wx.Panel(self.mainPanel)
		self.upperPanel.SetMinSize(wx.Size(400,-1)) #-1 auto
		self.upperPanel.SetBackgroundColour(wx.RED)

		self.leftButton = wx.Button(self.upperPanel, label = 'left')
		self.rightButton = wx.Button(self.upperPanel, label = 'right')

		self.hBoxSizer = wx.StaticBoxSizer(wx.HORIZONTAL, self.upperPanel, "Upper")
		self.hBoxSizer.Add(self.leftButton) #add button to the boxsizer
		self.hBoxSizer.Add(self.rightButton)
		self.upperPanel.SetSizer(self.hBoxSizer)

		self.middleButton = wx.Button(self.mainPanel, label = "middle")
		self.bottomButton = wx.Button(self.mainPanel, label = "bottom")

		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.mainSizer.Add(self.upperPanel, 0, wx.ALIGN_LEFT|wx.TOP|wx.LEFT, 5)
		self.mainSizer.Add(self.middleButton, 1, wx.EXPAND | wx.ALL, 5)
		self.mainSizer.Add(self.bottomButton, 0, wx.ALIGN_RIGHT|wx.BOTTOM, 5)
		self.mainPanel.SetSizer(self.mainSizer)

if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()

	app.MainLoop() 
