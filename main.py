import requests
from bs4 import BeautifulSoup
import kivy
import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(MDRectangleFlatButton(
            text="Hello World",
            pos_hint={"center_x": 0.5, "center_y":0.5},
            on_press=exit,
            )
        )
        screen.add_widget()
        return screen
        #return MDLabel(text="Hello, World", halign="center")

MainApp().run()
# request_url = https://www.gelbeseiten.de/Suche/{"job"}/{"city"}
# plzurl = https://home.meinestadt.de/deutschland/plz-6