import tkinter as tk
import csv
import datetime
import time
import threading
import math
from utils import get_heart_rate

class HeartApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-transparentcolor', 'black')
        self.root.geometry('150x150+100+100')

        # 中键拖拽功能
        self.drag_start = (0, 0)
        self.root.bind("<Button-2>", self.start_drag)  # 中键按下
        self.root.bind("<B2-Motion>", self.on_drag)    # 中键拖动

        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.heart_rate = "00"
        self.scale = 1.0
        self.scaling = 0.03
        self.animating = True

        self.update_animation()
        self.start_heart_rate_monitor()

    def start_drag(self, event):
        self.drag_start = (event.x_root, event.y_root)

    def on_drag(self, event):
        dx = event.x_root - self.drag_start[0]
        dy = event.y_root - self.drag_start[1]
        x = self.root.winfo_x() + dx
        y = self.root.winfo_y() + dy
        self.root.geometry(f"+{x}+{y}")
        self.drag_start = (event.x_root, event.y_root)

    def draw_heart(self, scale):
        self.canvas.delete("all")
        w, h = 150, 150
        
        points = []
        for t in range(0, 628, 2):
            t = t / 100
            x = 16 * (math.sin(t)**3)
            y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            px = w/2 + x * 2 * scale
            py = h/2 + y * 2 * scale
            points.extend([px, py])
        
        self.canvas.create_polygon(
            *points,
            fill='#FF3366',
            outline='#CC0033',
            smooth=True,
            splinesteps=32,
            width=0
        )

        self.canvas.create_text(
            w/2, h/2,
            text=self.heart_rate,
            fill='white',
            font=('Arial', int(24 * scale), 'bold'),
            anchor='center'
        )

    def update_animation(self):
        if self.animating:
            self.scale += self.scaling
            if self.scale > 1.15 or self.scale < 0.95:
                self.scaling *= -1
            
            self.draw_heart(self.scale)
            self.root.after(50, self.update_animation)

    def update_heart_rate(self, new_rate):
        # 只有当新数据有效时更新
        if new_rate is not None:
            self.heart_rate = new_rate.zfill(2)
            with open('heart.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.datetime.now().isoformat(),
                    new_rate
                ])

    def start_heart_rate_monitor(self):
        def monitor():
            while True:
                try:
                    hr = get_heart_rate()
                    # 过滤None值
                    if hr is not None:
                        self.root.after(0, self.update_heart_rate, str(hr))
                except Exception as e:
                    print(f"Error: {e}")
                time.sleep(2)
        
        thread = threading.Thread(target=monitor, daemon=True)
        thread.start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    with open('heart.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'heart_rate'])
    app = HeartApp()
    app.run()