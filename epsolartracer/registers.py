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
    BatteryStatus = InputRegister(0x3200, "D3-D0: 01H Overvolt , 00H Normal , 02H Under Volt, 03H Low Volt Disconnect, 04H Fault D7-D4: 00H Normal, 01H Over Temp.(Higher than the warning settings), 02H Low Temp.(Lower than the warning settings), D8: Battery inner resistance abnormal 1, normal 0 D15: 1-Wrong identification for rated voltage", "", 1)
    ChargingEquipmentStatus = InputRegister(0x3201, "D15-D14: Input volt status. 00 normal, 01 no power connected, 02H Higher volt input, 03H Input volt error. D13: Charging MOSFET is short. D12: Charging or Anti-reverse MOSFET is short. D11: Anti-reverse MOSFET is short. D10: Input is over current. D9: The load is Over current. D8: The load is short. D7: Load MOSFET is short. D4: PV Input is short. D3-2: Charging status. 00 No charging,01 Float,02 Boost, 03 Equalization. D1: 0 Normal, 1 Fault. D0: 1 Running, 0 Standby.", "", 1)
    DischargeEquipmentStatus = InputRegister(0x3202, "D15-D14: 00H normal, 01H low, 02H High, 03H no access Input volt error. D13-D12: output power:00-light load,01-moderate,02-rated,03-overlo ad D11: short circuit D10: unable to discharge D9: unable to stop discharging D8: output voltage abnormal D7: input overpressure D6: high voltage side short circuit D5: boost overpressure D4: output overpressure D1: 0 Normal, 1 Fault. D0: 1 Running, 0 Standby", "", 1)


class StatisticalParameters(object):
    MaximumPVVoltageToday = InputRegister(0x3300, "00: 00 Refresh every day", "V", 100)
    MinimunPVVoltageToday = InputRegister(0x3301, "00: 00 Refresh every day", "V", 100)
    MaximumBatteryVoltageToday = InputRegister(0x3302, "00: 00 Refresh every day", "V", 100)
    MinimumBatteryVoltageToday = InputRegister(0x3303, "00: 00 Refresh every day", "V", 100)
    ConsumedEnergyTodayL = InputRegister(0x3304, "00: 00 Clear every day", "KWH", 100)
    ConsumedEnergyTodayH = InputRegister(0x3305, "00: 00 Clear every day", "KWH", 100)
    ConsumedEnergyMonthL = InputRegister(0x3306, "00: 00 Clear on the first day of month", "KWH" ,100)
    ConsumedEnergyMonthH = InputRegister(0x3307, "00: 00 Clear on the first day of month", "KWH", 100)
    ConsumedEnergyYearL = InputRegister(0x3308, "00: Clear on 1, Jan", "KWH", 100)
    ConsumedEnergyYearH = InputRegister(0x3309, "00: Clear on 1, Jan", "KWH", 100)
    TotalConsumedEnergyL = InputRegister(0x330A, "", "KWH", 100)
    TotalConsumedEnergyH = InputRegister(0x330B, "", "KWH", 100)
    GeneratedEnergyTodayL = InputRegister(0x330C, "00: 00 Clear every day", "KWH", 100)
    GeneratedEnergyTodayH = InputRegister(0x330D, "00: 00 Clear every day", "KWH", 100)
    GeneratedEnergyMonthL = InputRegister(0x330E, "00: 00 Clear on the first day of month", "KWH", 100)
    GeneratedEnergyMonthH = InputRegister(0x330F, "00: 00 Clear on the first day of month", "KWH", 100)
    GeneratedEnergyYearL = InputRegister(0x3310, "00: Clear on 1, Jan", "KWH", 100)
    GeneratedEnergyYearH = InputRegister(0x3311, "00: Clear on 1, Jan", "KWH", 100)
    TotalGeneratedEnergyL = InputRegister(0x3312, "", "KWH", 100)
    TotalGeneratedEnergyH = InputRegister(033013, "", "KWH", 100)
    BatteryVoltage = InputRegister(0x331A, "Battery voltage", "V", 100)
    BatteryCurrentL = InputRegister(0x331B, "Battery Current", "A", 100)
    BatteryCurrentH = InputRegister(0x331C, "Battery Current", "A", 100)


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
