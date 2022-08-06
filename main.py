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
import wget
import webbrowser
import sqlite3

class MainApp(MDApp):
    def gettingdata(self, instance): #get data from gelbe seiten
        self.printx = print("Working.")
    
    def updateprogramm(self,instance):
        url="https://github.com/tct123/gelbeseiten-excel/releases"
        webbrowser.open(url)

    def build(self):
        conn = sqlite3.connect("entries.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists "gelbeseiten-excel" (
	        "name-of-buissnes"	TEXT,
	        "category"	TEXT,
	        "webpage"	TEXT,
	        "zipcode-and-city"	TEXT,
	        "telnummer"	INTEGER,
	        "Adress"	TEXT
            );""")
        screen = MDScreen()
        self.toolbar = MDToolbar(title="Gelbe Seiten to Excel Converter")
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)
        self.job_input = MDTextField(
            hint_text = "Input job",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.15},
            #font_size = 22
            )

        self.update_btn = MDRoundFlatButton(
            text = "Search for updates",
            pos_hint = {"center_x": 0.5, "center_y":0.5})
        self.update_btn.bind(on_press = self.updateprogramm)
        screen.add_widget(self.update_btn)
        screen.add_widget(self.job_input)
        self.get_data_button = MDRoundFlatButton(
            text = "Search for entries"
        )
        self.get_data_button.bind(on_press = self.gettingdata)
        screen.add_widget(self.get_data_button)
        #screen.add_widget(MDTextField(hint_text = "No helper text")
        return screen
        #return MDLabel(text="Hello, World", halign="center")
    



version=1

if __name__ == '__main__':
    MainApp().run()
# request_url = https://www.gelbeseiten.de/Suche/{"job"}/{"city"}
# plzurl = https://home.meinestadt.de/deutschland/plz-6
# Info = https://stackoverflow.com/questions/46351997/python-kivy-how-to-call-a-function-on-button-click