import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent = None, title = "Slider & Gauge")
		self.mainPanel = wx.Panel(self)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)

		self.slider = wx.Slider(self.mainPanel, minValue = 0, maxValue = 100)
		self.gauge = wx.Gauge(self.mainPanel, range = 100)

		self.mainSizer.Add(self.slider, 1, wx.ALL|wx.EXPAND, 5)
		self.mainSizer.Add(self.gauge, 1, wx.ALL|wx.EXPAND, 5)

		self.mainPanel.SetSizer(self.mainSizer)

		self.Bind(wx.EVT_SLIDER, self.OnSliderChange, self.slider)
	def OnSliderChange(self, e):
		self.gauge.SetValue(self.slider.GetValue())

if __name__ == "__main__":
	app = wx.App()
	frame = MyFrame()
	frame.Show()

	app.MainLoop()