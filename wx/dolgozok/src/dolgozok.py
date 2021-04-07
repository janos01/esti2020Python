#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Wed Mar 31 18:55:42 2021
#

import wx
import wx.adv

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade



class MainMenuBar(wx.MenuBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainMenuBar.__init__
        wx.MenuBar.__init__(self, *args, **kwds)
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Megnyitás", "")
        self.Bind(wx.EVT_MENU, self.on_click_open_menu_item, item)
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Mentés", "")
        self.Bind(wx.EVT_MENU, self.on_click_save_menu_item, item)
        wxglade_tmp_menu.AppendSeparator()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Kilépés", "")
        self.Bind(wx.EVT_MENU, self.on_click_exit_menu_item, item)
        self.Append(wxglade_tmp_menu, u"Fájl")
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, u"Névjegy", "")
        self.Bind(wx.EVT_MENU, self.on_click_about_menu_item, item)
        self.Append(wxglade_tmp_menu, u"Súgó")

        # end wxGlade
        


    def on_click_open_menu_item(self, event):  # wxGlade: MainMenuBar.<event_handler>
        fd = wx.FileDialog(self.GetParent())
        if fd.ShowModal() == wx.ID_OK:
            path = fd.GetPath()
            # ~ print(self.GetParent().statusBar)
            self.GetParent().statusBar.SetStatusText(path, 0)
        
        fp = open(path, 'r')
        lines = fp.readlines()
        new_lines = []
        for line in lines:
            line = line.rstrip()
            new_lines.append(line)
            
        self.GetParent().dolgozok_listbox.Append(new_lines)
        event.Skip()

    def on_click_save_menu_item(self, event):  # wxGlade: MainMenuBar.<event_handler>
        print("Event handler 'on_click_save_menu_item' not implemented!")
        event.Skip()

    def on_click_exit_menu_item(self, event):  # wxGlade: MainMenuBar.<event_handler>
        print(self.GetParent())
        self.GetParent().Close()
        event.Skip()

    def on_click_about_menu_item(self, event):  # wxGlade: MainMenuBar.<event_handler>
        about = wx.adv.AboutDialogInfo()
        about.SetName('Dolgozó nyilvántartó')
        about.SetVersion('0.1')
        about.SetDescription('Ez egy gyakorló program')
        about.SetCopyright('Copyright (c) Nagy Jánops, 2021')
        about.SetLicence('Szabadon terjeszthető')
        about.AddDeveloper('Nagy János')
        wx.adv.AboutBox(about)
        event.Skip()

# end of class MainMenuBar
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((440, 337))
        self.SetTitle("frame")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.notebook_1 = wx.Notebook(self.panel_1, wx.ID_ANY)
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)

        self.list_pane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.list_pane, "Lista")

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        self.dolgozok_listbox = wx.ListBox(self.list_pane, wx.ID_ANY, choices=[])
        sizer_2.Add(self.dolgozok_listbox, 1, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_8, 0, wx.EXPAND, 0)

        self.update_button = wx.Button(self.list_pane, wx.ID_ANY, u"Frissítés")
        sizer_8.Add(self.update_button, 0, wx.ALL, 6)

        self.add_pane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.add_pane, u"Hozzáadás")

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        label_1 = wx.StaticText(self.add_pane, wx.ID_ANY, u"Új dolgozó felvétele", style=wx.ALIGN_CENTER_HORIZONTAL)
        sizer_3.Add(label_1, 0, wx.ALL | wx.EXPAND, 6)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.add_pane, wx.ID_ANY, u"Név", style=wx.ALIGN_RIGHT)
        sizer_4.Add(label_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        self.name_text_ctrl = wx.TextCtrl(self.add_pane, wx.ID_ANY, "")
        sizer_4.Add(self.name_text_ctrl, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.add_pane, wx.ID_ANY, u"Település", style=wx.ALIGN_RIGHT)
        sizer_5.Add(label_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        self.city_text_ctrl = wx.TextCtrl(self.add_pane, wx.ID_ANY, "")
        sizer_5.Add(self.city_text_ctrl, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.add_pane, wx.ID_ANY, u"Fizetés", style=wx.ALIGN_RIGHT)
        sizer_6.Add(label_4, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        self.salary_text_ctrl = wx.TextCtrl(self.add_pane, wx.ID_ANY, "")
        sizer_6.Add(self.salary_text_ctrl, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 6)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)

        self.save_button = wx.Button(self.add_pane, wx.ID_ANY, u"Mentés")
        sizer_7.Add(self.save_button, 0, wx.ALL, 6)

        self.add_pane.SetSizer(sizer_3)

        self.list_pane.SetSizer(sizer_2)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.on_click_update_button, self.update_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_save_button, self.save_button)
        # end wxGlade
        
        menusav = MainMenuBar()
        self.SetMenuBar(menusav)
        self.statusBar = self.CreateStatusBar(1)
        

        

    def on_click_save_button(self, event):  # wxGlade: MyFrame.<event_handler>
        path = self.statusBar.GetStatusText(0)
        name = self.name_text_ctrl.GetValue()        
        city = self.city_text_ctrl.GetValue()        
        salary = self.salary_text_ctrl.GetValue()
        if path == '':
            wx.MessageBox('Nincs fájl kiválasztva!', 'Figyelem')
        elif (name == '' or
            city == '' or
            salary == ''):
            wx.MessageBox('Nincs adat!', 'Figyelem')
        else:            
            line = name + ':' + city + ':' + salary + '\n'
            print(line)
            fp = open(path, 'a')
            fp.write(line)
            fp.close()
        event.Skip()
    def on_click_update_button(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_click_update_button' not implemented!")
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