#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 928d1e45e6a1+ on Tue May 24 06:45:37 2016
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Frame186(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Frame186.__init__
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.Bug186_Frame_menubar = wx.MenuBar()
        global myMagicMenu; myMagicMenu = wx.NewId()
        self.File = wx.Menu()
        self.File.Append(myMagicMenu, _("Magic"), "")
        self.Bug186_Frame_menubar.Append(self.File, _("File"))
        self.SetMenuBar(self.Bug186_Frame_menubar)
        # Menu Bar end
        
        # Tool Bar
        self.Bug186_Frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.Bug186_Frame_toolbar)
        global myMagicTool; myMagicTool = wx.NewId()
        self.Bug186_Frame_toolbar.AddLabelTool(myMagicTool, _("Magic"), wx.EmptyBitmap(32, 32), wx.NullBitmap, wx.ITEM_NORMAL, _("Do a MAGIC action"), _("It's really MAGIC"))
        # Tool Bar end
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, _("Id: automatic (default behaviour)"))
        self.text_ctrl_2 = wx.TextCtrl(self, 12123, _("Id: numeric value \"12123\""))
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, _("Id: predefined identify: \"wxID_ANY\""))
        global myButtonId; myButtonId = wx.NewId()
        self.text_ctrl_4 = wx.TextCtrl(self, myButtonId, _("Id: variable assignment \"myButtonId=?\""))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Frame186.__set_properties
        self.SetTitle(_("frame_1"))
        self.SetSize((300, 300))
        self.Bug186_Frame_toolbar.Realize()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Frame186.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.text_ctrl_1, 1, wx.ALL | wx.EXPAND, 5)
        sizer_2.Add(self.text_ctrl_2, 1, wx.ALL | wx.EXPAND, 5)
        sizer_2.Add(self.text_ctrl_3, 1, wx.ALL | wx.EXPAND, 5)
        sizer_2.Add(self.text_ctrl_4, 1, wx.ALL | wx.EXPAND, 5)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.SetSize((300, 300))
        # end wxGlade

# end of class Frame186
class MyApp(wx.App):
    def OnInit(self):
        Bug186_Frame = Frame186(None, wx.ID_ANY, "")
        self.SetTopWindow(Bug186_Frame)
        Bug186_Frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()
