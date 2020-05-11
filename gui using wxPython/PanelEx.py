import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "PanelEx.py")
		self.mainPanel = wx.Panel(self)
		self.leftPanel = wx.Panel(mainPanel)
		self.rightPanel = wx.Panel(mainPanel)

		self.leftPanel.SetBackgroundColour(wx.RED)
		self.rightPanel.SetBackgroundColour(wx.BLUE)
if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()