import tkinter as tk
from tkinter import ttk, messagebox
import time
import subprocess
import os
import webbrowser

class ModernGUI:
    def __init__(self):
        self.setup_main_window()
        
    def setup_main_window(self):
        self.window = tk.Tk()
        self.window.title("SMS Tufani")
        self.window.geometry("400x300")
        self.window.configure(bg='#f0f0f0')
        
        # Center window on screen
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 300) // 2
        self.window.geometry(f"400x300+{x}+{y}")
        
        self.window.attributes("-alpha", 0)
        self.create_main_widgets()
        self.fade_in(self.window)

    def create_main_widgets(self):
        # Style configuration
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 12), background='#f0f0f0')
        style.configure('TButton', font=('Helvetica', 11), padding=10)
        
        # Main frame
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(expand=True, fill='both')
        
        # Title with custom font and styling
        title_label = ttk.Label(
            main_frame, 
            text="Welcome / Hoşgeldiniz", 
            font=('Helvetica', 18, 'bold'),
            style='TLabel'
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle = ttk.Label(
            main_frame,
            text="Please select your language",
            font=('Helvetica', 10),
            style='TLabel'
        )
        subtitle.pack(pady=5)
        
        # Button frame for better organization
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # Enhanced buttons with hover effect
        self.create_hover_button(button_frame, "English", lambda: self.open_second_window("English"))
        self.create_hover_button(button_frame, "Turkish", lambda: self.open_second_window("Turkish"))

        # Create TikTok link with blinking effect
        self.tiktok_label = tk.Label(
            main_frame,
            text="tiktok.com/@unknown_napim",
            font=('Helvetica', 10),
            fg='black',
            bg='#f0f0f0',
            cursor='hand2'
        )
        self.tiktok_label.pack(pady=(20, 5))
        self.tiktok_label.bind('<Button-1>', lambda e: webbrowser.open('https://tiktok.com/@unknown_napim'))
        
        # Creator credit
        creator_label = tk.Label(
            main_frame,
            text="Made by Unknown Destroyer / Unknown Destroyer tarafından yapıldı",
            font=('Helvetica', 8),
            fg='gray',
            bg='#f0f0f0'
        )
        creator_label.pack(pady=5)
        
        # Version label with transparency
        version_label = tk.Label(
            main_frame,
            text="SMSTufani 2.3 EX - Beta",
            font=('Helvetica', 8),
            fg='gray',
            bg='#f0f0f0'
        )
        version_label.pack(pady=5)
        
        # Start blinking animation for TikTok label
        self.blink_tiktok_label()

    def blink_tiktok_label(self):
        current_color = self.tiktok_label.cget("fg")
        new_color = "white" if current_color == "black" else "black"
        self.tiktok_label.configure(fg=new_color)
        self.window.after(500, self.blink_tiktok_label)  # Blink every 500ms

    def create_hover_button(self, parent, text, command):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=('Helvetica', 11),
            bg='#2196F3',
            fg='white',
            activebackground='#1976D2',
            activeforeground='white',
            width=20,
            height=2,
            border=0,
            cursor='hand2'
        )
        btn.pack(pady=5)
        
        # Hover effects
        btn.bind('<Enter>', lambda e: btn.configure(bg='#1976D2'))
        btn.bind('<Leave>', lambda e: btn.configure(bg='#2196F3'))

    def open_second_window(self, language):
        self.fade_out(self.window)
        self.window.withdraw()

        second_window = tk.Toplevel()
        second_window.title("Configuration")
        second_window.geometry("450x500")
        second_window.configure(bg='#f0f0f0')
        
        # Center the second window
        screen_width = second_window.winfo_screenwidth()
        screen_height = second_window.winfo_screenheight()
        x = (screen_width - 450) // 2
        y = (screen_height - 500) // 2
        second_window.geometry(f"450x500+{x}+{y}")
        
        self.fade_in(second_window)

        # Variables for checkboxes
        options = {
            'hide_number': tk.BooleanVar(),
            'skip_agreements': tk.BooleanVar(),
            'skip_animations': tk.BooleanVar()
        }

        # Main frame for second window
        main_frame = ttk.Frame(second_window, padding="20")
        main_frame.pack(expand=True, fill='both')

        # Title for second window
        title = ttk.Label(
            main_frame,
            text="Configuration Settings" if language == "English" else "Yapılandırma Ayarları",
            font=('Helvetica', 16, 'bold')
        )
        title.pack(pady=(0, 20))

        # Create option frames
        self.create_option_frame(
            main_frame,
            "Hide Number" if language == "English" else "Numarayı Gizle",
            "Do you want to hide the number?" if language == "English" else "Numarayı gizlemek ister misiniz?",
            options['hide_number']
        )
        
        self.create_option_frame(
            main_frame,
            "Skip Agreements" if language == "English" else "Anlaşmaları Atla",
            "Do you want to skip agreements?" if language == "English" else "Anlaşmaları atlamak ister misiniz?",
            options['skip_agreements']
        )
        
        self.create_option_frame(
            main_frame,
            "Skip Animations" if language == "English" else "Animasyonları Atla",
            "Do you want to skip animations?" if language == "English" else "Animasyonları geçmek ister misiniz?",
            options['skip_animations']
        )

        # Confirm button with modern styling
        confirm_btn = tk.Button(
            main_frame,
            text="Confirm" if language == "English" else "Onayla",
            command=lambda: self.confirm_settings(second_window, language, options),
            font=('Helvetica', 12),
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049',
            activeforeground='white',
            width=20,
            height=2,
            border=0,
            cursor='hand2'
        )
        confirm_btn.pack(pady=20)
        
        # Hover effects for confirm button
        confirm_btn.bind('<Enter>', lambda e: confirm_btn.configure(bg='#45a049'))
        confirm_btn.bind('<Leave>', lambda e: confirm_btn.configure(bg='#4CAF50'))

    def create_option_frame(self, parent, title, description, var):
        frame = ttk.Frame(parent)
        frame.pack(fill='x', pady=10, padx=5)
        
        ttk.Label(
            frame,
            text=title,
            font=('Helvetica', 12, 'bold')
        ).pack(anchor='w')
        
        ttk.Label(
            frame,
            text=description,
            font=('Helvetica', 10)
        ).pack(anchor='w', pady=(0, 5))
        
        ttk.Checkbutton(
            frame,
            variable=var,
            style='Switch.TCheckbutton'
        ).pack(anchor='w')

    def confirm_settings(self, window, language, options):
        self.fade_out(window)
        time.sleep(0.5)
        try:
            script_name = self.get_script_name(language, options)
            
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
            window.quit()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred: {str(e)}"
            )
            window.quit()

    def get_script_name(self, language, options):
        prefix = "smstufani"
        lang_code = "en" if language == "English" else "tr"
        
        components = []
        if options['hide_number'].get():
            components.append("hided")
        if options['skip_agreements'].get():
            components.append("skip")
        if options['skip_animations'].get():
            components.append("anim")
            
        if not components:
            return None
            
        return f"{prefix}{lang_code}{''.join(components)}.py"

    def fade_in(self, window):
        for i in range(0, 11):
            window.attributes("-alpha", i / 10)
            time.sleep(0.03)
            window.update()

    def fade_out(self, window):
        for i in range(10, -1, -1):
            window.attributes("-alpha", i / 10)
            time.sleep(0.03)
            window.update()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ModernGUI()
    app.run()
