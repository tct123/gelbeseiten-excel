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

lang = input("Enter your language (Deutsch, English): ")

if lang.lower() == "deutsch":
    job_input_text = "Gebe Job ein"
    update_btn_text = "Suche nach Updates"
    get_data_button_text = "Suche nach Einträgen"
else:
    job_input_text = "Enter job"
    update_btn_text = "Search for updates"
    get_data_button_text = "Search for entries"


class MainApp(MDApp):
    def callback(self):
        pass
    def gettingdata(self, instance): #get data from gelbe seiten
        self.printx = print("Working.")
    
    def updateprogramm(self,instance):
        url="https://github.com/tct123/gelbeseiten-excel/releases"
        webbrowser.open(url)

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

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

        screen = MDScreen()
        self.toolbar = MDTopAppBar(title="Gelbe Seiten to Excel Converter",left_action_items = [["menu", lambda x: self.callback(x)]])
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)
        self.nav_draw = MDNavigationDrawer()
        #screen.add_widget(self.nav_draw)
        self.job_input = MDTextField(
            hint_text = f"{job_input_text}",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.15},
            #font_size = 22
            )

        self.update_btn = MDRoundFlatButton(
            text = f"{update_btn_text}",
            pos_hint = {"center_x": 0.5, "center_y":0.5})
        self.update_btn.bind(on_press = self.updateprogramm)
        screen.add_widget(self.update_btn)
        screen.add_widget(self.job_input)
        self.get_data_button = MDRoundFlatButton(
            text = f"{get_data_button_text}"
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