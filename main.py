import logging
import GUI
#import motor_control
import scope_communication

# Setup logging
logging.basicConfig(filename='log.txt', format='%(asctime)s %(message)s', datefmt='%I:%M:%S', filemode='w', level=logging.DEBUG)

def main():
    # Setup logging
    logging.basicConfig(filename='log.txt', format='%(asctime)s %(message)s', datefmt='%I:%M:%S', filemode='w', level=logging.DEBUG)
    
    # Launch GUI
    GUI.launch_GUI()
    
if __name__ == '__main__':
    main()