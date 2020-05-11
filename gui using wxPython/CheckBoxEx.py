import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "CheckBox Example")
		self.mainPanel = wx.Panel(self)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.checkBold = wx.CheckBox(self.mainPanel, label = "Bold")
		self.checkBold.SetValue(wx.CHK_CHECKED)
		self.mainSizer.Add(self.checkBold, wx.ALL)

		self.checkItalic = wx.CheckBox(self.mainPanel, label = "Italic")
		self.checkItalic.SetValue(wx.CHK_CHECKED)
		self.mainSizer.Add(self.checkItalic, wx.ALL)


		self.text = wx.StaticText(self.mainPanel, label = "I am a Programmer")
		self.mainSizer.Add(self.text, wx.ALL)
		self.mainPanel.SetSizer(self.mainSizer)

		self.Bind(wx.EVT_CHECKBOX, self.OnCheck, self.checkBold)
		self.Bind(wx.EVT_CHECKBOX, self.OnCheck, self.checkItalic)
		self.ChangeFont()


	def OnCheck(self, e):
		self.ChangeFont()

	def ChangeFont(self):
		style = wx.FONTSTYLE_NORMAL
		weight = wx.FONTWEIGHT_NORMAL

		if self.checkBold.GetValue() == wx.CHK_CHECKED:
			weight = wx.FONTWEIGHT_BOLD
		if self.checkItalic.GetValue() == wx.CHK_CHECKED:
			style = wx.FONTSTYLE_ITALIC

		font = wx.Font(10, wx.FONTFAMILY_DEFAULT, style, weight)
		self.text.SetFont(font)

if __name__ == "__main__":
	app = wx.App()
	font = MyFrame()
	font.Show()
	app.MainLoop()