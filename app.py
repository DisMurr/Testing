import tkinter as tk
from tkinter import ttk
from models import run_model  # uses the default (single) model

def run_once(event=None):
    prompt = prompt_entry.get().strip()
    query = query_entry.get().strip()
    if not prompt:
        output_box.config(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("end", "Please type a prompt.")
        output_box.config(state="normal")
        return
    text = run_model(prompt, user_query=query)
    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("end", text)
    output_box.config(state="normal")

# --- Minimal UI ---
root = tk.Tk()
root.title("One-Model Starter App")
root.geometry("640x360")

ttk.Label(root, text="Prompt").pack(anchor="w", padx=10, pady=(10, 0))
prompt_entry = ttk.Entry(root)
prompt_entry.pack(fill="x", padx=10, pady=4)
prompt_entry.insert(0, "a robot")

ttk.Label(root, text="Query (optional)").pack(anchor="w", padx=10)
query_entry = ttk.Entry(root)
query_entry.pack(fill="x", padx=10, pady=(2, 6))

btn_row = ttk.Frame(root); btn_row.pack(fill="x", padx=10, pady=(0, 6))
ttk.Button(btn_row, text="Run (Enter)", command=run_once).pack(side="left")

ttk.Label(root, text="Output").pack(anchor="w", padx=10)
output_box = tk.Text(root, height=8, wrap="word")
output_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))

prompt_entry.bind("<Return>", run_once)
query_entry.bind("<Return>", run_once)

root.mainloop()
