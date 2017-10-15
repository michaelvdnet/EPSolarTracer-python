from pymodbus.client.sync import BaseModbusClient
from pymodbus.register_read_message import *
from pymodbus.transaction import ModbusRtuFramer

from epsolartracer.registers import InputRegister, HoldingRegister


class Response(object):
    def __init__(self, success, data):
        self.success = success
        self.data = data


class DataResponse(object):
    def __init__(self, value, raw_value, unit):
        # type: (float, float, str) -> None
        self.unit = unit
        self.value = value
        self.raw_value = raw_value

    def __str__(self):
        return str(self.value) + self.unit


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

        raw_response = self.modbusclient.read_input_registers(input_register.address,
                                                              unit=self.unit)
        raw_value = raw_response.registers[0].value

        if isinstance(raw_response, ReadInputRegistersResponse):
            value = float(raw_value.registers[0]) / input_register.times
            response = Response(True, DataResponse(value, raw_value, input_register.unit))
        else:
            response = Response(False, raw_value.string)
        return response

    def read_holding_register(self, holding_register):
        # type: (HoldingRegister) -> Response

        if not isinstance(holding_register, HoldingRegister):
            raise TypeError("1st argument must be a holding register")

        raw_response = self.modbusclient.read_holding_registers(holding_register.address,
                                                                unit=self.unit)
        raw_value = raw_response.registers[0].value

        if isinstance(raw_response, ReadHoldingRegistersResponse):
            value = float(raw_response.registers[0]) / holding_register.times
            response = Response(True, DataResponse(value, raw_value, holding_register.unit))

        else:
            response = Response(False, raw_response.string)
        return response

    def write_holding_register(self, holding_register, value):
        # type: (HoldingRegister) -> None

        if not isinstance(holding_register, HoldingRegister):
            raise TypeError("1st argument must be a holding register")

        self.modbusclient.write_register(holding_register, value, unit=self.unit)
