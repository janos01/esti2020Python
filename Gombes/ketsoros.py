import wx

class MainFrame(wx.Frame):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent)

        self.button1 = wx.Button(self, label="gomb1")
        self.button2 = wx.Button(self, label="gomb2")
        self.text1 = wx.TextCtrl(self)
        self.text2 = wx.TextCtrl(self)

        # elrendezés
        self.vbox1 = wx.BoxSizer(wx.VERTICAL)
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        self.vbox1.Add(self.hbox1)
        self.vbox1.Add(self.hbox2)
        self.hbox1.Add(self.text1)
        self.hbox1.Add(self.button1)
        self.hbox2.Add(self.text2)
        self.hbox2.Add(self.button2)

        self.SetSizer(self.vbox1)
        self.Layout()


# MainFrame vége

class GombesApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None)
        frame.Show()
        return True
# GombesApp vége3

app = GombesApp()
app.MainLoop()

