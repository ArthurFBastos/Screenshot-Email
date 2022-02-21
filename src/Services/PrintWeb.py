
from turtle import screensize
import pygetwindow
import pyautogui
from PIL import Image
import time

def print_web(path):

    #If you need the Titleof a window run these commands 
    #titles = pygetwindow.getAllTitles()
    #print(titles)

    #the code sleeps for 5 seconds (Allow you to minimize any window open)
    time.sleep(5)

    #Select the window according to the Title and get the size of it
    window = pygetwindow.getWindowsWithTitle('Google Chrome')[0]
    #print(window)
    x1 = window.left
    y1 = window.top
    height = window.height
    width = window.width

    x2 = x1 + width
    y2 = y1 + height
    
    #Take the screenshot according to the window size 
    #If there is any window open in front of the selected the image overlaps the other,so leave just the selected window open
    pyautogui.screenshot(path)
    
    im = Image.open(path)
    im =im.crop((x1,y1,x2,y2))
    im.save(path)
    im.show(path)
