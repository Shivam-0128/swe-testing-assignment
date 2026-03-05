import tkinter as tk
from calculator import Calculator

class QuickCalcUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Quick-Calc")
        self.root.resizable(False, False)

        self.calc = Calculator()

        # UI state
        self.current = "0"
        self.stored = None
        self.op = None  # "+", "-", "*", "/"
        self.reset_next = False

        # Display
        self.display_var = tk.StringVar(value=self.current)
        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Consolas", 22),
            justify="right",
            bd=10,
            relief="flat",
            width=16,
            state="readonly",
            readonlybackground="white",
        )
        display.grid(row=0, column=0, columnspan=4, padx=12, pady=(12, 6), ipady=10)

        # Small status line (shows stored/op)
        self.status_var = tk.StringVar(value="")
        status = tk.Label(root, textvariable=self.status_var, anchor="e", font=("Consolas", 10))
        status.grid(row=1, column=0, columnspan=4, padx=12, pady=(0, 8), sticky="we")

        # Buttons layout
        buttons = [
            ("C", 2, 0, self.clear, {"bg": "#ffd6d6"}),
            ("⌫", 2, 1, self.backspace, {"bg": "#f0f0f0"}),
            ("%", 2, 2, self.percent, {"bg": "#f0f0f0"}),
            ("÷", 2, 3, lambda: self.set_op("/"), {"bg": "#d6e6ff"}),

            ("7", 3, 0, lambda: self.add_digit("7"), {}),
            ("8", 3, 1, lambda: self.add_digit("8"), {}),
            ("9", 3, 2, lambda: self.add_digit("9"), {}),
            ("×", 3, 3, lambda: self.set_op("*"), {"bg": "#d6e6ff"}),

            ("4", 4, 0, lambda: self.add_digit("4"), {}),
            ("5", 4, 1, lambda: self.add_digit("5"), {}),
            ("6", 4, 2, lambda: self.add_digit("6"), {}),
            ("−", 4, 3, lambda: self.set_op("-"), {"bg": "#d6e6ff"}),

            ("1", 5, 0, lambda: self.add_digit("1"), {}),
            ("2", 5, 1, lambda: self.add_digit("2"), {}),
            ("3", 5, 2, lambda: self.add_digit("3"), {}),
            ("+", 5, 3, lambda: self.set_op("+"), {"bg": "#d6e6ff"}),

            ("±", 6, 0, self.toggle_sign, {"bg": "#f0f0f0"}),
            ("0", 6, 1, lambda: self.add_digit("0"), {}),
            (".", 6, 2, self.add_decimal, {}),
            ("=", 6, 3, self.equals, {"bg": "#c8ffd6"}),
        ]

        for (text, r, c, cmd, style) in buttons:
            btn = tk.Button(
                root,
                text=text,
                command=cmd,
                width=5,
                height=2,
                font=("Consolas", 16),
                bd=0,
                relief="ridge",
                **style
            )
            btn.grid(row=r, column=c, padx=6, pady=6)

        # Keyboard support
        root.bind("<Key>", self.on_key)
        self.update_display()

    def update_display(self):
        self.display_var.set(self.current)
        if self.stored is None or self.op is None:
            self.status_var.set("")
        else:
            self.status_var.set(f"{self.format_num(self.stored)}  {self.op}")

    def format_num(self, x):
        # Show int without .0
        try:
            if float(x).is_integer():
                return str(int(float(x)))
        except Exception:
            pass
        return str(x)

    def add_digit(self, d: str):
        if self.reset_next:
            self.current = "0"
            self.reset_next = False

        if self.current == "0":
            self.current = d
        else:
            self.current += d
        self.update_display()

    def add_decimal(self):
        if self.reset_next:
            self.current = "0"
            self.reset_next = False
        if "." not in self.current:
            self.current += "."
        self.update_display()

    def toggle_sign(self):
        if self.current.startswith("-"):
            self.current = self.current[1:]
        else:
            if self.current != "0":
                self.current = "-" + self.current
        self.update_display()

    def backspace(self):
        if self.reset_next:
            return
        if len(self.current) <= 1 or (self.current.startswith("-") and len(self.current) == 2):
            self.current = "0"
        else:
            self.current = self.current[:-1]
        self.update_display()

    def clear(self):
        self.current = "0"
        self.stored = None
        self.op = None
        self.reset_next = False
        self.update_display()

    def percent(self):
        # Simple percent: current becomes current/100
        try:
            val = float(self.current) / 100.0
            self.current = self.format_num(val)
        except ValueError:
            self.current = "0"
        self.update_display()

    def set_op(self, op: str):
        try:
            cur = float(self.current)
        except ValueError:
            self.current = "0"
            cur = 0.0

        # If already have stored+op, compute intermediate result first
        if self.stored is not None and self.op is not None and not self.reset_next:
            self.current = self.compute(self.stored, cur, self.op)
            try:
                cur = float(self.current)
            except ValueError:
                # error shown in display; keep state reset
                self.stored = None
                self.op = None
                self.reset_next = True
                self.update_display()
                return

        self.stored = cur
        self.op = op
        self.reset_next = True
        self.update_display()

    def equals(self):
        if self.stored is None or self.op is None:
            return
        try:
            cur = float(self.current)
        except ValueError:
            self.current = "0"
            cur = 0.0

        result = self.compute(self.stored, cur, self.op)
        self.current = result
        self.stored = None
        self.op = None
        self.reset_next = True
        self.update_display()

    def compute(self, a: float, b: float, op: str) -> str:
        try:
            if op == "+":
                return self.format_num(self.calc.add(a, b))
            if op == "-":
                return self.format_num(self.calc.subtract(a, b))
            if op == "*":
                return self.format_num(self.calc.multiply(a, b))
            if op == "/":
                return self.format_num(self.calc.divide(a, b))
        except ValueError as e:
            return "Error"
        return self.format_num(b)

    def on_key(self, event):
        k = event.keysym
        ch = event.char

        if ch.isdigit():
            self.add_digit(ch)
        elif ch == ".":
            self.add_decimal()
        elif ch in ["+", "-", "*", "/"]:
            self.set_op(ch)
        elif k in ["Return", "KP_Enter"]:
            self.equals()
        elif k in ["BackSpace"]:
            self.backspace()
        elif k in ["Escape"]:
            self.clear()

def main():
    root = tk.Tk()
    QuickCalcUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()