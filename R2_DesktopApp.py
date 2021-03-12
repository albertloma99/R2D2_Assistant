import subprocess

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Adding an icon
icon = QIcon("icon.png")

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creating the options
menu = QMenu()
option1 = QAction("Odio la arena")
option2 = QAction("General Kenobi")
menu.addAction(option1)
menu.addAction(option2)

# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Adding options to the System Tray
tray.setContextMenu(menu)

subprocess.Popen("python SpeechRecognitionV3.py")
app.exec_()