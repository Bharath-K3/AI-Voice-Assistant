import pyautogui

# Printing the default screen width and height
screenWidth, screenHeight = pyautogui.size()

print(screenWidth, screenHeight)

# Showing the current cursor position
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print(currentMouseX, currentMouseY)

# Locating on the Screen by getting the co-ordinates
# x, y = pyautogui.locateCenterOnScreen("image.png")

# Open The Admin Directory
pyautogui.moveTo(37, 35, 1)
pyautogui.click(button='left', clicks=2)