import tkinter as tk
from tkinter import ttk
import re
from datetime import datetime

FILE_PATH = "/home/aparichit/Desktop/ObsidianVaults/Sem6vault/Tracking/TODOS.md"
MARKER = "---"

TODO_PATTERN = re.compile(r"- \[( |x)\] (.*?) - \((.*?)\)")


def format_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        return dt.strftime("%d %b %Y  %I:%M %p")
    except ValueError:
        return date_str


def parse_file():
    todos = []
    lines = []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if line.strip() == MARKER:
                break
            lines.append(line)

            m = TODO_PATTERN.match(line.strip())
            if m:
                checked, text, date = m.groups()
                todos.append({
                    "line_index": idx,
                    "checked": checked == "x",
                    "text": text,
                    "date": date
                })

    return todos, lines


def update_file(todos, lines):
    for t in todos:
        mark = "x" if t["checked"] else " "
        lines[t["line_index"]] = (
            f"- [{mark}] {t['text']} - ({t['date']})\n"
        )

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)
        f.write(MARKER + "\n")


def show_ui():
    todos, lines = parse_file()

    root = tk.Tk()
    root.title("TODOs")
    root.configure(bg="#020617")

    root.geometry(f"720x{root.winfo_screenheight()}")
    root.bind("<Escape>", lambda e: root.destroy())

    header = tk.Label(
        root,
        text="Tasks",
        font=("JetBrains Mono", 16, "bold"),
        fg="#38bdf8",
        bg="#020617"
    )
    header.pack(anchor="w", padx=20, pady=12)

    container = tk.Frame(root, bg="#020617")
    container.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    canvas = tk.Canvas(container, bg="#020617", highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    content = tk.Frame(canvas, bg="#020617")

    content.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=content, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # --- Touchpad / mouse wheel scrolling ---
    def _on_mousewheel(event):
        if event.delta:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            canvas.yview_scroll(int(event.num == 5) - int(event.num == 4), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    canvas.bind_all("<Button-4>", _on_mousewheel)
    canvas.bind_all("<Button-5>", _on_mousewheel)
    # ---------------------------------------

    def toggle():
        update_file(todos, lines)

    for t in todos:
        block = tk.Frame(content, bg="#020617")
        block.pack(fill="x", pady=10)

        var = tk.BooleanVar(value=t["checked"])

        def make_cmd(todo=t, v=var):
            def _cmd():
                todo["checked"] = v.get()
                toggle()
            return _cmd

        top = tk.Frame(block, bg="#020617")
        top.pack(anchor="w")

        cb = ttk.Checkbutton(
            top,
            variable=var,
            command=make_cmd()
        )
        cb.pack(side="left", padx=(0, 8))

        date = tk.Label(
            top,
            text=format_date(t["date"]),
            font=("JetBrains Mono", 9),
            fg="#94a3b8",
            bg="#020617"
        )
        date.pack(side="left")

        text = tk.Label(
            block,
            text=t["text"],
            font=("JetBrains Mono", 11),
            fg="#e5e7eb",
            bg="#020617",
            wraplength=640,
            justify="left"
        )
        text.pack(anchor="w", padx=26, pady=(2, 0))

    root.mainloop()


if __name__ == "__main__":
    show_ui()
