from tkinter import Tk
from modules.user_interface.gui import GUI

# launch the gui
def launch_gui():
    root = Tk()
    app = GUI(root)
    root.mainloop()

# Entry point
if __name__ == "__main__":
    launch_gui()