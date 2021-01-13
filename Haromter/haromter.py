import wx
import math

class MainFrame(wx.Frame):
	def __init__(self, parent):
		super(MainFrame, self).__init__(parent)
		
		aLabel = wx.StaticText(self, label='a oldal')
		self.aText = wx.TextCtrl(self)
		bLabel = wx.StaticText(self, label='b oldal')
		self.bText = wx.TextCtrl(self)
		cLabel = wx.StaticText(self, label='c oldal')
		self.cText = wx.TextCtrl(self)
		
		calcButton = wx.Button(self, label='Számít')
		calcButton.Bind(wx.EVT_BUTTON, self.onClickCalcButton)
		self.areaText = wx.TextCtrl(self)
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		
		vbox.Add(hbox1, 0, wx.EXPAND)
		vbox.Add(hbox2, 0, wx.EXPAND)
		vbox.Add(hbox3, 0, wx.EXPAND)
		vbox.Add(hbox4, 0, wx.EXPAND)
		
		hbox1.Add(aLabel, 1, wx.ALL, 6)
		hbox1.Add(self.aText, 1, wx.ALL, 6)
		hbox2.Add(bLabel, 1, wx.ALL, 6)
		hbox2.Add(self.bText, 1, wx.ALL, 6)
		hbox3.Add(cLabel, 1, wx.ALL, 6)
		hbox3.Add(self.cText, 1, wx.ALL, 6)
		
		hbox4.Add(calcButton, 1, wx.ALL, 6)
		hbox4.Add(self.areaText, 1, wx.ALL, 6)		
		
		self.SetSizer(vbox)
		self.Layout()
		
	def onClickCalcButton(self, event):
		a = float(self.aText.GetValue())
		b = float(self.bText.GetValue())
		c = float(self.cText.GetValue())
		s = (a+b+c)/2
		area = math.sqrt(s*(s-a)*(s-b)*(s-c))
		self.areaText.SetValue(str(area))
	    # 30, 35, 40 > 508.	

class HaromterApp(wx.App):
	def OnInit(self):
		frame = MainFrame(None)
		frame.Show()
		return True

app = HaromterApp()
app.MainLoop()
