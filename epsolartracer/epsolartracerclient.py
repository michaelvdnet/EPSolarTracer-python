from pymodbus.client.sync import BaseModbusClient
from pymodbus.register_read_message import *
from pymodbus.transaction import ModbusRtuFramer

from epsolartracer.registers import InputRegister, HoldingRegister


class Response(object):
    def __init__(self, success, data):
        self.success = success
        self.data = data


class DataResponse(object):
    def __init__(self, value, raw_value):
        self.value = value
        self.raw_value = raw_value


class EPSolarTracerClient(object):
    def __init__(self, modbusclient, unit=1):
        # type: (BaseModbusClient, int) -> None

        # Type validation
        if not isinstance(modbusclient, BaseModbusClient):
            raise TypeError("1st argument must be a valid ModbusClient")

        if not isinstance(unit, int):
            raise TypeError("2nd argument must be a integer")

        # Check if framer is RTU framer
        if not isinstance(modbusclient.framer, ModbusRtuFramer):
            raise RuntimeError("The ModbusClient's framer must be ModbusRtuFramer.")

        self.modbusclient = modbusclient
        self.unit = unit

    def read_input_register(self, input_register):
        # type: (InputRegister) -> Response

        if not isinstance(input_register, InputRegister):
            raise TypeError("1st argument must be an input register")

        raw_value = self.modbusclient.read_input_registers(input_register.address, unit=self.unit)

        if isinstance(raw_value, ReadInputRegistersResponse):
            value = "" + str(float(raw_value.registers[0]) / input_register.times) + input_register.unit
            response = Response(True, DataResponse(value, raw_value))
        else:
            response = Response(False, raw_value.string)
        return response

    def read_holding_register(self, holding_register):
        # type: (HoldingRegister) -> Response

        if not isinstance(holding_register, HoldingRegister):
            raise TypeError("1st argument must be a holding register")

        raw_value = self.modbusclient.read_holding_registers(holding_register.address, unit=self.unit)

        if isinstance(raw_value, ReadHoldingRegistersResponse):
            value = "" + str(float(raw_value.registers[0]) / holding_register.times) + holding_register.unit
            response = Response(True, DataResponse(value, raw_value))

        else:
            response = Response(False, raw_value.string)
        return response

