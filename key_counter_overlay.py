#!/usr/bin/env python3
"""
Key Counter Overlay - A minimal, borderless overlay.
Left-click to increment. Right-click for menu.
"""

import tkinter as tk
from tkinter import simpledialog, colorchooser
import sys
import os

# macOS: hide from dock and menu bar
if sys.platform == 'darwin':
    try:
        from AppKit import NSApplication, NSApplicationActivationPolicyAccessory
        NSApplication.sharedApplication().setActivationPolicy_(NSApplicationActivationPolicyAccessory)
    except ImportError:
        pass


class KeyCounterOverlay:
    def __init__(self):
        self.count = 0
        self.format = self.load_config()
        self.root = tk.Tk()

        # Hide window while configuring
        self.root.withdraw()

        # Borderless - no title bar
        self.root.overrideredirect(True)

        # Transparency
        try:
            self.root.attributes("-alpha", 0.85)
        except:
            pass

        # Dark background
        self.root.configure(bg="#1a1a1a")

        # Counter label - smaller font for longer text
        self.label = tk.Label(
            self.root,
            text=self.format.format(count=0),
            font=("Helvetica", 24, "bold"),
            fg="#00ff88",
            bg="#1a1a1a",
            padx=15,
            pady=10
        )
        self.label.pack(expand=True, fill=tk.BOTH)

        # Right-click context menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Set Number...", command=self.set_number)
        self.menu.add_command(label="Reset", command=self.reset)
        self.menu.add_separator()
        self.menu.add_command(label="Text Color...", command=self.change_color)
        self.menu.add_command(label="Background Color...", command=self.change_bg_color)
        self.menu.add_command(label="Transparency...", command=self.change_transparency)
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.root.quit)

        # Mouse bindings
        self.label.bind("<Button-1>", self.on_press)
        self.label.bind("<B1-Motion>", self.on_drag)
        self.label.bind("<ButtonRelease-1>", self.on_release)
        self.label.bind("<Button-3>", self.show_menu)

        # Drag state
        self._drag_start_x = 0
        self._drag_start_y = 0
        self._dragged = False

        # Auto-size window to fit content, then center
        self.root.update_idletasks()
        width = self.label.winfo_reqwidth()
        height = self.label.winfo_reqheight()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w - width) // 2
        y = (screen_h - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Show window and ensure always on top
        self.root.deiconify()
        self.root.attributes("-topmost", True)
        self.root.lift()

        # Periodically ensure window stays on top
        self.stay_on_top()

    def load_config(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "config.txt")
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except:
            return "{count}"

    def stay_on_top(self):
        self.root.attributes("-topmost", True)
        self.root.lift()
        self.root.after(100, self.stay_on_top)

    def on_press(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y
        self._dragged = False

    def on_drag(self, event):
        self._dragged = True
        x = self.root.winfo_x() + event.x - self._drag_start_x
        y = self.root.winfo_y() + event.y - self._drag_start_y
        self.root.geometry(f"+{x}+{y}")

    def on_release(self, event):
        if not self._dragged:
            # Only increment if not dragged
            self.count += 1
            self.label.config(text=self.format.format(count=self.count))

    def reset(self):
        self.count = 0
        self.label.config(text=self.format.format(count=0))

    def set_number(self):
        result = simpledialog.askinteger("Set Number", "Enter count:",
                                          initialvalue=self.count,
                                          parent=self.root)
        if result is not None:
            self.count = result
            self.label.config(text=self.format.format(count=self.count))

    def change_color(self):
        color = colorchooser.askcolor(title="Choose Text Color",
                                       initialcolor=self.label.cget("fg"),
                                       parent=self.root)
        if color[1]:
            self.label.config(fg=color[1])

    def change_bg_color(self):
        color = colorchooser.askcolor(title="Choose Background Color",
                                       initialcolor=self.label.cget("bg"),
                                       parent=self.root)
        if color[1]:
            self.root.configure(bg=color[1])
            self.label.config(bg=color[1])

    def change_transparency(self):
        current = int(self.root.attributes("-alpha") * 100)
        result = simpledialog.askinteger("Transparency", "Enter transparency (10-100%):",
                                          initialvalue=current,
                                          minvalue=10, maxvalue=100,
                                          parent=self.root)
        if result is not None:
            self.root.attributes("-alpha", result / 100)

    def show_menu(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = KeyCounterOverlay()
    app.run()
