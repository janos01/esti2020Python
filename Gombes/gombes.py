import wx

class MainFrame(wx.Frame):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent)
# MainFrame vége

class GombesApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None)
        frame.Show()
        return True
# GombesApp vége3

app = GombesApp()
app.MainLoop()

