#!/usr/bin/env python3
"""
Key Counter Overlay - A minimal, borderless overlay.
Left-click to increment. Right-click for menu.
"""

import tkinter as tk
from tkinter import simpledialog, colorchooser
import sys
import os
import time

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

        # Timer state
        self.timer_visible = False
        self.timer_running = False
        self.timer_start_time = 0
        self.timer_elapsed = 0

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

        # Timer label (hidden by default)
        self.timer_label = tk.Label(
            self.root,
            text="00:00:00",
            font=("Helvetica", 16),
            fg="#ffaa00",
            bg="#1a1a1a",
            padx=15,
            pady=5
        )

        # Right-click context menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Set Number...", command=self.set_number)
        self.menu.add_command(label="Reset", command=self.reset)
        self.menu.add_separator()
        self.menu.add_command(label="Text Color...", command=self.change_color)
        self.menu.add_command(label="Font Size...", command=self.change_font_size)
        self.menu.add_command(label="Background Color...", command=self.change_bg_color)
        self.menu.add_command(label="Transparency...", command=self.change_transparency)
        self.menu.add_separator()

        # Timer submenu
        self.timer_menu = tk.Menu(self.menu, tearoff=0)
        self.timer_menu.add_command(label="Show/Hide Timer", command=self.toggle_timer)
        self.timer_menu.add_separator()
        self.timer_menu.add_command(label="Start", command=self.timer_start)
        self.timer_menu.add_command(label="Pause", command=self.timer_pause)
        self.timer_menu.add_command(label="Reset", command=self.timer_reset)
        self.menu.add_cascade(label="Timer", menu=self.timer_menu)

        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.root.quit)

        # Mouse bindings - counter label
        self.label.bind("<Button-1>", self.on_press)
        self.label.bind("<B1-Motion>", self.on_drag)
        self.label.bind("<ButtonRelease-1>", self.on_release)
        self.label.bind("<Button-3>", self.show_menu)

        # Mouse bindings - timer label (drag only, no increment)
        self.timer_label.bind("<Button-1>", self.on_timer_press)
        self.timer_label.bind("<B1-Motion>", self.on_drag)
        self.timer_label.bind("<Button-3>", self.show_menu)

        # Drag state
        self._drag_start_x = 0
        self._drag_start_y = 0
        self._dragged = False
        self._dialog_open = False

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
        if not self._dialog_open:
            self.root.attributes("-topmost", True)
            self.root.lift()
        self.root.after(100, self.stay_on_top)

    def resize_window(self):
        self.root.update_idletasks()
        width = max(self.label.winfo_reqwidth(),
                    self.timer_label.winfo_reqwidth() if self.timer_visible else 0)
        height = self.label.winfo_reqheight()
        if self.timer_visible:
            height += self.timer_label.winfo_reqheight()
        x = self.root.winfo_x()
        y = self.root.winfo_y()
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def on_press(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y
        self._dragged = False

    def on_timer_press(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

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
        self._dialog_open = True
        self.root.attributes("-topmost", False)
        result = simpledialog.askinteger("Set Number", "Enter count:",
                                          initialvalue=self.count,
                                          parent=self.root)
        self._dialog_open = False
        if result is not None:
            self.count = result
            self.label.config(text=self.format.format(count=self.count))

    def change_color(self):
        self._dialog_open = True
        self.root.attributes("-topmost", False)
        color = colorchooser.askcolor(title="Choose Text Color",
                                       initialcolor=self.label.cget("fg"),
                                       parent=self.root)
        self._dialog_open = False
        if color[1]:
            self.label.config(fg=color[1])

    def change_font_size(self):
        current_font = self.label.cget("font")
        # Get current size
        current_size = 24  # default
        if isinstance(current_font, str):
            parts = current_font.split()
            for p in parts:
                if p.isdigit():
                    current_size = int(p)
                    break

        self._dialog_open = True
        self.root.attributes("-topmost", False)
        result = simpledialog.askinteger("Font Size", "Enter font size (8-200):",
                                          initialvalue=current_size,
                                          minvalue=8, maxvalue=200,
                                          parent=self.root)
        self._dialog_open = False
        if result is not None:
            self.label.config(font=("Helvetica", result, "bold"))
            self.resize_window()

    def change_bg_color(self):
        self._dialog_open = True
        self.root.attributes("-topmost", False)
        color = colorchooser.askcolor(title="Choose Background Color",
                                       initialcolor=self.label.cget("bg"),
                                       parent=self.root)
        self._dialog_open = False
        if color[1]:
            self.root.configure(bg=color[1])
            self.label.config(bg=color[1])
            self.timer_label.config(bg=color[1])

    def change_transparency(self):
        self._dialog_open = True
        self.root.attributes("-topmost", False)
        current = int(self.root.attributes("-alpha") * 100)
        result = simpledialog.askinteger("Transparency", "Enter transparency (10-100%):",
                                          initialvalue=current,
                                          minvalue=10, maxvalue=100,
                                          parent=self.root)
        self._dialog_open = False
        if result is not None:
            self.root.attributes("-alpha", result / 100)

    def toggle_timer(self):
        self.timer_visible = not self.timer_visible
        if self.timer_visible:
            self.timer_label.pack(expand=False, fill=tk.X)
            self.update_timer_display()
        else:
            self.timer_label.pack_forget()
        self.resize_window()

    def timer_start(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_start_time = time.time() - self.timer_elapsed
            self.update_timer()
            if not self.timer_visible:
                self.toggle_timer()

    def timer_pause(self):
        if self.timer_running:
            self.timer_running = False
            self.timer_elapsed = time.time() - self.timer_start_time

    def timer_reset(self):
        self.timer_running = False
        self.timer_elapsed = 0
        self.timer_start_time = 0
        self.update_timer_display()

    def update_timer(self):
        if self.timer_running:
            self.update_timer_display()
            self.root.after(100, self.update_timer)

    def update_timer_display(self):
        if self.timer_running:
            elapsed = time.time() - self.timer_start_time
        else:
            elapsed = self.timer_elapsed
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def show_menu(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = KeyCounterOverlay()
    app.run()
