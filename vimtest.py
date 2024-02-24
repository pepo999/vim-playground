from pynput.keyboard import Listener, KeyCode, Key
import os
import sys
import random

counter = 0
initial_coords = [1, 4]
target_coords = [50, 14]
money = 0

os.system('cls')

intro = """

   VIM PLAYGROUND

   Move with:

        k
       /\\

   h<       >l

       \\/
        j

   Pick up the cash $ with:

      x

   Exit with:

      q

   To start press:
      
      l


   Go get that dough

"""

def generate_map(x_dim=100, y_dim=30, char=' '):
    table = []
    empty_l = []
    for i in range(3):
        if i == 1:
            table.append([' ',' ', '$:', ' ', str(money)])
        else:
             for _ in range(x_dim):
                  empty_l.append(' ')
             table.append(empty_l)
    for i in range(y_dim):
        x = []
        for y in range(x_dim):
            if i == 0 or i == y_dim -1:
                x.append('-')
            elif y == 0 or y == x_dim -1:
                x.append('|')   
            else:
                x.append(char)
        table.append(x)
    table[0]=table[0][:-5]
    # labyrinth
    for index, line in enumerate(table):
        if index % 2 != 0 and index > 4 and index < 100:
            random_n = random.randint(2, x_dim - 5)
            random_n2 = random.randint(2, x_dim - 5)
            for char_i, char in enumerate(line):
                if (char_i != random_n and char_i != random_n+1 and char_i != random_n+2 and char_i != random_n2 and char_i != random_n2+1 and char_i!=random_n2 +2):
                    table[index][char_i] = '-'
    table[-1] = [' ' for _ in table[-1]]
    table[-2] = ['-' for _ in table[-2]]
    for i in range(10):
        empty_line = []
        for y in range(x_dim):
            empty_line.append(' ')
        table.append(empty_line)
    return table

map = generate_map()

os.system('clear')
os.system('cls')
print(intro)
sys.stdout.write('\033[H')
sys.stdout.flush()

def even_random_y():
    random_y = random.randint(4, 29)
    if random_y % 2 == 0:
        return random_y
    else:
        return even_random_y()

def print_key(*key):
    global initial_coords
    global target_coords
    global money
    x = initial_coords[0]
    y = initial_coords[1]
    x_t = target_coords[0]
    y_t = target_coords[1]
    map[y][x] = ' ' 
    map[y_t][x_t] = '$'
    if initial_coords == target_coords and key[0] == KeyCode.from_char('x'):
        money += 1
        map[1][4] = str(money)
        map[y_t][x_t] = ' '
        random_y = even_random_y()
        target_coords = [random.randint(2,98),random_y]
        x_t = target_coords[0]
        y_t = target_coords[1]
        map[y_t][x_t] = '$'
        map[y][x] = 'O'
        for line in map:
            print(''.join(line))
        sys.stdout.write('\033[H')
        sys.stdout.flush()
    if key[0] == KeyCode.from_char('q'):
        os.system('cls')
        os.system('clear')
        sys.stdout.flush()
        os.system('cls')
        os._exit(0)
    if key[0] == KeyCode.from_char('l'):
        if x +1 > len(map[y]) - 2 or map[y][x + 1] == '-':
            pass
        else:
            initial_coords[0] += 1
            map[y][initial_coords[0]] = 'O'
            for line in map:
                print(''.join(line))
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    elif key[0] == KeyCode.from_char('h'):
        if initial_coords[0] -1 < 1 or map[y][x-1] == '-':
            pass
        else:
            initial_coords[0] -= 1
            map[y][initial_coords[0]] = 'O'
            for line in map:
                print(''.join(line))
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    elif key[0] == KeyCode.from_char('k'):
        if initial_coords[1] - 1 < 4 or map[y-1][x] == '-':
            pass
        else:
            initial_coords[1] -= 1
            map[initial_coords[1]][x] = 'O'
            for line in map:
                print(''.join(line))
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    elif key[0] == KeyCode.from_char('j'):
        if initial_coords[1] + 1 > len(map) -12 or map[y+1][x] == '-':
            pass
        else:
            initial_coords[1] += 1
            map[initial_coords[1]][x] = 'O'
            for line in map:
                print(''.join(line))
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    
def key():
    with Listener(on_press=print_key) as listener:
        listener.join()

while True:
    key()
