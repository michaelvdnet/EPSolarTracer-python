# region Types

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


class InputRegister(Register):
    pass


class HoldingRegister(Register):
    pass


class DiscreteInput(Coil):
    pass


# endregion

# region Registers
class RatedDatum(object):
    ArrayRatedVoltage = InputRegister(0x3000, "PV array rated voltage", "V", 100)
    ArrayRatedCurrent = InputRegister(0x3001, "PV array rated current", "A", 100)
    ArrayRatedPowerL = InputRegister(0x3002, "PV array rated power L", "W", 100)
    ArrayRattedPowerH = InputRegister(0x3003, "PV array rated power H", "W", 100)
    BatteryRatedVoltage = InputRegister(0x3004, "Rated voltage to battery", "v", 100)
    BatteyRatedCurrent = InputRegister(0x3005, "Rated current to battery", "A", 100)
    BatteryRatedPowerL = InputRegister(0x3006, "Rated power to battery", "W", 100)
    BatteryRatedPowerH = InputRegister(0x3007, "Rated poewe to battery", "W", 100)
    ChargingMode = InputRegister(0x3008, "0000H Connect/disconnect, 0001H PWM, 0002H MPPT", "", 1)
    RatedCurrentOfLoad = InputRegister(0x300E, "Rated current of loadf", "A", 100)

class RealtimeDatum(object):
    BatterySOC = InputRegister(0x311A, "The percentage of battery's remaining capacity", "%", 1)
    BatteryVoltage = InputRegister(0x3104, "", "V", 100)

class RealtimeStatus(object):
    pass


class StatisticalParameters(object):
    pass


class SettingParameters(object):
    pass


# endregion

# region Coils
class SwitchValues(object):
    ChargingDeviceOnOff = Coil(0, "1 Charging device on\n"
                                  "0 Charging device off")


class DescreteValues(object):
    pass

# endregion
