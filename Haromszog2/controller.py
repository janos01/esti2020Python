import wx

from mainframe import MainFrame
from model import Model

class Controller:
    def __init__(self):
        self.frame = MainFrame(None)
        self.frame.Bind(wx.EVT_BUTTON,
            self.onclick_calc_button, 
            self.frame.calc_button)
        self.model = Model()
        self.frame.SetTitle(self.model.get_name())
        self.frame.Show()

    def onclick_calc_button(self):
        pass
