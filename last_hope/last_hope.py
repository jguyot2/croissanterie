import setproctitle
import keyboard
import time
import subprocess
import socket

event_list = []

setproctitle.setproctitle("noCroissantsForYou")
def remove_more_than_30s_ago_inputs():
    global event_list
    now = int(time.time())
    cpt = 0
    for event in event_list:
        if(now - int(event.time) < 30):
            event_list = event_list[cpt:]
            return
        cpt +=1

def get_string_from_list():
    ret = ""
    for event in event_list:
        if(True):
            ret += event.name
    return ret

def stop_the_retard():
  host = socket.gethostname()  # get local machine name
  port = 65250  # Make sure it's within the > 1024 $$ <65535 range
  
  s = socket.socket()
  s.connect((host, port))
  message = 'block that retard'
  s.send(message.encode('utf-8'))
  s.close()

def lock():
    global event_list
    event_list = []
    print("LOCK")
    stop_the_retard()
    return

def is_string_not_okay(s):
    return "croissant" in s or "ssant" in s or "croiss" in s

    
def check_the_list_is_okay():
    remove_more_than_30s_ago_inputs()
    s = get_string_from_list()
    if(is_string_not_okay(s)):
        lock()

def callback(keyboard_event):
    global event_list
    print(event_list)
    pressed_key = keyboard_event.name
    code = keyboard_event.scan_code
    time = keyboard_event.time
    event_list.append(keyboard_event)
    check_the_list_is_okay()


if __name__ == '__main__':
    keyboard.on_press(callback)
    keyboard.wait()
