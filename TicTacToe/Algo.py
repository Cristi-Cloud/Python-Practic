
def utility(tabel):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for condition in win_conditions:
        a, b, c = condition
        if tabel[a[0]][a[1]] == tabel[b[0]][b[1]] == tabel[c[0]][c[1]] and tabel[a[0]][a[1]] == "x":
            return 'x'
        elif tabel[a[0]][a[1]] == tabel[b[0]][b[1]] == tabel[c[0]][c[1]] and tabel[a[0]][a[1]] == "o":
            return 'o'

    return '-'


def is_terminal(status):
    if utility(status) != '-':
        return True
    else:
        return False


def value_status(status):
    decision = utility(status)
    if decision == 'x':
        return 1
    elif decision == 'o':
        return -1
    else:
        return 0

def actions(status)->list[tuple[int, int]]:
    vec = []
    for i in range(3):
        for j in range(3):
            if status[i][j] == '-':
                vec.append((i, j))
    return vec

def result_of_action1(status, action):
    status[action[0]][action[1]] = 'x'
    return status

def result_of_action2(status, action):
    status[action[0]][action[1]] = 'o'
    return status

def player(turn):
    return turn

def minimax(status, turn:int, temp=0):
     if is_terminal(status):
         return value_status(status), None

     if player(turn) == 1:
         value: int = -10
         act = None
         for action in actions(status):
             decision:int = minimax(result_of_action1(status, action), turn * -1)[0]
             if temp > 0:
                print(action, decision)
             if decision > value:
                 value = decision
                 act = action

         return value, act

     if player(turn) == -1:
         value: int = 10
         act = None
         for action in actions(status):
             decision:int = minimax(result_of_action2(status, action), turn * -1)[0]
             if decision < value:
                 value = decision
                 act = action

         return value, act

     return 0, None



def nextmove(tabel):
    nr = 0
    for i in range(3):
        for j in range(3):
            if tabel[i][j] == '-':
                nr += 1
    if nr == 9:
        return 1, 1
    else:
        return minimax(tabel, 1)[1]

def main():
    tabel = [
        ['x', '-', '-'],
        ['o', 'x', 'x'],
        ['o', 'o', '-']
    ]
    finish = minimax(tabel, 1, 1)
    print(finish)


if __name__ == '__main__':
    main()