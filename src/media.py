from pynput.keyboard import Key,Controller
from time import sleep

keyboard = Controller()

def volume_up():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volume_down():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def volume_mute():
    keyboard.press(Key.media_volume_mute)
    keyboard.release(Key.media_volume_mute)
    sleep(0.1)

def play_pause():
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)
    sleep(0.1)

def next_track():
    keyboard.press(Key.media_next)
    keyboard.release(Key.media_next)
    sleep(0.1)

def previous_track():
    keyboard.press(Key.media_previous)
    keyboard.release(Key.media_previous)
    sleep(0.1)
