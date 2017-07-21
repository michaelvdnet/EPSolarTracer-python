import unittest

from pymodbus.client.sync import ModbusTcpClient

from epsolartracer.EPSolarTracerClient import EPSolarTracerClient


class EPSolarTracerClientTestCase(unittest.TestCase):
    def test_init_wrong_type(self):
        try:
            EPSolarTracerClient("test")
            self.fail("Constructing with wrong type should raise")
        except:
            pass

    def test_construct(self):

        client = EPSolarTracerClient(ModbusTcpClient("192.168.100.111"))