import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "practicing EVT")

		self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButton)
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRButton)

	def OnMouseLButton(self, event):
		frame.SetSize(wx.Size(400,200))
		self.SetBackgroundColour(wx.Colour(200,0,0,200))
		self.SetWindowStyle(wx.RESIZE_BORDER | wx.CAPTION)
		self.Refresh()
	def OnMouseRButton(self, event):
		frame.SetSize(wx.Size(200,400))
		self.SetBackgroundColour(wx.Colour(0,200,0,100)) #setBackgroundColour requires color value and wx.Colour return colour value
		self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)
		self.Refresh()

if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()

	app.MainLoop()