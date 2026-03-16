import sqlite3
import tkinter as tk
import webbrowser

DATABASE_FILE = 'airbnb.db'
TABLE_NAME = 'listings'

COLUMNS = ['id', 'name', 'host_name', 'neighbourhood', 'room_type', 'price', 'number_of_reviews', 'url']


def fetch_all(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT {', '.join(COLUMNS)} FROM {table_name}")
    rows = cursor.fetchall()
    conn.close()
    return rows


class ListingViewer(tk.Tk):
    def __init__(self, rows):
        super().__init__()
        self.title("Airbnb Listing Viewer")
        self.geometry("900x600")
        self.rows = rows
        self._build_ui()

    def _build_ui(self):
        # Left panel: scrollable list
        left = tk.Frame(self, width=300)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(8, 0), pady=8)
        left.pack_propagate(False)

        tk.Label(left, text="Listings", font=("Helvetica", 12, "bold")).pack(anchor="w")

        scrollbar = tk.Scrollbar(left, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(left, yscrollcommand=scrollbar.set, activestyle="dotbox", selectmode=tk.SINGLE)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        for row in self.rows:
            self.listbox.insert(tk.END, f"#{row[0]}  {row[1][:40]}")

        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        # Right panel: detail view
        right = tk.Frame(self)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=8, pady=8)

        tk.Label(right, text="Listing Details", font=("Helvetica", 12, "bold")).pack(anchor="w")

        self.detail_frame = tk.Frame(right)
        self.detail_frame.pack(fill=tk.BOTH, expand=True, pady=(4, 0))

        self.detail_labels = {}
        for col in COLUMNS:
            row_frame = tk.Frame(self.detail_frame)
            row_frame.pack(fill=tk.X, pady=2)
            tk.Label(row_frame, text=f"{col}:", width=18, anchor="w", font=("Helvetica", 10, "bold")).pack(side=tk.LEFT)
            if col == 'url':
                val_label = tk.Label(row_frame, text="", anchor="w", wraplength=500, justify=tk.LEFT,
                                     fg="blue", cursor="hand2", font=("Helvetica", 10, "underline"))
                val_label.bind("<Button-1>", lambda _, lbl=val_label: webbrowser.open(lbl.cget("text")))
            else:
                val_label = tk.Label(row_frame, text="", anchor="w", wraplength=500, justify=tk.LEFT)
            val_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
            self.detail_labels[col] = val_label

        # Top panel: Filter view
        

    def _on_select(self, _):
        selection = self.listbox.curselection()
        if not selection:
            return
        row = self.rows[selection[0]]
        for i, col in enumerate(COLUMNS):
            self.detail_labels[col].config(text=str(row[i]))


if __name__ == "__main__":
    rows = fetch_all(DATABASE_FILE, TABLE_NAME)
    app = ListingViewer(rows)
    app.mainloop()
