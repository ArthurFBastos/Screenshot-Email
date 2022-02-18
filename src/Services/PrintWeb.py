from turtle import screensize
import pygetwindow
import pyautogui
from PIL import Image
import time
n = 1
path = f"C:\\Users\\Acer\\Desktop\\Arquivos\\Py\\Screenshot_Email\\src\\Services\\Prints\\Print{n}.png"

titles = pygetwindow.getAllTitles()

time.sleep(5)
window = pygetwindow.getWindowsWithTitle('Google Chrome')[0]
#print(window)
x1 = window.left
y1 = window.top
height = window.height
width = window.width

x2 = x1 + width
y2 = y1 + height

pyautogui.screenshot(path)

im = Image.open(path)
im =im.crop((x1,y1,x2,y2))
im.save(path)
im.show(path)