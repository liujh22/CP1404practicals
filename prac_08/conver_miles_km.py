"""
Calculator to convert mile to km
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILE_TO_KM = 1.609344


class ConvertMilesToKilometers(App):
    """Kivy app to convert miles to kilometers"""
    def build(self):
        """load laying out from file"""
        Window.size = (400, 200)
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, value):
        """converter with error checking"""
        try:
            value = float(value)
            value = value * MILE_TO_KM
            self.root.ids.output_number.text = str(value)
        except ValueError:
            self.root.ids.output_number.text = str("0")

    def handle_increment(self, value, increment):
        """increment with error checking"""
        try:
            value = float(value)
            value += increment
            self.root.ids.input_number.text = str(value)
        except ValueError:
            value = 0
            value += increment
            self.root.ids.input_number.text = str(value)


ConvertMilesToKilometers().run()
