import customtkinter as ctk

def fetch_star_rating():
    yards = float(entry.get())
    tds = float(entry2.get())
    ints = float(entry3.get())
    team_wins = float(entry4.get())

    c1 = 0
    if yards > 3000:
        c1 += 2
    if yards >= 3700:
        c1 += 1
    if yards >= 4300:
        c1 += 1
    if yards >= 5000:
        c1 += 1

    c2 = 0
    if tds >= 18:
        c2 += 2
    if tds >= 26:
        c2 += 1
    if tds >= 32:
        c2 += 1
    if tds >= 40:
        c2 += 1

    c3 = 5
    if ints >= 25:
        c3 -= 1
    if ints >= 18:
        c3 -= 1
    if ints >= 13:
        c3 -= 1
    if ints >= 9:
        c3 -= 1

    c4 = 1
    if team_wins >= 4:
        c4 += 1
    if team_wins >= 8:
        c4 += 1
    if team_wins >= 12:
        c4 += 1
    if team_wins >= 14:
        c4 += 1

    n = c1 + c2 + c3 + c4
    stars = n / 4

    result_label.configure(text=f"Stars: {stars:.2f}")

def clear_entry(event, entry):
    if entry.get() == "Yards" or entry.get() == "TDs" or entry.get() == "Ints" or entry.get() == "TeamWins":
        entry.delete(0, ctk.END)

root = ctk.CTk()
root.geometry("380x400")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=70, padx=130, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="THE DPFF", text_color="blue")
label.pack(padx=25, pady=10)

entry = ctk.CTkEntry(master=root, placeholder_text="Yards")
entry.pack(padx=20, pady=5)
entry.bind("<FocusIn>", lambda event: clear_entry(event, entry))

entry2 = ctk.CTkEntry(master=root, placeholder_text="TDs")
entry2.pack(padx=20, pady=5)
entry2.bind("<FocusIn>", lambda event: clear_entry(event, entry2))

entry3 = ctk.CTkEntry(master=root, placeholder_text="Ints")
entry3.pack(padx=20, pady=5)
entry3.bind("<FocusIn>", lambda event: clear_entry(event, entry3))

entry4 = ctk.CTkEntry(master=root, placeholder_text="TeamWins")
entry4.pack(padx=20, pady=5)
entry4.bind("<FocusIn>", lambda event: clear_entry(event, entry4))

button = ctk.CTkButton(master=root, text="DPFF Score", command=fetch_star_rating)
button.pack(padx=25, pady=5)

result_label = ctk.CTkLabel(master=root, text="Stars: ")
result_label.pack()

root.mainloop()
