from pymodbus.client.sync import BaseModbusClient
from pymodbus.transaction import ModbusRtuFramer


class EPSolarTracerClient(object):
    def __init__(self, modbusclient):
        # type: (BaseModbusClient) -> None

        # Type validation
        if not isinstance(modbusclient, BaseModbusClient):
            raise TypeError("1st argument should be a valid ModbusClient")

        # Change framer to the RTU Framer (The tracer responds back in RTU even when requesting in TCP)
        modbusclient.framer = ModbusRtuFramer

