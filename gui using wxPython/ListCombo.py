import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "Combo/ListBox Example")
		self.mainPanel = wx.Panel(self)
		self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
		colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
		self.comboBox = wx.ComboBox(self.mainPanel, choices = colors) #style = wx.CB_READONLY
		self.colorListBox = wx.ListBox(self.mainPanel, size = wx.Size(100, 200))

		self.mainSizer.Add(self.comboBox, 0, wx.ALL, 5)
		self.mainSizer.Add(self.colorListBox, 1, wx.ALL, 5)

		self.Bind(wx.EVT_COMBOBOX, self.ClickComboBox, self.comboBox)
		self.Bind(wx.EVT_LISTBOX, self.ClickListBox, self.colorListBox)


		self.mainPanel.SetSizer(self.mainSizer)
	def ClickComboBox(self, e):
		self.colorListBox.Append(self.comboBox.Items[self.comboBox.GetCurrentSelection()])
	def ClickListBox(self, e):
		wx.MessageBox(self.colorListBox.Items[self.colorListBox.GetSelection()])

if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()

