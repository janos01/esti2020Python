
import wx

print('Olvasás fájlból')

program = wx.App(False)
ablak = wx.Frame(None, title='Párbeszéd')
ablak.Show()
fd = wx.FileDialog(ablak, style=wx.FD_OPEN)
fd.Show()
program.MainLoop()
