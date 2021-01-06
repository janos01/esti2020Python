import wx

class MainFrame(wx.Frame):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent)
        self.button = wx.Button(self, label="Változtat")
        self.button.Bind(wx.EVT_BUTTON, self.OnClickButton)
    def OnClickButton(self, event):
        self.SetTitle('Új szöveg')
# MainFrame vége

class GombesApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None)
        frame.Show()
        return True
# GombesApp vége3

app = GombesApp()
app.MainLoop()

