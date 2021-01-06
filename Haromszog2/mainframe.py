import wx

class MainFrame(wx.Frame):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent)
        self.SetSize((400, 300))
        
        self.base_label = wx.StaticText(self, label="Alap")
        self.base_text = wx.TextCtrl(self)        
        self.height_label = wx.StaticText(self, label="Magasság")
        self.height_text = wx.TextCtrl(self)        
        self.calc_button = wx.Button(self, label="Számít")
        self.result_text = wx.TextCtrl(self)
        
        self.vbox1 = wx.BoxSizer(wx.VERTICAL)
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)        
        self.vbox1.Add(self.hbox1)
        self.vbox1.Add(self.hbox2)
        self.vbox1.Add(self.hbox3)
        
        self.hbox1.Add(self.base_label);
        self.hbox1.Add(self.base_text);
        self.hbox2.Add(self.height_label);
        self.hbox2.Add(self.height_text);
        self.hbox3.Add(self.calc_button);
        self.hbox3.Add(self.result_text);
        
        self.SetSizer(self.vbox1)
        self.Layout()
        
        
