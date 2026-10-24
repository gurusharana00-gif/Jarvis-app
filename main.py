from datetime import datetime
import random

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = """
BoxLayout:
    orientation: "vertical"
    padding: 14
    spacing: 10
    canvas.before:
        Color:
            rgba: 0.015, 0.035, 0.10, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "[b]J.A.R.V.I.S[/b]"
        markup: True
        font_size: "30sp"
        color: 0.0, 0.85, 1, 1
        size_hint_y: 0.14

    Label:
        text: "PERSONAL OFFLINE ASSISTANT"
        font_size: "11sp"
        color: 0.3, 0.8, 1, 1
        size_hint_y: 0.06

    TextInput:
        id: chat
        text: "JARVIS ONLINE\\nHello bro! How can I help?"
        readonly: True
        background_color: 0.02, 0.07, 0.15, 1
        foreground_color: 0.3, 0.9, 1, 1
        font_size: "16sp"

    TextInput:
        id: question
        hint_text: "Type a command..."
        multiline: False
        size_hint_y: 0.10
        on_text_validate: app.ask()

    Button:
        text: "SEND COMMAND"
        size_hint_y: 0.12
        background_normal: ""
        background_color: 0, 0.45, 0.85, 1
        on_release: app.ask()
"""

class Jarvis(App):
    def build(self):
        self.title = "JARVIS"
        return Builder.load_string(KV)

    def ask(self):
        box = self.root.ids
        q = box.question.text.strip().lower()

        if not q:
            return

        if q in ("hi", "hello", "hey jarvis"):
            answer = "Hello bro! I am JARVIS."
        elif "time" in q:
            answer = "Time: " + datetime.now().strftime("%I:%M %p")
        elif "date" in q:
            answer = "Date: " + datetime.now().strftime("%d-%m-%Y")
        elif "your name" in q or "who are you" in q:
            answer = "I am JARVIS, your personal assistant."
        elif "joke" in q:
            answer = random.choice([
                "Why did the computer smile? It had a byte!",
                "Robots need breaks too. They recharge!"
            ])
        elif "help" in q:
            answer = "Try: hello, time, date, your name, or joke."
        else:
            answer = (
                "I am running offline, bro. "
                "My basic version cannot answer that yet."
            )

        box.chat.text += (
            "\n\nYOU: " + q +
            "\nJARVIS: " + answer
        )
        box.question.text = ""

Jarvis().run()
