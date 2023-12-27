# Import the required modules
import kivy
from kivy.app import App
from kivy.uix.button import Button

# Set the Kivy version
kivy.require('1.11.1')

# Define the DraggableButton class
class DraggableButton(Button):
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

# Define the Kivy application class
class MyApp(App):
   def build(self):
      # Create a DraggableButton widget and add it to the root widget
      button = DraggableButton(text='Drag me to any direction!')
      return button

# Run the application
if __name__ == '__main__':
   MyApp().run()