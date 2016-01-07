"""
Compatibility code to run with different versions of wxPython

@copyright: 2013-2016 Carsten Grohmann
@license: MIT (see LICENSE.txt) - THIS PROGRAM COMES WITH NO WARRANTY
"""

import wx


SizerItem_SetWindow = None
GridSizer_GetRows = None
GridSizer_GetCols = None

def SizerItem_AssignWindow(item, window):
    """
    Wrapper for wxSizerItem.SetWindow() resp. wxSizerItem.AssignWindow()

    wxSizerItem.SetWindow() is deprecated since wxPython 2.9 use
    wxSizerItem.AssignWindow() instead.

    Depending on the wxPython version L{SizerItem_SetWindow28()} or
    L{SizerItem_AssignWindow()} will be used.

    @param item:   Instance of wxSizerItem
    @param window: Instance of wxWindow

    @see: L{SizerItem_SetWindow()}
    @see: L{SizerItem_SetWindow28()}
    @see: L{SizerItem_AssignWindow()}
    """
    item.AssignWindow(window)


def SizerItem_SetWindow28(item, window):
    """
    Wrapper for wxSizerItem.SetWindow() resp. wxSizerItem.AssignWindow()

    wxSizerItem.SetWindow() is deprecated since wxPython 2.9 use
    wxSizerItem.AssignWindow() instead.

    Depending on the wxPython version L{SizerItem_SetWindow28()} or
    L{SizerItem_AssignWindow()} will be used.

    @param item:   Instance of wxSizerItem
    @param window: Instance of wxWindow

    @see: L{SizerItem_SetWindow()}
    @see: L{SizerItem_SetWindow28()}
    @see: L{SizerItem_AssignWindow()}
    """
    item.SetWindow(window)


def SizerItem_SetSizer(item, sizer):
    """
    Wrapper for wxSizerItem.SetSizer() resp. wxSizerItem.AssignSizer()

    wxSizerItem.SetSizer() is deprecated since wxPython 2.9 use
    wxSizerItem.AssignSizer() instead.

    @param item:  Instance of wxSizerItem
    @param sizer: Instance of wxSizer
    """
#    if hasattr(item, 'AssignSizer'):
#        item.AssignSizer(sizer)
#    else:
    item.SetSizer(sizer)


def GridSizer_GetRows28(sizer):
    """
    Wrapper for wxGridSizer.GetRows()

    With wx3 wxGridSizer.GetRows() and wxGridSizer.GetCols() "returns zero
    if the sizer is automatically adjusting the number of rows depending
    on number of its children."

    @param sizer: Instance of wxGridSizer or a derived class
    @return: Number of rows specified for this sizer
    @rtype:  int
    """
    return sizer.GetRows()


def GridSizer_GetRows3(sizer):
    """
    Wrapper for wxGridSizer.GetRows()

    With wx3 wxGridSizer.GetRows() and wxGridSizer.GetCols() "returns zero
    if the sizer is automatically adjusting the number of rows depending
    on number of its children."

    @param sizer: Instance of wxGridSizer or a derived class
    @return: Number of rows specified for this sizer
    @rtype:  int
    """
    return sizer.GetEffectiveRowsCount()


def GridSizer_GetCols28(sizer):
    """
    Wrapper for wxGridSizer.GetColws()

    With wx3 wxGridSizer.GetRows() and wxGridSizer.GetCols() "returns zero
    if the sizer is automatically adjusting the number of rows depending
    on number of its children."

    @param sizer: Instance of wxGridSizer or a derived class
    @return: Number of columns specified for this sizer
    @rtype:  int
    """
    return sizer.GetCols()


def GridSizer_GetCols3(sizer):
    """
    Wrapper for wxGridSizer.GetColws()

    With wx3 wxGridSizer.GetRows() and wxGridSizer.GetCols() "returns zero
    if the sizer is automatically adjusting the number of rows depending
    on number of its children."

    @param sizer: Instance of wxGridSizer or a derived class
    @return: Number of columns specified for this sizer
    @rtype:  int
    """
    return sizer.GetEffectiveColsCount()


# Set different functions depending on the active wxPython version
if wx.VERSION[:2] >= (2, 9):
    SizerItem_SetWindow = SizerItem_AssignWindow
    GridSizer_GetRows = GridSizer_GetRows3
    GridSizer_GetCols = GridSizer_GetCols3
else:
    SizerItem_SetWindow = SizerItem_SetWindow28
    GridSizer_GetRows = GridSizer_GetRows28
    GridSizer_GetCols = GridSizer_GetCols28
