import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

first_hod = "player_1"

def which_turn():
    global first_hod
    first_hod = "player_2" if first_hod == "player_1" else "player_1"

i = 0
button_states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Хранение состояний кнопок (0 - пусто, 1 - player_1, 2 - player_2)
button_positions = [[(j * 300, i * 300) for j in range(3)] for i in range(3)]  # Хранение позиций кнопок
def on_button_press(button):
    global i, button_states, button_positions
    button_x, button_y = button.pos
    button_color = button.background_color
    
    print(f'{i} cordinate --> {button_x, button_y}')
    print(f"color --> {button_color}")
    i += 1

    # Определение игрока и изменение цвета кнопки
    if first_hod == "player_1":
        if button_color[0] == 1 and button_color[1] == 10 and button_color[2] == 0:
            which_turn()
        else:
            button.background_color = [1, 0, 0, 1]  # Изменение цвета на красный при нажатии
            print(button_x//400)
            button_states[int(button_y // 300)][int(button_x // 400)] = 1  # Обновление состояния кнопки
            for buttons in button_states:
                print(buttons)  # Вывод состояния кнопок
            which_turn()
    else:
        if button_color[0] == 1 and button_color[1] == 0 and button_color[2] == 0:
            which_turn()
        else:
            button.background_color = [1, 10, 0, 1]  # Изменение цвета на зеленый при нажатии
            print(button_x//400)
            button_states[int(button_y // 300)][int(button_x // 400)] = 2  # Обновление состояния кнопки
            for buttons in button_states:
                print(buttons)  # Вывод состояния кнопок
            which_turn()

    print(check_winner())  # Проверка победителя после каждого хода
 # Проверка победителя после каждого хода

# Проверка выигрышных комбинаций
def check_win():
    for i in range(3):
        if button_states[i][0] == button_states[i][1] == button_states[i][2] != 0 or \
           button_states[0][i] == button_states[1][i] == button_states[2][i] != 0:
            return True
    
    if button_states[0][0] == button_states[1][1] == button_states[2][2] != 0 or \
       button_states[0][2] == button_states[1][1] == button_states[2][0] != 0:
        return True
    
    return False

# Проверка победителя
def check_winner():
    if check_win():
        if first_hod == "player_1":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    return "No winner yet."

class ColorGame(App):
    def build(self):
        layout = GridLayout(cols=3, spacing=10)
        
        for i in range(3):
            for j in range(3):
                button = Button(text=f'Button {i * 3 + j + 1}', background_color=[1, 1, 1, 1])
                button_positions[i][j] = (i * 300, j * 300)
                button.bind(on_press=lambda btn: on_button_press(btn))
                layout.add_widget(button)
        
        return layout

if __name__ == '__main__':
    ColorGame().run()
