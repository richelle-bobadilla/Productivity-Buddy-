# imports
from cProfile import label
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import pygame
from study_app import StudyApp


class StudyTimer(StudyApp):

    def __init__(self, root):
        super().__init__(root)
        self.time_left = 0
        self.root.title("Study Timer")

        #widgets
        # instructions
        self.instructions = tk.Label(root, text = "Ready to focus?", font = ("Courier Prime 16", 13), fg = "#ececec", bg = "#1f1f1f")
        self.instructions.pack(pady = 25)

        # countdown text
        self.countdown_text = tk.Label(root, text = "25:00", font =("Courier Prime 16", 50), fg = "#4a7eff", bg = "#1f1f1f")
        self.countdown_text.pack()
        

        # slider
        self.slider.pack(pady = 50)
        self.slider.set(25)

        # button frame
        self.button_frame = tk.Frame(root, bg="#1f1f1f")
        self.button_frame.pack(pady=10)


        # pause button
        self.pause_button = ctk.CTkButton(master = self.button_frame, text = "Pause", command = self.pause_timer, width = 70, height = 30, corner_radius = 10,
            fg_color="#4a7eff",
            hover_color="#2e5cb8",
            text_color="#ececec",
            font=("Courier Prime 16", 14, "bold"))
                
        self.pause_button.pack(side = "left", padx = 10)
        
        # start button
        self.start_button = ctk.CTkButton(master = self.button_frame, text = "Start", command = super().start_timer, width = 70, height = 30, corner_radius = 10,
            fg_color="#4a7eff",
            hover_color="#2e5cb8",
            text_color="#ececec",
            font=("Courier Prime 16", 14, "bold"))
        
        self.start_button.pack(side = "left", padx = 10)

        # reset button
        self.reset_button =  ctk.CTkButton(self.button_frame, text = "Reset", command = self.reset_timer, width = 70, height = 30, corner_radius = 10,
            fg_color="#4a7eff",
            hover_color="#2e5cb8",
            text_color="#ececec",
            font=("Courier Prime 16", 14, "bold"))
                        
        self.reset_button.pack(side = "left", padx = 10)

        pygame.mixer.init()

    def pause_timer(self):
        self.is_timer_running = False
        messagebox.showinfo("Make sure to come back to studying after your break!")
        self.is_timer_running = True
        self.update_timer()


    def reset_timer(self):
        self.is_timer_running = False
        self.countdown_text.config(text = "25:00")

        #reset to 25 minutes
        self.time_left = 25 * 60 

        self.slider.configure(state = "normal")
        self.slider.set(25)


    def update_timer(self):
        # update the countdown text
        super().update_timer()

        if self.countdown_text.cget("text") == "00:00" and self.is_timer_running:
            messagebox.showinfo("Time's up! Break time :D")
            pygame.mixer.init()
            pygame.mixer.music.load("bell.mp3")
            
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play()
            self.is_timer_running = False
            pygame.mixer.music.stop()
            
            self.slider.set(25)
            self.slider.configure(state = "normal")



if __name__ == "__main__":

    root = tk.Tk()
    StudyTimer(root)
    root.mainloop()
