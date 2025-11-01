import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import base64
import webbrowser

class Base64Tool:
    def __init__(self, root):
        self.root = root
        self.root.title("ChowdhuryVai - Professional Base64 Tool")
        self.root.geometry("900x700")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(True, True)
        
        # Set hacker theme colors
        self.bg_color = '#0a0a0a'
        self.fg_color = '#00ff00'
        self.accent_color = '#0088ff'
        self.warning_color = '#ff4444'
        self.text_color = '#ffffff'
        
        self.setup_ui()
        self.create_footer()
        
    def setup_ui(self):
        # Header with branding
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(fill=tk.X, padx=20, pady=10)
        
        title_label = tk.Label(
            header_frame, 
            text="▓▒░ BASE64 ENCODER/DECODER ░▒▓", 
            font=('Courier', 20, 'bold'),
            fg=self.fg_color,
            bg=self.bg_color
        )
        title_label.pack(pady=5)
        
        subtitle_label = tk.Label(
            header_frame,
            text="PROFESSIONAL HACKING TOOL - CHOWDHURYVAI",
            font=('Courier', 10),
            fg=self.accent_color,
            bg=self.bg_color
        )
        subtitle_label.pack()
        
        # Mode selection
        mode_frame = tk.Frame(self.root, bg=self.bg_color)
        mode_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.mode_var = tk.StringVar(value="encode")
        
        encode_btn = tk.Radiobutton(
            mode_frame,
            text="ENCODE TO BASE64",
            variable=self.mode_var,
            value="encode",
            font=('Courier', 11, 'bold'),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor='#003300',
            command=self.on_mode_change
        )
        encode_btn.pack(side=tk.LEFT, padx=10)
        
        decode_btn = tk.Radiobutton(
            mode_frame,
            text="DECODE FROM BASE64",
            variable=self.mode_var,
            value="decode",
            font=('Courier', 11, 'bold'),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor='#003300',
            command=self.on_mode_change
        )
        decode_btn.pack(side=tk.LEFT, padx=10)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Input section
        input_frame = tk.LabelFrame(
            main_frame, 
            text=" INPUT ", 
            font=('Courier', 12, 'bold'),
            fg=self.fg_color,
            bg=self.bg_color,
            bd=1,
            relief=tk.SOLID
        )
        input_frame.pack(fill=tk.X, pady=10)
        
        self.input_text = scrolledtext.ScrolledText(
            input_frame, 
            height=6, 
            font=('Courier', 10),
            bg='#111111',
            fg=self.text_color,
            insertbackground=self.fg_color,
            selectbackground=self.accent_color
        )
        self.input_text.pack(fill=tk.X, padx=10, pady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=15)
        
        process_btn = tk.Button(
            buttons_frame,
            text="PROCESS",
            font=('Courier', 12, 'bold'),
            bg='#006600',
            fg='white',
            command=self.process_data,
            width=12,
            height=1
        )
        process_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            buttons_frame,
            text="CLEAR ALL",
            font=('Courier', 12, 'bold'),
            bg='#660000',
            fg='white',
            command=self.clear_all,
            width=12,
            height=1
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        copy_btn = tk.Button(
            buttons_frame,
            text="COPY RESULT",
            font=('Courier', 12, 'bold'),
            bg='#000066',
            fg='white',
            command=self.copy_result,
            width=12,
            height=1
        )
        copy_btn.pack(side=tk.LEFT, padx=5)
        
        # Output section
        output_frame = tk.LabelFrame(
            main_frame, 
            text=" OUTPUT ", 
            font=('Courier', 12, 'bold'),
            fg=self.fg_color,
            bg=self.bg_color,
            bd=1,
            relief=tk.SOLID
        )
        output_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame, 
            height=6, 
            font=('Courier', 10),
            bg='#111111',
            fg=self.text_color,
            insertbackground=self.fg_color,
            selectbackground=self.accent_color
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Statistics frame
        stats_frame = tk.Frame(main_frame, bg=self.bg_color)
        stats_frame.pack(fill=tk.X, pady=5)
        
        self.stats_label = tk.Label(
            stats_frame,
            text="Input: 0 chars | Output: 0 chars",
            font=('Courier', 9),
            fg=self.accent_color,
            bg=self.bg_color
        )
        self.stats_label.pack()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Enter text and click PROCESS")
        status_bar = tk.Label(
            self.root, 
            textvariable=self.status_var,
            font=('Courier', 10),
            fg=self.accent_color,
            bg='#111111',
            anchor=tk.W
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=5)
        
        # Bind events
        self.input_text.bind('<KeyRelease>', self.update_stats)
        
    def create_footer(self):
        footer_frame = tk.Frame(self.root, bg='#111111')
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Contact information
        contacts = [
            ("Telegram ID", "https://t.me/darkvaiadmin"),
            ("Telegram Channel", "https://t.me/windowspremiumkey"),
            ("Hacking Website", "https://crackyworld.com")
        ]
        
        contact_frame = tk.Frame(footer_frame, bg='#111111')
        contact_frame.pack(pady=8)
        
        for i, (label, url) in enumerate(contacts):
            link_label = tk.Label(
                contact_frame,
                text=label,
                font=('Courier', 9, 'underline'),
                fg=self.accent_color,
                bg='#111111',
                cursor="hand2"
            )
            link_label.pack(side=tk.LEFT, padx=15)
            link_label.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
            
        copyright_label = tk.Label(
            footer_frame,
            text="© 2024 ChowdhuryVai - Professional Security Tools",
            font=('Courier', 8),
            fg=self.fg_color,
            bg='#111111'
        )
        copyright_label.pack(pady=5)
        
    def on_mode_change(self):
        mode = self.mode_var.get()
        if mode == "encode":
            self.status_var.set("Mode: Encoding text to Base64")
        else:
            self.status_var.set("Mode: Decoding Base64 to text")
        self.update_stats()
        
    def update_stats(self, event=None):
        input_text = self.input_text.get("1.0", tk.END).strip()
        output_text = self.output_text.get("1.0", tk.END).strip()
        
        input_len = len(input_text)
        output_len = len(output_text)
        
        self.stats_label.config(text=f"Input: {input_len} chars | Output: {output_len} chars")
        
    def process_data(self):
        input_data = self.input_text.get("1.0", tk.END).strip()
        
        if not input_data:
            messagebox.showwarning("Input Error", "Please enter some text!")
            return
        
        try:
            mode = self.mode_var.get()
            
            if mode == "encode":
                # Encode to Base64
                encoded_bytes = base64.b64encode(input_data.encode('utf-8'))
                result = encoded_bytes.decode('utf-8')
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert("1.0", result)
                self.status_var.set("Successfully encoded text to Base64")
                
            else:  # decode mode
                # Add padding if necessary
                padding = 4 - len(input_data) % 4
                if padding != 4:
                    input_data += "=" * padding
                
                # Decode base64
                decoded_bytes = base64.b64decode(input_data)
                
                # Try to decode as UTF-8 text
                try:
                    decoded_text = decoded_bytes.decode('utf-8')
                    self.output_text.delete("1.0", tk.END)
                    self.output_text.insert("1.0", decoded_text)
                    self.status_var.set("Successfully decoded Base64 to text")
                    
                except UnicodeDecodeError:
                    # If it's binary data, show hex representation
                    hex_representation = decoded_bytes.hex()
                    formatted_hex = ' '.join(hex_representation[i:i+2] for i in range(0, len(hex_representation), 2))
                    self.output_text.delete("1.0", tk.END)
                    self.output_text.insert("1.0", f"Binary Data (Hex):\n{formatted_hex}")
                    self.status_var.set("Decoded binary data (displayed as hex)")
                    
        except Exception as e:
            error_msg = str(e)
            if "incorrect padding" in error_msg.lower():
                messagebox.showerror("Decoding Error", "Invalid Base64 format! Check your input.")
            else:
                messagebox.showerror("Processing Error", f"Operation failed: {error_msg}")
            self.status_var.set("Error processing data")
        
        self.update_stats()
    
    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.status_var.set("Cleared all fields")
        self.update_stats()
    
    def copy_result(self):
        result = self.output_text.get("1.0", tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            self.status_var.set("Result copied to clipboard")
            messagebox.showinfo("Success", "Result copied to clipboard!")
        else:
            messagebox.showwarning("Copy Error", "No result to copy!")

def main():
    try:
        root = tk.Tk()
        app = Base64Tool(root)
        
        # Center the window
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        root.geometry('+{}+{}'.format(x, y))
        
        root.mainloop()
    except Exception as e:
        print(f"Application error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
