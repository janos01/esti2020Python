#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Wed Apr 21 18:55:42 2021
#

import wx
import wx.adv

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 338))
        self.SetTitle(u"Könyvtár")

        self.frame_statusbar = self.CreateStatusBar(1)
        self.frame_statusbar.SetStatusWidths([-1])

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        root_box = wx.BoxSizer(wx.VERTICAL)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"Könyvtár", style=wx.ALIGN_CENTER_HORIZONTAL)
        root_box.Add(label_1, 0, wx.ALL | wx.EXPAND, 15)

        main_box = wx.BoxSizer(wx.HORIZONTAL)
        root_box.Add(main_box, 1, wx.EXPAND, 0)

        left_box = wx.BoxSizer(wx.VERTICAL)
        main_box.Add(left_box, 1, wx.EXPAND, 0)

        self.open_button = wx.Button(self.panel_1, wx.ID_ANY, u"Megnyitás")
        left_box.Add(self.open_button, 0, wx.ALL | wx.EXPAND, 6)

        self.save_button = wx.Button(self.panel_1, wx.ID_ANY, u"Mentés")
        left_box.Add(self.save_button, 0, wx.ALL | wx.EXPAND, 6)

        self.save_as_button = wx.Button(self.panel_1, wx.ID_ANY, u"Mentés másként")
        left_box.Add(self.save_as_button, 0, wx.ALL | wx.EXPAND, 6)

        self.about_button = wx.Button(self.panel_1, wx.ID_ANY, u"Névjegy")
        left_box.Add(self.about_button, 0, wx.ALL | wx.EXPAND, 6)

        self.exit_button = wx.Button(self.panel_1, wx.ID_ANY, u"Kilépés")
        left_box.Add(self.exit_button, 0, wx.ALL | wx.EXPAND, 6)

        right_box = wx.BoxSizer(wx.VERTICAL)
        main_box.Add(right_box, 2, wx.EXPAND, 0)

        self.book_list_box = wx.ListBox(self.panel_1, wx.ID_ANY, choices=[])
        right_box.Add(self.book_list_box, 1, wx.ALL | wx.EXPAND, 6)

        self.book_text_ctrl = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        right_box.Add(self.book_text_ctrl, 0, wx.ALL | wx.EXPAND, 6)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        right_box.Add(sizer_3, 1, wx.EXPAND, 0)

        self.add_button = wx.Button(self.panel_1, wx.ID_ANY, u"Hozzáad")
        sizer_3.Add(self.add_button, 0, wx.ALL, 6)

        self.delete_button = wx.Button(self.panel_1, wx.ID_ANY, u"Törlés")
        sizer_3.Add(self.delete_button, 0, wx.ALL, 6)

        self.panel_1.SetSizer(root_box)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.on_click_open_button, self.open_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_save_button, self.save_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_save_as_button, self.save_as_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_about_button, self.about_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_exit_button, self.exit_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_add_button, self.add_button)
        self.Bind(wx.EVT_BUTTON, self.on_click_delete_button, self.delete_button)
        # end wxGlade
        self.path=''
        
        self.aboutinfo = wx.adv.AboutDialogInfo()
        self.aboutinfo.SetName('Könyvtár')
        self.aboutinfo.SetVersion('1.0')
        self.aboutinfo.SetDescription('Ez egy könyvtár nyilvántartó')
        self.aboutinfo.SetLicence('GNU GPL v.2')
        self.aboutinfo.AddDeveloper('Nagy János')
        

    def on_click_open_button(self, event):  # wxGlade: MainFrame.<event_handler>
        
        fd = wx.FileDialog(self,
            message="Megnyitás",
            style=wx.FD_OPEN|wx.FD_MULTIPLE|wx.FD_CHANGE_DIR)        
        
        if fd.ShowModal()==wx.ID_OK:
            self.path = fd.GetPath()
            print(self.path)
        self.frame_statusbar.SetStatusText(self.path, 0)
        lines = self.open_file()
        self.book_list_box.Append(lines)
        event.Skip()

    def on_click_save_button(self, event):  # wxGlade: MainFrame.<event_handler>
        if self.path == '':
            if self.show_save_dialog():
                lines = self.book_list_box.GetStrings()
                self.save_file(lines)
        else:
            lines = self.book_list_box.GetStrings()
            self.save_file(lines)
        event.Skip()

    def on_click_save_as_button(self, event):  # wxGlade: MainFrame.<event_handler>
        if self.show_save_dialog():
            lines = self.book_list_box.GetStrings()
            self.save_file(lines)
        event.Skip()

    def on_click_about_button(self, event):  # wxGlade: MainFrame.<event_handler>
        wx.adv.AboutBox(self.aboutinfo)
        event.Skip()

    def on_click_exit_button(self, event):  # wxGlade: MainFrame.<event_handler>
        self.Close()
        event.Skip()

    def on_click_add_button(self, event):  # wxGlade: MainFrame.<event_handler>
        new_book = self.book_text_ctrl.GetValue()
        self.book_list_box.Append(new_book)
        self.book_text_ctrl.SetValue('')
        event.Skip()

    def show_save_dialog(self):
        fd = wx.FileDialog(
            self, message="Mentés", 
            style=wx.FD_SAVE)
        if fd.ShowModal() == wx.ID_OK:
            self.path = fd.GetPath()
            return True
        else:
            return False
       
    def save_file(self, lines):
        fp = open(self.path, 'w', encoding='utf-8')
        for line in lines:
            fp.write(line + '\n')
        fp.close()
        
    def open_file(self):
        fp = open(self.path)
        lines = fp.readlines()
        new_lines = []
        for line in lines:
            line = line.rstrip()
            new_lines.append(line)
        return new_lines;
        

    def on_click_delete_button(self, event):  # wxGlade: MainFrame.<event_handler>
        index = self.book_list_box.GetSelection()
        self.book_list_box.Delete(index)
        event.Skip()
    
# end of class MainFrame

class KonyvtarApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class KonyvtarApp

if __name__ == "__main__":
    app = KonyvtarApp(0)
    app.MainLoop()
