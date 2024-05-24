import requests
import tkinter as tk
from tkinter import ttk
import time

def fetch_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        response_json = response.json()
        response.raise_for_status()
        price = response_json["bitcoin"]["usd"]
        return price
    except requests.exceptions.RequestException as e:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Error fetching data: {e}")

def update_price():
    price = fetch_price()
    if price is not None:
        price_label.config(text=f"Current Bitcoin Price: ${price:,.2f}")
    else:
        root.after(2000, update_price)

def refresh_price():
    price = fetch_price()
    if price is not None:
        price_label.config(text=f"Current Bitcoin Price: ${price:,.2f}")
    else:
        price_label.config(text="Error fetching price")

root = tk.Tk()
root.title("Bitcoin Price")

price_label = ttk.Label(root, text="Fetching price...", font = ("Helvetica", 16))
price_label.pack(pady = 20)

refresh_button = ttk.Button(root, text="Refresh", command=update_price)
refresh_button.pack(pady=20)

update_price()

root.mainloop()
