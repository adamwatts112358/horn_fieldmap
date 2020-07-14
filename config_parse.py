import configparser

# https://wiki.python.org/moin/ConfigParserExamples

config = configparser.ConfigParser()
config.read("config.ini")

def get_scope_params():
    scope_A = {}
    scope_A['Type'] = config.get('Scope A', 'Type')
    scope_A['IP'] = config.get('Scope A', 'IP')
    
    scope_B = {}
    scope_B['Type'] = config.get('Scope B', 'Type')
    scope_B['IP'] = config.get('Scope B', 'IP')
    
    return scope_A, scope_B
    
def get_BB_params():
    BB = {}
    BB['IP'] = config.get('BeagleBone', 'IP')
    # Get pin configurations
    BB['trigger'] = config.get('BeagleBone', 'Trigger')
    BB['A step'] = config.get('BeagleBone', 'MotorA_step')
    BB['A dir'] = config.get('BeagleBone', 'MotorA_dir')
    BB['B step'] = config.get('BeagleBone', 'MotorB_step')
    BB['B dir'] = config.get('BeagleBone', 'MotorB_dir')
    BB['C step'] = config.get('BeagleBone', 'MotorC_step')
    BB['C dir'] = config.get('BeagleBone', 'MotorC_dir')
    BB['X-axis'] = config.get('BeagleBone', 'X-axis')
    BB['Y-axis'] = config.get('BeagleBone', 'Y-axis')
    BB['Z-axis'] = config.get('BeagleBone', 'Z-axis')
    
    return BB