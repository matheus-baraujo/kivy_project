from re import MULTILINE
from typing import Text
from kivy.app import App
from kivy.core import image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class DnDLogin(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.window.bg_color = '#C62B29'

        #add widgets to window

        self.logo = Image(source = "resources/dndlogo.jpg")
        self.window.add_widget(self.logo)
        
        self.userLabel = Label(
                            text = "User name",
                            font_size = 20,
                            color = '#FF0000'
                            )
        self.window.add_widget(self.userLabel)

        self.user = TextInput(
                            multiline = False,
                            padding_y = (20,20),
                            size_hint = (1, 0.3),
                            border = (30, 30, 30, 30)
                            )
        self.window.add_widget(self.user) 

        return self.window

if __name__ == "__main__":
    DnDLogin().run()