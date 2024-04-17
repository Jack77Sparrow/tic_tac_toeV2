from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.input_label = Label(text="Введите ваше имя:")
        self.input_text = TextInput()
        self.submit_button = Button(text="Готово", on_press=self.switch_to_game)
        self.layout.add_widget(self.input_label)
        self.layout.add_widget(self.input_text)
        self.layout.add_widget(self.submit_button)
        self.add_widget(self.layout)

    def switch_to_game(self, instance):
        # Переключаемся на экран игры и передаем введенное имя
        self.manager.get_screen('game').start_game(self.input_text.text)
        self.manager.current = 'game'

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.game_label = Label(text="Игра начинается!")
        self.layout.add_widget(self.game_label)
        self.add_widget(self.layout)

    def start_game(self, player_name):
        self.game_label.text = f"Игра начинается, {player_name}!"

class MyApp(App):
    def build(self):
        # Создаем экраны
        sm = ScreenManager()
        input_screen = InputScreen(name='input')
        game_screen = GameScreen(name='game')

        # Добавляем экраны в менеджер экранов
        sm.add_widget(input_screen)
        sm.add_widget(game_screen)

        return sm

if __name__ == '__main__':
    MyApp().run()
