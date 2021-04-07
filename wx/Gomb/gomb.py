import wx

app = wx.App()

frame = wx.Frame(None, title="Gombos")
button = wx.Button(frame, label="Ok")
frame.Show(True)

app.MainLoop()
