import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.background_color = (1, 1, 1, 1)  # Set the background color to white

        self.input_label = Label(text="Enter your name:", color=(0, 0, 0, 1))  # Set the text color to black
        self.input_text = TextInput(multiline=False, foreground_color=(0, 0, 0, 1))  # Set the text input color to black
        self.input_text.bind(on_text_validate=self.on_enter)

        self.add_widget(self.input_label)
        self.add_widget(self.input_text)

    def on_enter(self, instance):
        greeting_label = Label(text="Hello " + self.input_text.text + "!", color=(0, 0, 0, 1))  # Set the text color to black
        self.add_widget(greeting_label)


class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Set the window background color to white
        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()
