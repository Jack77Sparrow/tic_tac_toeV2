from tic_tac_toe import button_y, button_x, first_hod


# Проверка выигрышных комбинаций
def check_win():
    # Проверка по горизонтали
    for i in range(3):
        if button_y[i][0] == button_y[i][1] == button_y[i][2] or button_x[i][0] == button_x[i][1] == button_x[i][2]:
            return True
    
    # Проверка по вертикали
    for i in range(3):
        if button_y[0][i] == button_y[1][i] == button_y[2][i] or button_x[0][i] == button_x[1][i] == button_x[2][i]:
            return True
    
    # Проверка по диагоналям
    if button_y[0][0] == button_y[1][1] == button_y[2][2] or button_x[0][0] == button_x[1][1] == button_x[2][2]:
        return True
    if button_y[0][2] == button_y[1][1] == button_y[2][0] or button_x[0][2] == button_x[1][1] == button_x[2][0]:
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

print(check_winner())
