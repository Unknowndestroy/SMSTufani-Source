import tkinter as tk
from tkinter import ttk
import os

class ThemeSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SMSTufanı 2.3 EX-BETA / WARNING: Light mode may not work!")
        self.root.geometry("600x300")
        self.root.resizable(False, False)

        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (300 // 2)
        self.root.geometry(f"600x300+{x}+{y}")

        self.canvas = tk.Canvas(self.root, width=600, height=300)
        self.canvas.pack(fill="both", expand=True)

        # Draw two triangles for Dark and Light themes
        self.canvas.create_polygon(0, 0, 600, 0, 0, 300, fill="black", tags="dark")
        self.canvas.create_polygon(600, 300, 600, 0, 0, 300, fill="white", tags="light")

        self.canvas.create_text(150, 100, text="Dark / Koyu", fill="white", font=("Arial", 24), tags="dark_text")
        self.canvas.create_text(450, 200, text="Light / Açık", fill="black", font=("Arial", 24), tags="light_text")

        # Bind click events
        self.canvas.tag_bind("dark", "<Button-1>", lambda e: self.select_theme("dark"))
        self.canvas.tag_bind("light", "<Button-1>", lambda e: self.select_theme("light"))
        self.canvas.tag_bind("dark_text", "<Button-1>", lambda e: self.select_theme("dark"))
        self.canvas.tag_bind("light_text", "<Button-1>", lambda e: self.select_theme("light"))

    def select_theme(self, theme):
        self.root.destroy()
        if theme == "dark":
            os.system("start pythonw main1.pyw")
        elif theme == "light":
            os.system("start pythonw main2.pyw")

if __name__ == "__main__":
    root = tk.Tk()
    app = ThemeSelectorApp(root)
    root.mainloop()
