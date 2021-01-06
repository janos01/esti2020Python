import wx

class MainFrame(wx.Frame):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent)

        self.button = wx.Button(self, label="Dupla")
        self.button.Bind(wx.EVT_BUTTON, self.OnClickButton)
        self.text = wx.TextCtrl(self)

        # elrendezés
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.text)
        vbox.Add(self.button)
        self.SetSizer(vbox)
        self.Layout()

    def OnClickButton(self, event):
        szamStr = self.text.GetValue()
        szam = int(szamStr)
        dupla = szam * 2
        self.text.SetValue(str(dupla))
# MainFrame vége

class GombesApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None)
        frame.Show()
        return True
# GombesApp vége3

app = GombesApp()
app.MainLoop()

