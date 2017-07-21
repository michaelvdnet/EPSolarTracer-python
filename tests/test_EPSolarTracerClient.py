import unittest

from pymodbus.client.sync import ModbusTcpClient, ModbusSerialClient
from pymodbus.transaction import ModbusRtuFramer

from epsolartracer.epsolartracerclient import EPSolarTracerClient

from epsolartracer.registers import RatedDatum

# noinspection PyMethodMayBeStatic
class EPSolarTracerClientTestCase(unittest.TestCase):
    def test_init_wrong_type(self):
        try:
            EPSolarTracerClient("test")
            self.fail("Constructing with wrong type should raise")
        except:
            pass

    def test_construct(self):
        EPSolarTracerClient(ModbusTcpClient("192.168.100.111", framer=ModbusRtuFramer))

    def test_read_input_register(self):
        modbusclient = ModbusTcpClient("192.168.100.111", framer=ModbusRtuFramer)

        client = EPSolarTracerClient(modbusclient)

        print client.read_input_register(RatedDatum.ArrayRatedVoltage)