class InputRegister(object):
    pass


class HoldingRegister(object):
    pass


class _Coil(object):
    pass


class DiscreteInput(object):
    pass


class Register(object):
    """
    Defines a register
    """

    def __init__(self, address, description, unit, times):
        """
        Constructor
        :param address: Address of the register
        :param description: Description given in the documentation
        :param unit: Unit the returned value is in
        :param times: Multiplication factor
        """
        self.times = times
        self.unit = unit
        self.description = description
        self.address = address


class Coil(object):
    """
    Defines a coil
    """

    def __init__(self, address, description):
        """
        Constructor
        :param address: Address of the coil
        :param description: Description given in the documentation
        """
        self.address = address
        self.description = description


# region registers
class RatedDatum(InputRegister):
    ArrayRatedVoltage = Register(0x3000, "PV array rated voltage", "V", 100)


class RealtimeDatum(InputRegister):
    pass


class RealtimeStatus(InputRegister):
    pass


class StatisticalParameters(InputRegister):
    pass


class SettingParameters(HoldingRegister):
    pass


# endregion
# region coils
class SwitchValues(_Coil):
    ChargingDeviceOnOff = Coil(0, "1 Charging device on\n"
                                  "0 Charging device off")


class DescreteValues(DiscreteInput):
    pass

# endregion
