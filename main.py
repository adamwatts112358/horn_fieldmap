import sys
import logging
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import motor_control
import scope_communication

# Add: display positions on GUI
# Add: bring together all modules
# Add scan inputs to GUI
# Make scan GUI load defaults from config file
# Make input from GUI change params
# Add: saving numpy files for data https://stackoverflow.com/questions/30376581/save-numpy-array-in-append-mode

def log_message(logfile, log_window, message):
    ''' Log message and timestamp to both GUI log window and log file. '''
    logging.info(message)
    with open(logfile, 'r') as f:
        text=f.read()
        log_window.setText(text)
    log_window.moveCursor(QTextCursor.End)

def dir_button_pressed(logfile, log_window, d):
    if d is 'up':
        log_message(logfile, log_window, 'Moving up (+Y)')
    elif d is 'down':
        log_message(logfile, log_window, 'Moving down (-Y)')
    elif d is 'left':
        log_message(logfile, log_window, 'Moving left (-X)')
    elif d is 'right':
        log_message(logfile, log_window, 'Moving right (+X)')
    elif d is 'forward':
        log_message(logfile, log_window, 'Moving forward (+Z)')
    elif d is 'back':
        log_message(logfile, log_window, 'Moving back (-Z)')

if __name__ == '__main__':
    # Setup logging
    logfile = 'log.txt'
    logging.basicConfig(filename=logfile, format='%(asctime)s %(message)s', datefmt='%I:%M:%S', filemode='w', level=logging.DEBUG)
    
    # Setup GUI
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('GUI Test')
    grid = QGridLayout(window)
    
    # Log output window
    log_window = QTextEdit(window)
    log_window.setReadOnly(True)
    log_window.setLineWrapMode(QTextEdit.NoWrap)
    font = log_window.font()
    font.setFamily("Courier")
    font.setPointSize(10)
    grid.addWidget(log_window,7,0,1,3)
    log_message(logfile, log_window, 'Initalized.')
    
    # Setup buttons
    u_button = QPushButton('Up')
    grid.addWidget(u_button,0,0,1,3)
    u_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'up'))
    d_button = QPushButton('Down')
    grid.addWidget(d_button,1,0,1,3)
    d_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'down'))
    l_button = QPushButton('Left')
    grid.addWidget(l_button,2,0,2,1)
    l_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'left'))
    r_button = QPushButton('Right')
    grid.addWidget(r_button,2,2,2,1)
    r_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'right'))
    f_button = QPushButton('Forward')
    grid.addWidget(f_button,2,1)
    f_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'forward'))
    b_button = QPushButton('Back')
    grid.addWidget(b_button,3,1)
    b_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'back'))
    
    window.setLayout(grid)
    window.show()
    sys.exit(app.exec_())
