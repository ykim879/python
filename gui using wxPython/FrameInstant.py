import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = 'check the user whether frame wanna be closed')
		self.Bind(wx.EVT_CLOSE, self.OnClose)

	def OnClose(self, event):
		if wx.MessageBox("Wanna close the window?", 
				"please select the button", 
				wx.YES_NO) != wx.YES:
			event.Skip(False) #do not close the window
		else:
			self.Destroy() #close genearted messagebox

if __name__ == "__main__":
	print("This is main method")
	app = wx.App()
	frame = MyFrame()
	frame.Show(True)

	app.MainLoop()