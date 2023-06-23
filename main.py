from pynput import keyboard
from pynput import mouse


"""Click and Hold Clicker"""

print('-' * 10 + '\nHello!\n' + '-' * 10 + '\nOptions:\n\tif you want to finish clicker - press "t"\n\tif you want to start clicker - hold "k"\n\nHave fuuun!!!!!')


term_key = keyboard.KeyCode(char='t')
main_key = keyboard.KeyCode(char='k')

Mouse = mouse.Controller()

def on_release(key):
    if key == term_key:
        print('---finished---')
        return False


def on_press(key):
     if key == main_key:
        Mouse.click(mouse.Button.left, 1)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
