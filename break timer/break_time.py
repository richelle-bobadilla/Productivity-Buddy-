# imports
from cProfile import label
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import pygame


class BreakTimer(StudyTimer):

    def __init__(self, root):
        super().__init__(root)
        self.root.title("Break Timer")


if __name__ == "__main__":
    root = tk.Tk()
    break_timer = BreakTimer(root)
    root.mainloop()