import requests
from bs4 import BeautifulSoup
import kivy
import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar
import pooch
import pandas as pd

class MainApp(MDApp):
    def gettingdata(self): #get data from gelbe seiten
        self.printx = print("Working.")
    def updatezipcodes(self,url):
        self.url = "https://raw.githubusercontent.com/tct123/zipcodes-germany/master/zipcodes-germany-cleaned-up.csv"
        pooch.retrieve(url)

    def build(self):
        screen = MDScreen()
        self.toolbar = MDToolbar(title="Gelbe Seiten to Excel Converter")
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)
        self.job_input = MDTextField(
            text = "Input job",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.45},
            font_size = 22)

        self.btn = MDRoundFlatButton(
            text = "Get/update Lists",
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            on_press = self.updatezipcodes)
        screen.add_widget(self.btn)
        screen.add_widget(self.job_input)
        #screen.add_widget(MDTextField(hint_text = "No helper text")
        return screen
        #return MDLabel(text="Hello, World", halign="center")

version=1

if __name__ == '__main__':
    MainApp().run()
# request_url = https://www.gelbeseiten.de/Suche/{"job"}/{"city"}
# plzurl = https://home.meinestadt.de/deutschland/plz-6