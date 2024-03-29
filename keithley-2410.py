import pyvisa
rm = pyvisa.ResourceManager('@py')
print(rm.list_resources()) # rm.list_resources() is a tuple

GPIB_A = 'GPIB0::3::INSTR'
GPIB_B = 'GPIB0::6::INSTR'

def Instrument_Info_Query(rm, instrument_name):
    #---------- get info about GPIB: “what are you?” using Query
    instrument_handler = rm.open_resource(instrument_name)
    instrument_handler.read_termination = '\n'
    instrument_handler.write_termination = '\n'
    instrument_info = instrument_handler.query("*IDN?")
    return(instrument_info)

def Instrument_Info_Write_Read(rm, instrument_name):
    #---------- get info about GPIB: “what are you?” using Read & Write
    instrument_handler = rm.open_resource(instrument_name)
    instrument_handler.read_termination = '\n'
    instrument_handler.write_termination = '\n'
    instrument_handler.write('*IDN?')
    instrument_info = instrument_handler.read()
    return(instrument_info)

instrument_info_GPIB_A =  Instrument_Info_Query(rm, GPIB_A)
print(instrument_info_GPIB_A)
print("----------")
instrument_info_GPIB_A =  Instrument_Info_Write_Read(rm, GPIB_A)
print(instrument_info_GPIB_A)


def Instrument_Measure_Voltage(rm,instrument_name):
    instrument_handler = rm.open_resource(instrument_name)
    #instrument_handler.read_termination = '\n'
    #instrument_handler.write_termination = '\n'
    instrument_handler.write(":SOUR:FUNC VOLT") #set source function to volts
    instrument_handler.write(":SENS:FUNC 'CURR:DC'") #set sense function to current
    instrument_handler.write(":SENS:CURR:PROT 1E-5") #set compliance to 10 micro amps
    instrument_handler.write(":SOUR:VOLT:START 0") #set start voltage to 0
    instrument_handler.write(":SOUR:VOLT:STOP 10") #set end voltage to 10 V
    instrument_handler.write(":SOUR:VOLT:STEP 1") #set voltage step size to 1 V
    instrument_handler.write(":SOUR:VOLT:MODE SWE") #select voltage sweep mode
    instrument_handler.write(":SOUR:SWE:RANG AUTO") #Auto range source
    instrument_handler.write(":SOUR:SWE:SPAC LIN") #Select linear staircase sweep
    instrument_handler.write(":TRIG:COUN 10") # Trigger count = # sweep points - = (stop-start) / step+1
    instrument_handler.write(":SOUR:DEL 0.1") #100 ms source delay
    instrument_handler.write(":OUTP ON") #turn on output
    voltages = instrument_handler.query(":READ?") #trigger sweep and request data
    instrument_handler.write(":OUTP OFF") #turn output off
    instrument_handler.query("status:measurement?")
    instrument_handler.write("trace:clear; trace:feed:control next")
    return(voltages)

voltages = Instrument_Measure_Voltage(rm, GPIB_A)
print(voltages)
