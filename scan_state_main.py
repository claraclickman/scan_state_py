from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import mapview

class ScreenManagement(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class BuildProject(Screen):
    CurrProjectName = StringProperty('')
    CurrProjectLocation = StringProperty('')
    CurrProjectDate = StringProperty('')
    FastText = StringProperty('')
    
    def submit_data(self, input_name, input_location):
        try:
            self.CurrProjectName = input_name.text
            print("value changed to: ", input_name)
        except:
            print("No Dice!")
        try:
            self.CurrProjectLocation = input_location.text
            print("value changed to: ", input_location.text)
        except:
            print("Something went wrong with location")

    def update_text(self, fast_text):
        try:
            self.FastText = fast_text.text
            print("update!", self.FastText)
        except:
            print("not working!")

class LocationSet(Screen):
    pass

class MapWindow(Widget):
    pass

presentation = Builder.load_file("scan_state_main.kv")


class scan_state_py(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    scan_state_py().run()