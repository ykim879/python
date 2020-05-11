import wx

class MyFrame(wx.Frame): #class returning frame inheritated wx.frame
	def __init__(self):
		wx.Frame.__init__(self, parent = None )#call inherited constructor,
		button = wx.Button(self, label = "click!") # can put label by label = "Click!"
		button.SetSize(10,10)
		button.Bind(wx.EVT_BUTTON, self.ClickButton)
	def ClickButton(self, event):
		wx.MessageBox("The button is clicked!", "Popped Up!", wx.OK)
if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()

	app.MainLoop()