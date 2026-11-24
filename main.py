
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=5)

        self.screen = TextInput(
            font_size=35,
            readonly=True,
            halign="right",
            size_hint_y=0.25
        )
        layout.add_widget(self.screen)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for row in buttons:
            line = BoxLayout(spacing=5)
            for char in row:
                btn = Button(text=char, font_size=30)
                btn.bind(on_press=self.press)
                line.add_widget(btn)
            layout.add_widget(line)

        return layout

    def press(self, instance):
        char = instance.text

        if char == "C":
            self.screen.text = ""
        elif char == "=":
            try:
                expression = self.screen.text
                if not all(c in "0123456789+-*/. " for c in expression):
                    raise ValueError()
                self.screen.text = str(eval(expression))
            except:
                self.screen.text = "خطا"
        else:
            if self.screen.text == "خطا":
                self.screen.text = ""
            self.screen.text += char

Calculator().run()
