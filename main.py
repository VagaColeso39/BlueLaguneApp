from kivy.app import App
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.uix.togglebutton import ToggleButton


class Base(App):
    def __init__(self):
        super().__init__()
        self.button = Button(text="123", size_hint=(0.2, 0.5), pos_hint={"x": 0.3, "y": 0.2})
        self.box = RelativeLayout()
        self.box.add_widget(self.button)

    def build(self):
        return self.box


Base().run()
print(123)