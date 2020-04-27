import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QTextEdit
from time import gmtime, strftime

# Add: display positions on GUI
# Add: bring together all modules
# Add scan inputs to GUI
# Make scan GUI load defaults from config file
# Make input from GUI change params
# Add: saving numpy files for data https://stackoverflow.com/questions/30376581/save-numpy-array-in-append-mode

def log_message(logOutput, message):
    ''' Log message and timestamp to both GUI log window and log file. '''
    time = strftime("%H:%M:%S", gmtime())
    logOutput.append('[{}] {}'.format(time, message))
    logging.info(message)
    # Append to log text file

def dir_button_pressed(logOutput, d):
    if d is 'up':
        log_message(logOutput, 'Moving up (+Y)')
    elif d is 'down':
        log_message(logOutput, 'Moving down (-Y)')
    elif d is 'left':
        log_message(logOutput, 'Moving left (-X)')
    elif d is 'right':
        log_message(logOutput, 'Moving right (+X)')
    elif d is 'forward':
        log_message(logOutput, 'Moving forward (+Z)')
    elif d is 'back':
        log_message(logOutput, 'Moving back (-Z)')

def launch_GUI():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('GUI Test')
    grid = QGridLayout(window)
    
    # Log output window
    logOutput = QTextEdit(window)
    logOutput.setReadOnly(True)
    logOutput.setLineWrapMode(QTextEdit.NoWrap)
    font = logOutput.font()
    font.setFamily("Courier")
    font.setPointSize(10)
    grid.addWidget(logOutput,7,0,1,3)
    log_message(logOutput, 'Initalized.')
    
    # Setup buttons
    u_button = QPushButton('Up')
    grid.addWidget(u_button,0,0,1,3)
    u_button.clicked.connect(lambda: dir_button_pressed(logOutput, 'up'))
    d_button = QPushButton('Down')
    grid.addWidget(d_button,1,0,1,3)
    d_button.clicked.connect(lambda: dir_button_pressed(logOutput, 'down'))
    l_button = QPushButton('Left')
    grid.addWidget(l_button,2,0,2,1)
    l_button.clicked.connect(lambda: dir_button_pressed(logOutput, 'left'))
    r_button = QPushButton('Right')
    grid.addWidget(r_button,2,2,2,1)
    r_button.clicked.connect(lambda: dir_button_pressed(logOutput, 'right'))
    f_button = QPushButton('Forward')
    grid.addWidget(f_button,2,1)
    f_button.clicked.connect(lambda: dir_button_pressed(logOutput, 'forward'))
    b_button = QPushButton('Back')
    grid.addWidget(b_button,3,1)
    b_button.clicked.connect(lambda: dir_button_pressed(logOutput, 'back'))
    
    window.setLayout(grid)
    window.show()
    sys.exit(app.exec_())