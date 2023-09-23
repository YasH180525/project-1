from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.toast import toast
from kivymd.uix.label import MDLabel

from kivymd.app import MDApp
# from kivymd_extensions.akivymd import*
# from kivymd_extensions.akivymd.uix.charts import AKPieChart
from kivy.metrics import dp
from datetime import date
from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarIconListItem,TwoLineAvatarIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import platform
import datetime
from firebase_admin import *
from firebase_admin import db
    
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

kv = """

ScreenManager:
    id:screen_manager
    MenuScreen:
    SecondScreen:

<MenuScreen>:

    name: 'menu'

    MDLabel:
        text: 'Enter Username'
        
        pos_hint:{'center_x': 0.9, 'center_y': 0.8}
    MDTextField:
        id:username
        hint_text: "username"
        helper_text: "username"
        helper_text_mode: "on_focus"
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        size_hint_x:None
        width:300
    MDLabel:
        text: 'Enter Password'
        
        pos_hint:{'center_x': 0.9, 'center_y': 0.6}
    MDTextField:
        id:password
        hint_text: "password"
        helper_text: "password"
        helper_text_mode: "on_focus"
        icon_right: "form-textbox-password"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:300
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release: root.database() 

    
    

<SecondScreen>:
    name: 'second'

    MDLabel:
        id:username_show
        text: 'Hello'
        
        pos_hint:{'center_x': 0.9, 'center_y': 0.8}
    


"""

class MenuScreen(Screen):
    
    if platform =='android':
         from android.permissions import request_permissions, Permission
         request_permissions([ Permission.READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE])
         
    cred = credentials.Certificate('/storage/emulated/0/testing.json')

    app = firebase_admin.initialize_app(cred)
    def database(self):
        

        db = firestore.client()
        name = self.ids.username.text
        password = self.ids.password.text
        data = {"name": str(name), "password": str(password)}

    # Add a new doc in collection 'cities' with ID 'LA'


        # city_ref = db.collection("users").document("info")
        doc_ref = db.collection("users").document(self.ids.username.text)

        doc = doc_ref.get()
        if doc.exists:
            toast("Welcome User: " + self.ids.username.text)
            print(doc.to_dict())
            results = doc.to_dict()
            app2 = MDApp.get_running_app()
            app2.root.current = "second"
        else:
            db.collection("users").document(name).set(data)
        
    
  
    # city_ref.set({"capital": True}, merge=True)
  
    
    # city_ref = db.collection("users").document("info")

# # Atomically add a new region to the 'regions' array field.
#     city_ref.update({"name": firestore.ArrayUnion([name]),"mobile": firestore.ArrayUnion([mobile])})
            toast("Data Saved")

class SecondScreen(Screen):
    pass
    


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SecondScreen(name='second'))
class DemoApp(MDApp):
    dialog = None
    def build(self):
        screen = Builder.load_string(kv)
        
        
        return screen
    
DemoApp().run()

