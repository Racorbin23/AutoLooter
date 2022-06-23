import pyautogui
import keyboard
import time


ore_icon1 = "dolivine.png" #Get Ore Icon
ore_icon2 = "hadanite.png" #Get Ore Icon
ores = [ore_icon1, ore_icon2]
left_location = (400, 400) #TODO: Get window location of inventory
right_location = (2000, 400) #TODO: Get window location of inventory

SLEEP = 0.1
DELAY = 0.5
CONFIDENCE = 0.9

def isOreOnScreen(item_pic):
    return pyautogui.locateOnScreen(item_pic, confidence=CONFIDENCE, grayscale=True) is not None

def clickDrag(x1, y1, x2, y2):
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, button='left', duration=0.5)
    
def moveOre(loc, left):
    print("======= Dragging ore! =======")
    if left:
        clickDrag(loc[0], loc[1], left_location[0], left_location[1])
    else:
        clickDrag(loc[0], loc[1], right_location[0], right_location[1])
            

def findOre():
    ore1 = pyautogui.locateOnScreen(ore_icon1, confidence=CONFIDENCE, grayscale=True)
    if ore1: 
        return ore1
    ore2 = pyautogui.locateOnScreen(ore_icon2, confidence=CONFIDENCE, grayscale=True)
    if ore2: 
        return ore2
    return False


def isOreInventoy(ore_location):
    if ore_location[1] > pyautogui.size()[1]/2:
        return True
    else:
        return False
    
    
    
    
    

    



# Wait for button to be clicked
while True:
    if keyboard.is_pressed("m"):
        print("Macro Triggered!")
        loc = findOre()
        while loc != False and not keyboard.is_pressed("n"):
            moveOre(loc, True)
            loc = findOre() 
    elif keyboard.is_pressed(","):
        print("Macro Triggered!")
        loc = findOre()
        while loc != False and not keyboard.is_pressed("n"):
            moveOre(loc, False)
            time.sleep(SLEEP)
            loc = findOre() 
    else:
        print("IDLE")
        time.sleep(SLEEP)
        
        

