import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import cv2

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Office Object Detection")



