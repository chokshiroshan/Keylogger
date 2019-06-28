# Keylogger 

![alt text](https://www.hs-academypages.com/hubfs/lp/academy/keylogger.png)

A keylogger, sometimes called a keystroke logger or system monitor, is a type of surveillance technology used to monitor and record each keystroke typed on a specific computer's keyboard. It stores log file into your google drive under name of log.txt using google drive's api. It uses Pydrive(Wrapper) to use API.

## How do I use it?

Run below script to install required libraries:

     pip install -r requirements.txt
    
To run the script:

    python main.py
    
It will open authentication window and u need to allow access to keylogger and then it will start working in background recording and sending each keystroke simultaneously.
    
## What's it doing?

The script is using Listener module of Pynput Library to listen every keystroke and it is then stored to log.txt. Which is being uploaded to Google Drive (after authentication) by Drive's API Wrapper known as Pydrive.
