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
    BatteryRatedVoltage = InputRegister(0x3004, "Rated voltage to battery", "V", 100)
    BatteyRatedCurrent = InputRegister(0x3005, "Rated current to battery", "A", 100)
    BatteryRatedPowerL = InputRegister(0x3006, "Rated power to battery", "W", 100)
    BatteryRatedPowerH = InputRegister(0x3007, "Rated power to battery", "W", 100)
    ChargingMode = InputRegister(0x3008, "0000H Connect/disconnect, 0001H PWM, 0002H MPPT", "", 1)
    RatedCurrentOfLoad = InputRegister(0x300E, "Rated current of load", "A", 100)


class RealtimeDatum(object):
    PvArrayInputVoltage = InputRegister(0x3100, "Solar charge controller--PV array voltage", "V", 100)
    PvArrayInputCurrent = InputRegister(0x3101, "Solar charge controller--PV array Current", "A", 100)
    PvArrayInputPowerL = InputRegister(0x3102, "Solar charge controller--PV array Power", "W", 100)
    PvArrayInputPowerH = InputRegister(0x3103, "Solar charge controller--PV array Powe", "W", 100)
    BatteryVoltage = InputRegister(0x3104, "Battery Voltage", "V", 100)
    BatteryPowerL = InputRegister(0x3106, "Battery charging Power", "W", 100)
    BatteryPowerH = InputRegister(0x3107, "Battery charging Power", "W", 100)
    LoadVoltage = InputRegister(0x310C, "Load Voltage", "V", 100)
    LoadCurrent = InputRegister(0x310D, "Load Current", "A", 100)
    LoadPowerL = InputRegister(0x310E, "Load power", "W", 100)
    LoadPowerH = InputRegister(0x310F, "Load power", "W", 100)
    BatteryTemperature = InputRegister(0x3110, "Battery Temperature", "C", 100)
    TemperatureInsiteEquipment = InputRegister(0x3111, "Temperature insite case", "C", 100)
    BatterySOC = InputRegister(0x311A, "The percentage of battery's remaining capacity", "%", 1)
    RemoteBatteryTemperature = InputRegister(0x311B, "The batery tempereture measured by remote temperature sensor", "C", 100)
    BatteryRealRatedPower = InputRegister(0x311D, "Current system rated voltage 1200=12V", "VA", 100)



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
