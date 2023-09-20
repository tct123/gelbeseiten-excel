import requests
from bs4 import BeautifulSoup
import kivy
import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
import pooch
import pandas as pd
import wget
import webbrowser
import sqlite3
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.dropdownitem import MDDropDownItem



class MainApp(MDApp):
    def gettingdata(self, instance): #get data from gelbe seiten
        self.printx = print("Working.")
    
    def updateprogramm(self,instance):
        url="https://github.com/tct123/gelbeseiten-excel/releases"
        webbrowser.open(url)

    
    def de_lang(self, obj):
        self.job_input.hint_text = "Gebe Job ein"
        self.update_btn.text = "Suche nach Updates"
        self.get_data_button.text = "Suche nach Einträgen"

    def build(self):
        conn = sqlite3.connect("entries.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists "gelbeseiten-excel" (
	        "name-of-buissnes"	TEXT,
	        "category"	TEXT,
	        "webpage"	TEXT,
	        "zipcode-and-city"	TEXT,
	        "telnummer"	INTEGER,
	        "Adress"	TEXT)""")
        
        conn.commit()

        conn.close()

        self.screen = MDScreen()
        self.toolbar = MDTopAppBar(title="Gelbe Seiten to Excel Converter")
        self.toolbar.pos_hint = {"top": 1}
        self.screen.add_widget(self.toolbar)
        self.nav_draw = MDNavigationDrawer()
        #self.screen.add_widget(self.nav_draw)
        self.job_input = MDTextField(
            # halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.15},
            #font_size = 22
            )
        self.job_input.hint_text = "Enter job"

        self.update_btn = MDRoundFlatButton(pos_hint = {"center_x": 0.5, "center_y":0.5}, on_release = self.updateprogramm)
        self.update_btn.text = "Search for updates"
        self.screen.add_widget(self.update_btn)
        self.screen.add_widget(self.job_input)
        self.get_data_button = MDRoundFlatButton(on_press = self.gettingdata, pos_hint = {"center_x": 0.5, "center_y":0.3})
        self.get_data_button.text = "Search for entries"
        self.screen.add_widget(self.get_data_button)
        self.langbuttonde = MDRoundFlatButton(text="Deutsch", on_release = self.de_lang)
        self.screen.add_widget(self.langbuttonde)
        #self.screen.add_widget(MDTextField(hint_text = "No helper text")
        return self.screen
        #return MDLabel(text="Hello, World", halign="center")
    



version=1

if __name__ == '__main__':
    MainApp().run()
# request_url = https://www.gelbeseiten.de/Suche/{"job"}/{"city"}
# plzurl = https://home.meinestadt.de/deutschland/plz-6
# Info = https://stackoverflow.com/questions/46351997/python-kivy-how-to-call-a-function-on-button-click