# PyVISA
GPIB Operate Scientific Instruments for Keithley 2410


# Keithley 2410 Source Meter commands

### Calibration unlocked states


| Mode State  | Equivalent remote command |
| ----------- | ----------- | ----------- |
| Concurrent Functions = OFF       | :SENS:FUNC:CONC OFF                  |
| Sense Function = Source          | :SENS:FUNC <source_ function>        |
| Sense Volts NPLC = 1.0           | :SENS:VOLT:NPLC 1.0                  |
| Sense Volts Range = Source V     | :SENS:VOLT:RANG <source_V_range>     |
| Sense Current NPLC = 1.0         | :SENS:CURR:NPLC 1.0                  |
| Sense Current Range = Source I   | :SENS:CURR:RANG <source_ I_ range>   |
| Filter Count = 10                | :SENS:AVER:COUN 10                   |
| Filter Control = REPEAT          | :SENS:AVER:TCON REPeat               |
| Filter Averaging = ON            | :SENS:AVER:STAT ON                   |
| Source V Mode = FIXED            | :SOUR:VOLT:MODE FIXED                |
| Volts Autorange = OFF            | :VOLT:RANG:AUTO OFF                  |
| Source I Mode = FIXED            | :SOUR:CURR:MODE FIXED                |
| Current Autorange = OFF          | :SOUR:CURR:RANG:AUTO OFF             |
| Autozero = ON                    | :SYST:AZERO ON                       |
| Trigger Arm Count = 1            | :ARM:COUNT 1                         |
| Trigger Arm Source = Immediate   | :ARM:SOUR IMMediate                  |
| Trigger Count = 1                | :TRIG:COUNT 1                        |
| Trigger Source = Immediate       | :TRIG:SOUR IMMediate                 |
