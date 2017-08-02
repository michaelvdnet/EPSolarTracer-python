from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer

from epsolartracer.epsolartracerclient import EPSolarTracerClient
# create a modbus client
from epsolartracer.registers import RealtimeDatum

modbusclient = ModbusTcpClient("192.168.100.111", framer=ModbusRtuFramer)
# or modbusclient = ModbusSerialClient() when using serial

# create an EPSolarTracerClient
epsolarclient = EPSolarTracerClient(modbusclient)

# in this example we'll retrieve the battery SOC
print "Retrieving battery SOC (%s)" % RealtimeDatum.BatterySOC.description

# call read_input_register
response = epsolarclient.read_input_register(RealtimeDatum.BatterySOC)

# response.success will be true if the request finished without errors, and false if not (duh)
# when response.success is true, response.value will be a (value, raw_value) tuple,
# where value is a formatted string and raw_value the object returned by pymodbus
#
# And when response.success is false response.value will contain the error message

if response.success:
    print "Battery SOC: " + response.data.value
    print "Raw value: " + response.data.raw_value.registers[0].value

else:
    print "An error occured while retrieving battery SOC (%s)" % response.data
