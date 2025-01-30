import tkinter as tk
from tkinter import ttk, messagebox
import time
import subprocess
import os
import webbrowser
from math import sin, cos, pi
import colorsys

class ModernGUI:
    def __init__(self):
        self.animation_frame = 0
        self.gradient_hue = 0
        self.title_hue = 0
        self.setup_main_window()
        
    def setup_main_window(self):
        self.window = tk.Tk()
        self.window.title("SMSTufanı 2.3 EX-BETA")
        self.window.geometry("500x400")
        self.window.configure(bg='#1a1a1a')  # Dark theme
        
        # Make window draggable from anywhere
        self.window.bind("<Button-1>", self.start_move)
        self.window.bind("<ButtonRelease-1>", self.stop_move)
        self.window.bind("<B1-Motion>", self.do_move)
        
        # Center window on screen with blur effect
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 500) // 2
        y = (screen_height - 400) // 2
        self.window.geometry(f"500x400+{x}+{y}")
        
        # Create canvas for custom drawing
        self.canvas = tk.Canvas(self.window, bg='#1a1a1a', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        
        self.window.attributes("-alpha", 0)
        self.create_main_widgets()
        self.fade_in(self.window)
        
        # Start animation loop
        self.animate_background()

    def create_main_widgets(self):
        # Create floating effect container
        self.container = tk.Frame(self.canvas, bg='#2d2d2d', padx=30, pady=30)
        self.container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Animated title with gradient effect
        self.title_label = tk.Label(
            self.container,
            text="SMS Tufani",
            font=('Helvetica', 24, 'bold'),
            bg='#2d2d2d',
            fg='#ffffff'
        )
        self.title_label.pack(pady=(0, 20))
        self.animate_title_color()
        
        # Subtitle with typing animation
        self.subtitle = tk.Label(
            self.container,
            text="",
            font=('Helvetica', 12),
            bg='#2d2d2d',
            fg='#cccccc'
        )
        self.subtitle.pack(pady=(0, 30))
        self.type_text("Select Your Language / Dilinizi Seçin", self.subtitle)
        
        # Modern button frame
        button_frame = tk.Frame(self.container, bg='#2d2d2d')
        button_frame.pack(pady=20)
        
        # Enhanced buttons with pulse effect
        self.create_modern_button(button_frame, "English", lambda: self.open_second_window("English"))
        self.create_modern_button(button_frame, "Turkish", lambda: self.open_second_window("Turkish"))
        
        # Animated social link
        self.social_frame = tk.Frame(self.container, bg='#2d2d2d')
        self.social_frame.pack(pady=20)
        
        self.tiktok_button = tk.Label(
            self.social_frame,
            text="Made by Unknown Destroyer / Unknown Destroyer tarafından yapıldı",
            font=('Helvetica', 10),
            fg='#4a9eff',
            bg='#2d2d2d',
            cursor='hand2'
        )
        self.tiktok_button.pack()
        self.tiktok_button.bind('<Button-1>', lambda e: webbrowser.open('https://tiktok.com/@unknown_napim'))
        self.tiktok_button.bind('<Enter>', self.on_social_hover)
        self.tiktok_button.bind('<Leave>', self.on_social_leave)
        
        # Version with glow effect
        self.version_label = tk.Label(
            self.container,
            text="v2.3 EX - Beta",
            font=('Helvetica', 8),
            bg='#2d2d2d',
            fg='#666666'
        )
        self.version_label.pack(pady=(20, 0))
        
        # Start floating animation
        self.float_widgets()

    def create_modern_button(self, parent, text, command):
        frame = tk.Frame(parent, bg='#2d2d2d')
        frame.pack(pady=5)
        
        btn = tk.Label(
            frame,
            text=text,
            font=('Helvetica', 12),
            bg='#4a9eff',
            fg='white',
            padx=30,
            pady=10,
            cursor='hand2'
        )
        btn.pack()
        
        # Create hover and click effects
        def on_enter(e):
            btn.configure(bg='#3a8eff')
            self.pulse_animation(btn)
            
        def on_leave(e):
            btn.configure(bg='#4a9eff')
            
        def on_click(e):
            btn.configure(bg='#2a7eff')
            self.window.after(100, command)
        
        btn.bind('<Enter>', on_enter)
        btn.bind('<Leave>', on_leave)
        btn.bind('<Button-1>', on_click)
        
        return btn

    def type_text(self, text, label, index=0):
        if index < len(text):
            label.config(text=text[:index + 1])
            self.window.after(50, lambda: self.type_text(text, label, index + 1))

    def float_widgets(self):
        self.animation_frame += 0.05
        offset = sin(self.animation_frame) * 3
        self.container.place_configure(rely=0.5 + offset/100)
        self.window.after(50, self.float_widgets)

    def animate_background(self):
        self.gradient_hue = (self.gradient_hue + 0.001) % 1.0
        color = self.get_gradient_color(self.gradient_hue)
        self.canvas.configure(bg=color)
        self.window.after(50, self.animate_background)

    def animate_title_color(self):
        self.title_hue = (self.title_hue + 0.005) % 1.0
        rgb = colorsys.hsv_to_rgb(self.title_hue, 0.7, 1.0)
        color = f'#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}'
        self.title_label.configure(fg=color)
        self.window.after(50, self.animate_title_color)

    def get_gradient_color(self, hue):
        rgb = colorsys.hsv_to_rgb(hue, 0.1, 0.15)
        return f'#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}'

    def pulse_animation(self, widget, size=1.0, growing=True):
        if not hasattr(widget, '_pulse_active'):
            widget._pulse_active = True
            if growing and size < 1.1:
                size += 0.01
                widget.configure(font=('Helvetica', int(12 * size)))
                self.window.after(20, lambda: self.pulse_animation(widget, size, size < 1.1))
            elif not growing and size > 1.0:
                size -= 0.01
                widget.configure(font=('Helvetica', int(12 * size)))
                self.window.after(20, lambda: self.pulse_animation(widget, size, False))
            else:
                widget._pulse_active = False
                widget.configure(font=('Helvetica', 12))

    def on_social_hover(self, event):
        self.tiktok_button.configure(fg='#5aafff')
        self.pulse_animation(self.tiktok_button)

    def on_social_leave(self, event):
        self.tiktok_button.configure(fg='#4a9eff')

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry(f"+{x}+{y}")

    def open_second_window(self, language):
        self.fade_out(self.window)
        self.window.withdraw()
        
        config_window = ConfigWindow(language, self)
        config_window.run()

    def fade_in(self, window):
        for i in range(0, 21):
            window.attributes("-alpha", i / 20)
            window.update()
            time.sleep(0.02)

    def fade_out(self, window):
        for i in range(20, -1, -1):
            window.attributes("-alpha", i / 20)
            window.update()
            time.sleep(0.02)

    def run(self):
        self.window.mainloop()

class ConfigWindow:
    def __init__(self, language, parent):
        self.language = language
        self.parent = parent
        self.setup_window()
        
    def setup_window(self):
        self.window = tk.Tk()
        self.window.title("Configuration")
        self.window.geometry("600x500")
        self.window.configure(bg='#1a1a1a')
        
        # Center window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 600) // 2
        y = (screen_height - 500) // 2
        self.window.geometry(f"600x500+{x}+{y}")
        
        self.create_widgets()
        self.window.attributes("-alpha", 0)
        self.fade_in()
        
    def create_widgets(self):
        # Main container with glass effect
        container = tk.Frame(self.window, bg='#2d2d2d', padx=40, pady=40)
        container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Title with animation
        title = tk.Label(
            container,
            text="Configuration Settings" if self.language == "English" else "Yapılandırma Ayarları",
            font=('Helvetica', 20, 'bold'),
            bg='#2d2d2d',
            fg='white'
        )
        title.pack(pady=(0, 30))
        
        # Options with smooth transitions
        self.options = {
            'hide_number': tk.BooleanVar(),
            'skip_agreements': tk.BooleanVar(),
            'skip_animations': tk.BooleanVar()
        }
        
        option_data = [
            {
                'name': 'hide_number',
                'title': "Hide Number" if self.language == "English" else "Numarayı Gizle",
                'desc': "Do you want to hide the number?" if self.language == "English" else "Numarayı gizlemek ister misiniz?"
            },
            {
                'name': 'skip_agreements',
                'title': "Skip Agreements" if self.language == "English" else "Anlaşmaları Atla",
                'desc': "Do you want to skip agreements?" if self.language == "English" else "Anlaşmaları atlamak ister misiniz?"
            },
            {
                'name': 'skip_animations',
                'title': "Skip Animations" if self.language == "English" else "Animasyonları Atla",
                'desc': "Do you want to skip animations?" if self.language == "English" else "Animasyonları geçmek ister misiniz?"
            }
        ]
        
        for opt in option_data:
            self.create_option_widget(container, opt)
            
        # Modern confirm button
        confirm_text = "Confirm" if self.language == "English" else "Onayla"
        self.confirm_btn = tk.Label(
            container,
            text=confirm_text,
            font=('Helvetica', 12),
            bg='#4CAF50',
            fg='white',
            padx=40,
            pady=12,
            cursor='hand2'
        )
        self.confirm_btn.pack(pady=30)
        
        # Button effects
        self.confirm_btn.bind('<Enter>', lambda e: (
            self.confirm_btn.configure(bg='#45a049'),
            self.pulse_animation(self.confirm_btn)
        ))
        self.confirm_btn.bind('<Leave>', lambda e: self.confirm_btn.configure(bg='#4CAF50'))
        self.confirm_btn.bind('<Button-1>', self.confirm_settings)

    def create_option_widget(self, parent, option_data):
        frame = tk.Frame(parent, bg='#2d2d2d')
        frame.pack(fill='x', pady=10)
        
        title = tk.Label(
            frame,
            text=option_data['title'],
            font=('Helvetica', 12, 'bold'),
            bg='#2d2d2d',
            fg='white'
        )
        title.pack(anchor='w')
        
        desc = tk.Label(
            frame,
            text=option_data['desc'],
            font=('Helvetica', 10),
            bg='#2d2d2d',
            fg='#cccccc'
        )
        desc.pack(anchor='w', pady=(0, 5))
        
        # Custom toggle switch
        switch_frame = tk.Frame(frame, bg='#2d2d2d')
        switch_frame.pack(anchor='w')
        
        switch = tk.Label(
            switch_frame,
            text='●',
            font=('Helvetica', 16),
            bg='#2d2d2d',
            fg='#666666',
            cursor='hand2'
        )
        switch.pack(side='left')
        
        def toggle(e):
            current = self.options[option_data['name']].get()
            self.options[option_data['name']].set(not current)
            switch.configure(fg='#4a9eff' if not current else '#666666')
            self.pulse_animation(switch)
            
        switch.bind('<Button-1>', toggle)

    def pulse_animation(self, widget, size=1.0, growing=True):
        if not hasattr(widget, '_pulse_active'):
            widget._pulse_active = True
            if growing and size < 1.1:
                size += 0.01
                widget.configure(font=('Helvetica', int(12 * size)))
                self.window.after(20, lambda: self.pulse_animation(widget, size, size < 1.1))
            elif not growing and size > 1.0:
                size -= 0.01
                widget.configure(font=('Helvetica', int(12 * size)))
                self.window.after(20, lambda: self.pulse_animation(widget, size, False))
            else:
                widget._pulse_active = False
                widget.configure(font=('Helvetica', 12))

    def confirm_settings(self, event):
        self.fade_out()
        time.sleep(0.5)
        try:
            script_name = self.get_script_name()
            
            if script_name:
                if os.path.exists(script_name):
                    subprocess.Popen(
                        ["python", script_name],
                        creationflags=subprocess.CREATE_NEW_CONSOLE
                    )
                else:
                    messagebox.showerror(
                        "Error",
                        f"Script file not found: {script_name}"
                    )
            self.window.quit()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred: {str(e)}"
            )
            self.window.quit()

    def get_script_name(self):
        prefix = "smstufani"
        lang_code = "en" if self.language == "English" else "tr"
        
        components = []
        if self.options['hide_number'].get():
            components.append("hided")
        if self.options['skip_agreements'].get():
            components.append("skip")
        if self.options['skip_animations'].get():
            components.append("anim")
            
        if not components:
            return f"{prefix}{lang_code}.py"  # Default script name when no options selected
            
        return f"{prefix}{lang_code}{''.join(components)}.py"

    def fade_in(self):
        for i in range(0, 21):
            self.window.attributes("-alpha", i / 20)
            self.window.update()
            time.sleep(0.02)

    def fade_out(self):
        for i in range(20, -1, -1):
            self.window.attributes("-alpha", i / 20)
            self.window.update()
            time.sleep(0.02)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ModernGUI()
    app.run()
