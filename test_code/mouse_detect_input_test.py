
from pynput.mouse import Listener

def on_move(x, y):
    pass

def unpress_check(pressState):
    if pressState == False:
        return True
    return False

def on_click(x, y, button, pressed):
    if button == button.left and pressed:
        print("left")
    elif button == button.right and pressed:
        print("right")


def on_scroll(x, y, dx, dy):
    pass

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()