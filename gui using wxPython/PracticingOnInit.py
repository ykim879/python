#for wx we use Oninit instead of init
import wx

class MyApp(wx.App):
	def OnInit(self):
		#appear frame 
		frame = wx.Frame(parent=None, title='creating my own app instant')
		frame.Show(True)
		return True


if __name__ == "__main__": #check whether this is in main class
	app = MyApp()
	app.MainLoop()