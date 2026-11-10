from cProfile import label
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import pygame


class StudyApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.configure(bg = "#1f1f1f")
        self.is_timer_running = False

        self.instructions = tk.Label(root, text = "", font = ("Courier Prime 16", 13), fg = "#ececec", bg = "#1f1f1f")
        self.countdown_text = tk.Label(root, text = "00:00", font =("Courier Prime 16", 50), fg = "#4a7eff", bg = "#1f1f1f")
        self.slider = ctk.CTkSlider(master = root, from_ = 0, to = 120, width = 250, button_color = "#4a7eff", button_hover_color = "#2e5cb8", progress_color = "#4a7eff",
            fg_color = "#ececec", command = self.slider_value)


    def slider_value(self, value):
        minutes = int(value)
        self.countdown_text.config(text = f"{minutes:02d}:00")


    def start_timer(self):
        # start the timer
        if not self.is_timer_running:
            self.is_timer_running = True
            self.time_left = int(self.slider.get()) * 60
            self.slider.configure(state = "disabled")
    
            self.update_timer()


    def update_timer(self):
        # update the countdown text\
        if self.is_timer_running and self.time_left > 0:
            minutes = self.time_left // 60
            seconds = self.time_left % 60

            self.countdown_text.config(
                text=f"{minutes:02d}:{seconds:02d}"
            )   

            self.slider.set(self.time_left / 60)
            self.time_left -= 1

            self.root.after(1000, self.update_timer)

        elif self.is_timer_running:
            self.countdown_text.config(text="00:00")
            self.is_timer_running = False
            self.slider.configure(state="normal")