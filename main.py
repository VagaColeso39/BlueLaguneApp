from kivy.app import App
from kivy.clock import Clock
import json
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
Window.size = (1920, 1200)


# Данную часть кода я для примера взял из интернета, так что на всякий случай оставлю оригинальные комменрарии.
# В данном комите не реализована механика получения jsona кнопок, пока только заранее прописаные.
class DraggableImage(Image):
   # Override the on_touch_down method to detect when the user touches the widget
   def on_touch_down(self, touch):
      if self.collide_point(*touch.pos):
         # If the touch event occurred within the widget's bounds, handle the touch event
         # by setting the widget as the current touch target
         touch.grab(self)
         return True
      return super().on_touch_down(touch)

   # Override the on_touch_move method to track the movement of the user's finger
   def on_touch_move(self, touch):
      if touch.grab_current == self:
         # If the touch event is being handled by our widget, update the widget's position
         self.pos = (self.pos[0] + touch.dx, self.pos[1] + touch.dy)

   # Override the on_touch_up method to update the widget's position when the touch event ends
   def on_touch_up(self, touch):
      if touch.grab_current == self:
         # If the touch event is being handled by our widget, release the widget as the current
         # touch target and handle the touch event
         touch.ungrab(self)
         return True
      return super().on_touch_up(touch)


class Base(App):
    def __init__(self):
        super().__init__()
        json_example = {"106": {"pos": (50, 50), "type":  "lecture_class", "lectures": {"10:00":  {"group":  "636-02", "lecturer":  "Садовников А.В.", "length":  120,"subject":  "physics"},
                                                "13:00":  {"group":  "636-01", "lecturer":  "Иванов И.И", "length":  180,"subject":  "math",
                                                "17:00":  {"group":  "636", "lecturer":  "Александров А.А.", "length":  90,"subject":  "english"},
                                                "19:00":  {"group":  "701", "lecturer":  "Петров П.И.", "length":  90,"subject":  "history"}}}},
"108": {"pos": (100, 100), "type":  "coworking", "items":  ["board", "projector"], "currently_here": 4}}
        self.button = [Button(text="123", size_hint=(0.05, 0.05), pos=(50, 50), background_color="green"), Button(text="456", size_hint=(0.05, 0.05), pos=(100, 100), background_color="red")]
        self.box = FloatLayout()
        self.background = DraggableImage(source='background.png', fit_mode='cover')
        self.box.add_widget(self.background)
        self.buttons_base_state = []
        need_to_replace = 0
        for key in json_example:
            self.buttons_base_state.append(json_example[key]["pos"])
            self.box.add_widget(self.button[need_to_replace])
            need_to_replace += 1



        self.map_buttons = []
        Clock.schedule_interval(self.buttonsMove, 1 / 60)
        #self.create_map_buttons({"107": [(0.1, 0.2), "green"], "100": [(0.1, 0.2), "red"]})


    def buttonsMove(self, dt):
        if self.background.pos != (0, 0):
            num = 0
            for but in self.button:
                but.pos = (self.buttons_base_state[num][0] + self.background.pos[0], self.buttons_base_state[num][1] + self.background.pos[1])
                num += 1


    def resize(self, button):
        button.size = (0.1, 0.1)
        print(button.size)
        print(button.texture_size)
        print(self.background.size)
        print(Window.size)
        self.box._set_scale(0.5)

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
