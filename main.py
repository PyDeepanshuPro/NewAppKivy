from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


# ----------- Login Screen -----------
class LoginScreen(BoxLayout):
    def __init__(self, switch_to_calculator, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 40
        self.spacing = 20
        self.switch_to_calculator = switch_to_calculator

        self.add_widget(Label(text="🔒 Login Screen", font_size=30, bold=True))

        self.username = TextInput(hint_text="Enter Username", multiline=False)
        self.add_widget(self.username)

        self.password = TextInput(hint_text="Enter Password", multiline=False, password=True)
        self.add_widget(self.password)

        login_btn = Button(text="Login", font_size=20, size_hint=(1, 0.5), background_color=(0, 0.5, 1, 1))
        login_btn.bind(on_press=self.validate_login)
        self.add_widget(login_btn)

    def validate_login(self, instance):
        user = self.username.text
        pwd = self.password.text

        if user == "admin" and pwd == "1234":
            self.switch_to_calculator()
        else:
            self.show_popup("Login Failed ❌", "Invalid Username or Password")

    def show_popup(self, title, message):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        box.add_widget(Label(text=message))
        close_btn = Button(text="OK", size_hint=(1, 0.3))
        box.add_widget(close_btn)
        popup = Popup(title=title, content=box, size_hint=(0.7, 0.4))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()


# ----------- Calculator Screen -----------
class CalculatorScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        self.display = TextInput(
            readonly=True, halign="right", font_size=40, size_hint=(1, 0.3)
        )
        self.add_widget(self.display)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            ["="],
        ]

        layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.7))
        for row in buttons:
            for label in row:
                btn = Button(text=label, font_size=30)
                btn.bind(on_press=self.on_button_press)
                layout.add_widget(btn)
        self.add_widget(layout)

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""
        elif text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"
        else:
            self.display.text += text


# ----------- Main App -----------
class MyApp(App):
    def build(self):
        self.root_layout = BoxLayout()
        self.show_login()
        return self.root_layout

    def show_login(self):
        self.root_layout.clear_widgets()
        login_screen = LoginScreen(switch_to_calculator=self.show_calculator)
        self.root_layout.add_widget(login_screen)

    def show_calculator(self):
        self.root_layout.clear_widgets()
        calc_screen = CalculatorScreen()
        self.root_layout.add_widget(calc_screen)


if __name__ == "__main__":
    MyApp().run()
