#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Wed Jan 27 18:35:34 2021
#

# Nagy János, 2021-01-27

import wx
import math
import sys

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle(u"Romb - Nagy János, 2021-01-27")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Nagy János, 2021-01-27")
        sizer_1.Add(label_1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.TOP, 6)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Oldal", style=wx.ALIGN_RIGHT)
        sizer_2.Add(label_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        self.side_text = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_2.Add(self.side_text, 1, wx.ALL, 6)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Szög", style=wx.ALIGN_RIGHT)
        sizer_3.Add(label_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        self.deg_text = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_3.Add(self.deg_text, 1, wx.ALL, 6)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Eredmény", style=wx.ALIGN_RIGHT)
        sizer_4.Add(label_4, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        self.res_text = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        sizer_4.Add(self.res_text, 1, wx.ALL, 6)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)

        self.calc_button = wx.Button(self.panel_1, wx.ID_ANY, u"Számol")
        sizer_5.Add(self.calc_button, 1, wx.ALL, 6)

        self.exit_button = wx.Button(self.panel_1, wx.ID_ANY, u"Kilépés")
        sizer_5.Add(self.exit_button, 1, wx.ALL, 6)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.on_click_calc_button, self.calc_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_exit_button, self.exit_button)
        # end wxGlade

    def on_click_calc_button(self, event):  # wxGlade: MainFrame.<event_handler>
        side = float(self.side_text.GetValue())
        deg = float(self.deg_text.GetValue())
        ker = 4* side
        ter = math.pow(side, 2) * math.sin(deg * math.pi /180)
        res = 'Kerület: ' + str(ker) + ' Terület: ' + str(ter)
        self.res_text.SetValue(res)        
        event.Skip()
        
    def on_click_exit_button(self, event):  # wxGlade: MainFrame.<event_handler>
        sys.exit(0)
        event.Skip()
# end of class MainFrame

class MyApp(wx.App):
    def OnInit(self):
        self.main_frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.main_frame)
        self.main_frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
