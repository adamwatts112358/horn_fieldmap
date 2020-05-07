import sys
import logging
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5 import *

import motor_control
import scope_communication

# Make window setups their own functions?
# May need a "refresh status" function that re-checks subsystems to update status display (periodically?)
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
    
    main_window = QMainWindow()
    main_window.setFixedSize(800,600)
    main_window.setWindowTitle('NuMI horn field-mapping system')
    
    window = QWidget()
    window_layout = QGridLayout()
    window.setLayout(window_layout)
    
    control_window = QWidget()
    control_layout = QHBoxLayout()
    control_window.setLayout(control_layout)
    
    control_buttons = QWidget()
    control_grid = QGridLayout()
    control_buttons.setLayout(control_grid)
    control_layout.addWidget(control_buttons)
    
    readout = QTextEdit()
    # Temporary variable for designing layout
    oscope_status = "OK"
    probe_status = "OK"
    motor_status = "Failed"
    
    green = '#78BE20'
    red = '#AF272F'
    
    if oscope_status is "OK":
        oscope_status_color = green
    else:
        oscope_status_color = red
        
    if probe_status is "OK":
        probe_status_color = green
    else:
        probe_status_color = red
        
    if motor_status is "OK":
        motor_status_color = green
    else:
        motor_status_color = red
    
    x_pos = 0.0
    y_pos = 0.0
    z_pos = 10.0
    readout_text = '''
    <body style="background-color:#f2f2f2;">
    <center>
    <table cellpadding=10>
        <tr><td style="text-align: center;"><h2>Subsystem Status Checks</h2></td></tr>
    </table>
    <table border cellpadding=10>
        <tr><td style="text-align: center; background-color:{}">Oscilloscopes: <b>{}</b></td></tr>
        <tr><td style="text-align: center; background-color:{}">Magnetic field probe: <b>{}</b></td></tr>
        <tr><td style="text-align: center; background-color:{}">Stepper motor controllers: <b>{}</b></td></tr>
    </table>
    <p>&nbsp;</p>
    <font size=4>
    <table cellpadding=10>
        <tr><td colspan=2 style="text-align: center;"><h2>Live Position Readings</h2></td></tr>
        <tr>
            <td style="text-align: center;">X-axis</td>
            <td style="text-align: center;">{}</td>
        </tr>
        <tr>
            <td style="text-align: center;">Y-axis</td>
            <td style="text-align: center;">{}</td>
        </tr>
        <tr>
            <td style="text-align: center;">Z-axis</td>
            <td style="text-align: center;">{}</td>
        </tr>
    </table>
    </font>
    </center>
    </body>
    '''.format(oscope_status_color, oscope_status, probe_status_color, probe_status, motor_status_color, motor_status, x_pos, y_pos, z_pos)
    readout.setText(readout_text)
    
    
    control_layout.addWidget(readout)
    
    cal_window = QWidget()
    DAQ_window = QWidget()
    scan_window = QWidget()
    
    # Main menubar
    menubar = main_window.menuBar()
    file_menu = menubar.addMenu('File')
    
    exit_act = QAction('Exit', window)        
    exit_act.triggered.connect(qApp.quit)
    file_menu.addAction(exit_act)
    
    # Initialize tabs
    tabs = QTabWidget()
    tabs.addTab(control_window,"Control")
    tabs.addTab(cal_window,"Calibration")
    tabs.addTab(DAQ_window,"DAQ")
    tabs.addTab(scan_window,"Scan")
    
    # Log output window
    log_window = QTextEdit(window)
    log_window.setReadOnly(True)
    log_window.setLineWrapMode(QTextEdit.NoWrap)
    font = log_window.font()
    font.setFamily("Courier")
    font.setPointSize(10)
    
    # Setup buttons
    u_button = QPushButton('Up')
    control_grid.addWidget(u_button,0,0,1,3)
    u_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'up'))
    d_button = QPushButton('Down')
    control_grid.addWidget(d_button,1,0,1,3)
    d_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'down'))
    l_button = QPushButton('Left')
    control_grid.addWidget(l_button,2,0,2,1)
    l_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'left'))
    r_button = QPushButton('Right')
    control_grid.addWidget(r_button,2,2,2,1)
    r_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'right'))
    f_button = QPushButton('Forward')
    control_grid.addWidget(f_button,2,1)
    f_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'forward'))
    b_button = QPushButton('Back')
    control_grid.addWidget(b_button,3,1)
    b_button.clicked.connect(lambda: dir_button_pressed(logfile, log_window, 'back'))
    
    window_layout.setRowStretch(0, 3)
    window_layout.addWidget(tabs,0,0)
    window_layout.setRowStretch(1, 1)
    window_layout.addWidget(log_window,1,0)
    
    main_window.setCentralWidget(window)
    main_window.show()
    log_message(logfile, log_window, 'Program initalized.')
    sys.exit(app.exec_())
