# by Kami Bigdely
# Docstrings and blank lines

class OnBoardTemperatureSensor:
    """Represents the onboard temperature sensor."""

    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        pass

    def read_voltage(self):
        """In real life, it should read from hardware."""         
        return 2.7

    def get_temperature(self):
        """Returns the temperature in celcius"""

        return self.read_voltage() * \
            OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR
  
class CarbonMonoxideSensor:
    """Represents the carbon monoxide sensor."""

    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide(self):
        """Returns carbon monoxide level."""

        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = self.convert_voltage_to_carbon_monoxide(
                    sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """In real life, it should read from hardware."""   

        return 2.3

    def convert_voltage_to_carbon_monoxide(self, voltage, temperature):
        """Converts voltage to carbon monoxide level and returns it."""

        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR \
                * temperature

class DisplayUnit:
    """Represents the display unit."""

    def __init__(self):
        self.string = ''

    def display(self,msg):
        print(msg)

class CarbonMonoxideDevice():
    """Represents the carbon monoxide device."""

    def __init__(self, co_sensor, display_unit):
        self.carbonMonoxideSensor = co_sensor
        self.display_unit = display_unit

    def Display(self):
        msg = 'Carbon Monoxide Level is : ' + \
        str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.Display()