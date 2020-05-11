from datatime import datatime
import sqlite3
import wx
import wx.htm12 #WebView
import ntpath
import base64

RECORD_PER_PAGE = 5 #THIS VARIABLE IS FOR HOW MANY RECORDS I WANT TO PLACE IN ONE PAGE

class MainFrame (wx.Frame):
	def _init_(self):
		wx.Frame._init_ (self,
			None,
			title = '140 words diary',
			size = wx.Size(715, 655),
			style = wx.DEFAULT_FRAME_STYLE)
		self.MaxImageSize = 200

		self.mainPanel = wx.Panel(self) # this is like calling the scene from screen itself

		#from here ubfirnation about the words you write on the diary

		self.leftPanel = wx.Panel(self.mainPanel)
		self leftPanel.SetMaxSize(wx.Size(200, -1))
		self.input_image_path = ""
		self.inputTextCtrl = wx.TextCtrl(
			self.leftPanel, size = wx.TE_MULTILINE)

		self.inputTextCtrl.SetMaxLength(140)
		self.inputTextCtrl.Bind(wx.EVT_TEXT, self.OnTypeText)
		self.leftSizer = wx.BoxSizer(wx.VERTICAL)
		self.leftSizer.Add(inputTextCtrl)