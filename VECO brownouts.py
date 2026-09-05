import re
import unicodedata
## hehe TT
import tkinter as tk
from tkinter import scrolledtext

def normalize_text(text):
    return unicodedata.normalize("NFKD", text)

## paskitaan nato ug regex, joke lang - thanks Co-Pilot sa vibes ug vibe code

def check_text():
    output_box.delete("1.0", tk.END)

    raw_text = input_box.get("1.0", tk.END)
    normalized = normalize_text(raw_text)
    lower_text = normalized.lower()

    user_place = place_entry.get().strip().lower()

    if not user_place:
        output_box.insert(tk.END, "❌ Please enter a place/barangay.\n")
        return

    if user_place not in lower_text:
        output_box.insert(tk.END, f"❌ The place '{user_place}' was NOT mentioned.\n")
        return

    date_patterns = [
        r"(sept(?:ember)?\s*\d{1,2}\s*[-–]\s*\d{1,2},?\s*\d{4})",
        r"(sept(?:ember)?\s*\d{1,2},?\s*\d{4})",
        r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",
        r"\b\d{1,2}-\d{1,2}-\d{2,4}\b"
    ]

    detected_date = "Not detected"
    for pattern in date_patterns:
        match = re.search(pattern, normalized, re.IGNORECASE)
        if match:
            detected_date = match.group(0)
            break

    time_pattern = r"\d{1,2}:\d{2}\s*[APap][Mm]\s*[-–]\s*\d{1,2}:\d{2}\s*[APap][Mm]"
    all_times = re.findall(time_pattern, normalized)

    place_entries = []

    for time_window in all_times:
        idx = normalized.find(time_window)
        block_start = max(0, idx - 400)
        block_end = idx + 400
        block = normalized[block_start:block_end]
        block_lower = block.lower()

        if user_place in block_lower:
            map_match = re.search(r"https://tinyurl\.com/\S+", block)
            map_link = map_match.group(0) if map_match else "No map link found"
            place_entries.append((time_window, map_link))

    output_box.insert(tk.END, f"📅 Date: {detected_date}\n\n")

    if place_entries:
        output_box.insert(tk.END, f"⏰ Brownout Time Windows for '{user_place}':\n\n")
        for t, link in place_entries:
            output_box.insert(tk.END, f" • {t} — {link}\n")
    else:
        output_box.insert(tk.END, f"⏰ No time windows detected for '{user_place}'.\n")


# TT again (hehe)
root = tk.Tk()
root.title("VECO Rotational Brownout Checker")
root.geometry("700x600")

place_frame = tk.Frame(root)
place_frame.pack(pady=10)

place_label = tk.Label(place_frame, text="Enter place/barangay:", font=("Arial", 14))
place_label.pack(side=tk.LEFT, padx=5)

place_entry = tk.Entry(place_frame, font=("Arial", 14), width=25)
place_entry.pack(side=tk.LEFT, padx=5)

# Label para murag official
title_label = tk.Label(root, text="Paste VECO Advisory Content Below", font=("Arial", 16, "bold"))
title_label.pack(pady=5)

# define define kunohay
input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=15, font=("Arial", 11))
input_box.pack(padx=10, pady=10)

check_button = tk.Button(root, text="Check Brownout", font=("Arial", 12), command=check_text)
check_button.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=12, font=("Arial", 11))
output_box.pack(padx=10, pady=10)

root.mainloop()
