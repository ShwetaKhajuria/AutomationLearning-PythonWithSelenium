import pywinauto
print(pywinauto.__version__)

from pywinauto import Application
import time

# Start Notepad
app = Application().start("notepad.exe")

# Wait a moment for the app to open
time.sleep(1)

# Select the Notepad window
notepad = app.window(title_re=".*Notepad")

# Type some text
notepad.Edit.type_keys("Hello, this is an automation test!", with_spaces=True)
notepad.Edit.type_keys("\n This is something I want to write in notepad0", with_spaces=True)

# Open File > Save As
notepad.menu_select("File -> Save As")

# Wait for Save As dialog
save_as = app.window(title_re=".*Save As")

# Type file name and click Save
save_as.Edit.type_keys("C:\\Users\\Public\\testfile.txt", with_spaces=True)
save_as.Save.click()

# Optional: Close Notepad
notepad.close()

# Handle the prompt if asked to save again
try:
    app.window(title_re=".*Notepad").window(title="Don't Save").click()
except:
    pass