import wx 
from controller import Controller

class Harmoszog(wx.App):
    def OnInit(self):
        Controller()
        return True

app = Harmoszog()
app.MainLoop()
