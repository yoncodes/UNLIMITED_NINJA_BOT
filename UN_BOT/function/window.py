# coding: utf-8

import re, traceback
import win32gui, win32con, win32com.client,win32process
from win32api import GetSystemMetrics



class Window:
    """Encapsulates some calls to the winapi for window management"""
    def __init__ (self):
        """Constructor"""
        self._handle = None
        self.shell = win32com.client.Dispatch("WScript.Shell")

    def find_window(self, class_name, window_name = None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

    def set_window_pos(self, x_axis, y_axis, size_x, size_y ):
    	win32gui.ShowWindow(self._handle, win32con.SW_RESTORE)
    	#win32gui.SetWindowPos(self._handle, win32con.HWND_TOPMOST,x_axis, y_axis, size_y, size_y, 0)

    def move_window(self, x_axis, y_axis, size_x, size_y):
        win32gui.ShowWindow(self._handle, win32con.SW_RESTORE)
        win32gui.MoveWindow(self._handle,x_axis, y_axis, size_x, size_y, True)

    def get_window_pid(self,title):
        hwnd = self.find_window_wildcard(title)
        threadid,pid = win32process.GetWindowThreadProcessId(hwnd)
        return pid

    def return_hwnd(self):
        return self._handle

    def set_up(self, platform):


        if platform == "joyfun":
            title = ".*Unlimited Ninja - .*"

        elif platform == "fb":
            title = "Ninja World"

        
        self.find_window_wildcard(title)

        self.set_foreground()

        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)

        window_width = 1298
        window_height = 850

        x = (screen_width / 2) - (window_width / 2) 
        y = (screen_height / 2) - (window_height / 2)

        self.move_window(x,y,window_width,window_height)
