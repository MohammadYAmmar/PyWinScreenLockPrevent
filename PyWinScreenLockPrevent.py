import tkinter as tk
import pyautogui
import threading
import time

# Shared variable to control the thread
is_prevention_active = False

# Function to start screen lock prevention
def start_lock_prevention():
    global is_prevention_active
    is_prevention_active = True
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    
    def prevent_lock():
        while is_prevention_active:
            try:
                # Move the mouse cursor slightly
                # pyautogui.move(1, 1)
                # pyautogui.move(50, 50)
                # pyautogui.move(-1, -1)

                # Press the spacebar key
                # pyautogui.press('space')

                # Simulate pressing the Escape (Esc) key
                # pyautogui.press('esc')

                # Simulate pressing the Escape (F) key
                pyautogui.press('F')
                pyautogui.press('backspace')

                # Print a message for debug
                print("Action happen.")
                
                # Sleep for the specified interval (in seconds)
                time.sleep(interval)
            
            except KeyboardInterrupt:
                break

    # Start the thread
    global lock_prevention_thread
    lock_prevention_thread = threading.Thread(target=prevent_lock)
    lock_prevention_thread.daemon = True
    lock_prevention_thread.start()

# Function to stop screen lock prevention
def stop_lock_prevention():
    global is_prevention_active
    is_prevention_active = False
    if lock_prevention_thread.is_alive():
        lock_prevention_thread.join()
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Screen Lock Prevention")
# window.geometry("300x200")  # Adjusted window size
window.geometry("500x200")  # Adjusted window size

# Create labels
label = tk.Label(window, text="Click 'Start' to prevent screen lock.")
label.pack(pady=10)

# Create Start button
start_button = tk.Button(window, text="Start", command=start_lock_prevention)
start_button.pack(pady=5)

# Create Stop button (initially disabled)
stop_button = tk.Button(window, text="Stop", command=stop_lock_prevention, state=tk.DISABLED)
stop_button.pack(pady=5)

# Set the interval (in seconds) to move the mouse cursor
# interval = 300  # 5 minutes
interval = 60  # 1 minute

# Define the delay in milliseconds (e.g., 3000 milliseconds = 3 seconds)
# delay_ms = 60000

# Schedule the open_window function to run after the specified delay
# window.after(delay_ms)

# Run the tkinter main loop
window.mainloop()
