from kivy.app import App
import json
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
Window.size = (1000, 600)

class Base(App):
    def __init__(self):
        super().__init__()
        self.button = Button(text="123", size=(50, 50), pos=(50, 50), background_color="green")
        self.box = FloatLayout()
        self.background = Image(source='background.png', fit_mode='cover')
        self.box.add_widget(self.background)
        self.box.add_widget(self.button)



        self.map_buttons = []
        #self.create_map_buttons({"107": [(0.1, 0.2), "green"], "100": [(0.1, 0.2), "red"]})

    def build(self):
        return self.box

    def create_map_buttons(self, json_map:dict):
        a = 0
        for key in json_map.keys():
            self.map_buttons.append(Button(text=key, size_hint=json_map[key][0], pos_hint={"x": 0.1+(a*0.2), "y": 0.1+(a*0.2)}, background_color=json_map[key][1]))
            a += 1
        for buttons in self.map_buttons:
            self.box.add_widget(buttons)







if __name__ == "__main__":
    Base().run()