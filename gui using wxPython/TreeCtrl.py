import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "TreeCtrl Example")

		self.mainPanel = wx.Panel(self)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.mainPanel.SetSizer(self.mainSizer)

		self.button = wx.Button(self.mainPanel, label = "Expand")
		self.mainSizer.Add(self.button, 0, wx.EXPAND|wx.ALL, 5)

		self.tree = wx.TreeCtrl(self.mainPanel)
		self.beverage = self.tree.AddRoot('beverage')
		self.tree.AppendItem(self.beverage, "milkshake")
		self.coffee = self.tree.AppendItem(self.beverage, "coffee")
		self.tree.AppendItem(self.beverage, "tea")
		self.tree.AppendItem(self.coffee, "Americano")
		self.tree.AppendItem(self.coffee, "Cappuchino")

		self.mainSizer.Add(self.tree, 5, wx.ALL|wx.EXPAND, 5)

		self.staticText = wx.StaticText(self.mainPanel, style = wx.ALIGN_CENTER)
		self.mainSizer.Add(self.staticText, 0, wx.EXPAND|wx.ALL, 5)

		self.Bind(wx.EVT_BUTTON, self.OnExpandButton, self.button)
		self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnNodeSelected, self.tree)

	def OnExpandButton(self, e):
		self.tree.ExpandAll()

	def OnNodeSelected(self, e):
		self.staticText.SetLabel(self.tree.GetItemText(self.tree.GetSelection()))
		self.mainPanel.Layout()

if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()