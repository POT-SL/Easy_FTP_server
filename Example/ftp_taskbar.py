from pystray import Icon
from PIL import Image
from pystray import MenuItem

def all_closed(icon):
    setting_signal.put({'type': 'close'})
    icon.stop()

def opengui():
    setting_signal.put({'type': 'opengui'})

def taskbar_main(que):

    global setting_signal
    setting_signal = que

    menu = (
        MenuItem('打开主界面', action=opengui),
        MenuItem('退出', action=all_closed),
    )
    icon = Icon("name", Image.open(".\\config\\0.ico"), "ftp服务器", menu)
    icon.run()