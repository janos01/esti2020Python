#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Wed Apr  7 18:09:20 2021
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("frame")

        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Megnyitás", "")
        self.Bind(wx.EVT_MENU, self.on_click_open_menu, item)
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Mentés", "")
        self.Bind(wx.EVT_MENU, self.on_click_save_menu, item)
        wxglade_tmp_menu.AppendSeparator()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Kilépés", "")
        self.Bind(wx.EVT_MENU, self.on_click_exit_menu, item)
        self.frame_menubar.Append(wxglade_tmp_menu, u"Fájl")
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Súgó", "")
        self.Bind(wx.EVT_MENU, self.on_click_help_menu, item)
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Névjegy", "")
        self.Bind(wx.EVT_MENU, self.on_click_about_menu, item)
        self.frame_menubar.Append(wxglade_tmp_menu, u"Súgó")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_1.Add((0, 0), 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        # end wxGlade

    def on_click_open_menu(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_click_open_menu' not implemented!")
        event.Skip()

    def on_click_save_menu(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_click_save_menu' not implemented!")
        event.Skip()

    def on_click_exit_menu(self, event):  # wxGlade: MyFrame.<event_handler>
        self.Close()
        event.Skip()

    def on_click_help_menu(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_click_help_menu' not implemented!")
        event.Skip()

    def on_click_about_menu(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_click_about_menu' not implemented!")
        event.Skip()

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
