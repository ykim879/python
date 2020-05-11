import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "Menu Example")

		self.menubar = wx.MenuBar()
		#global value - fileMenu
		fileMenu = wx.Menu()
		fileNewMenu = fileMenu.Append(wx.ID_ANY, "New File")
		fileOpenMenu = fileMenu.Append(wx.ID_ANY, "Open File")
		fileMenu.AppendSeparator()
		fileCloseMenu = fileMenu.Append(wx.ID_ANY, "CLOSE")
		#global value - test
		testMenu = wx.Menu()
		testHelloMenu = testMenu.Append(wx.ID_ANY, "&TEST")
		#append to global
		self.menubar.Append(fileMenu, "&File")
		self.menubar.Append(testMenu, "&Test")

		self.SetMenuBar(self.menubar)

		self.Bind(wx.EVT_MENU, self.OnNew, fileNewMenu)
		self.Bind(wx.EVT_MENU, self.OnOpen, fileOpenMenu)
		self.Bind(wx.EVT_MENU, self.OnClose, fileCloseMenu)
		self.Bind(wx.EVT_MENU, self.Hello, testHelloMenu)

	def OnNew(self, e):
		wx.MessageBox("New File")
	def OnOpen(self, e):
		wx.MessageBox("Open File")
	def OnClose(self, e):
		self.Close()
	def Hello(self, e):
		wx.MessageBox("Hello");


if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()