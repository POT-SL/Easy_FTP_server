import pystray
from PIL import Image
from pystray import MenuItem
from sys import exit

def all_closed(icon):
    settings_signal.put({'type': 'closeall'})
    icon.stop()

def opengui():
    settings_signal.put({'type': 'opengui'})


def taskbat_main(signal_l):

    global settings_signal
    settings_signal = signal_l

    menu = (
        MenuItem('打开主界面', action=opengui),
        MenuItem('退出', action=all_closed),
    )
    icon = pystray.Icon("name", Image.open("icon\\ico.ico"), "ftp服务器", menu)
    icon.run()