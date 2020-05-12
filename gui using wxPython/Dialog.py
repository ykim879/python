import wx

class MyDialog(wx.Dialog):
	def __init__(self, _parent, _title):
		wx.Dialog.__init__(self, parent = _parent, title = _title)
		self.SetSize(200,100)
		self.mainPanel = wx.Panel(self)
		self.closeButton = wx.Button(self.mainPanel, label = "Close")
		self.Bind(wx.EVT_BUTTON, self.OnClose, self.closeButton)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
	def OnClose(self, e):
		self.Destroy()
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "Modeal & Modeless")
		self.SetSize(400,200)
		self.mainPanel = wx.Panel(self)
		self.mainSizer = wx.FlexGridSizer(rows = 1, cols = 2, hgap = 5, vgap = 5)
		self.mainPanel.SetSizer(self.mainSizer)

		self.modal = wx.Button(self.mainPanel, label = "Modal")
		self.modeless = wx.Button(self.mainPanel, label = "Modeless")

		self.mainSizer.Add(self.modal, 0, wx.ALIGN_LEFT|wx.ALL, 5)
		self.mainSizer.Add(self.modeless, 0, wx.ALIGN_RIGHT|wx.ALL, 5)
		self.mainSizer.AddGrowableRow(0)

		self.Bind(wx.EVT_BUTTON, self.Modal, self.modal)
		self.Bind(wx.EVT_BUTTON, self.Modeless, self.modeless)

	def Modal(self, e):
		dlg = MyDialog(self, "Modal Dialog").ShowModal()
		print dlg
	def Modeless(self, e):
		dlg = MyDialog(self, "Modeless Dialog")
		dlg.Show()
if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()