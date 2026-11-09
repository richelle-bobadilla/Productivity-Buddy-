# imports
from cProfile import label
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class StudyTimer:

    def __init__(self, root):

        # set up
        self.root = root
        self.root.title("Study Timer")
        self.time_left = 0
        self.root.geometry("400x400")
        self.root.configure(bg = "#1f1f1f")
        self.is_timer_running = False


        #widgets
        # instructions
        self.instructions = tk.Label(root, text = "Ready to focus?", font = ("Courier Prime 16", 13), fg = "#ececec", bg = "#1f1f1f")
        self.instructions.pack(pady = 25)

        # countdown text
        self.countdown_text = tk.Label(root, text = "25:00", font =("Courier Prime 16", 50), fg = "#4a7eff", bg = "#1f1f1f")
        self.countdown_text.pack()
        

        # slider
        self.slider = ctk.CTkSlider(master = root, from_ = 25, to = 120, width = 250, button_color = "#4a7eff", button_hover_color = "#2e5cb8", progress_color = "#4a7eff",
                                     fg_color = "#ececec", command = self.slider_value)
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
        self.start_button = ctk.CTkButton(master = self.button_frame, text = "Start", command = self.start_timer, width = 70, height = 30, corner_radius = 10,
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



    def slider_value(self, value):
        minutes = int(value)
        self.countdown_text.config(text = f"{minutes:02d}:00")
        

    def start_timer(self):
        # start the timer
        if not self.is_timer_running:
            self.is_timer_running = True
            self.time_left = int(self.slider.get()) * 60
            self.update_timer()

        
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




    def update_timer(self):
        # update the countdown text
        if self.time_left > 0 and self.is_timer_running:
            minutes, seconds = divmod(self.time_left, 60)
            formatted_time = f"{minutes:02d}:{seconds:02d}"
            self.countdown_text.config(text = formatted_time)
            self.time_left -= 1
            self.root.after(1000, self.update_timer)

        elif self.is_timer_running:
            self.countdown_text.config(text = "00:00")
            messagebox.showinfo("Time's up! Break time :D")
            self.is_timer_running = False



if __name__ == "__main__":

    root = tk.Tk()
    StudyTimer(root)
    root.mainloop()
