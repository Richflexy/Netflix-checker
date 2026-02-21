from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=30, spacing=20)

        with self.canvas.before:
            Color(1, 0.85, 0.95, 1)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[30])

        title = Label(
            text="🎀 Hello Kitty Checker 🎀",
            font_size=32,
            color=(1, 0.2, 0.6, 1)
        )

        load_btn = Button(
            text="Load Combo",
            size_hint=(1, None),
            height=60,
            background_color=(1, 0.4, 0.7, 1)
        )

        start_btn = Button(
            text="Start Checking",
            size_hint=(1, None),
            height=60,
            background_color=(1, 0.6, 0.8, 1)
        )

        self.add_widget(title)
        self.add_widget(load_btn)
        self.add_widget(start_btn)

class HelloKittyApp(App):
    def build(self):
        return MainUI()

HelloKittyApp().run()
