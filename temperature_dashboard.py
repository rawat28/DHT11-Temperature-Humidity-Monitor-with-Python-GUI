import serial
import tkinter as tk
from tkinter import Label
from tkinter import font
import time

# Define the serial port where the Arduino is connected
# Replace 'COM3' with the correct port (Windows) or '/dev/ttyUSB0' (Linux/Mac)
arduino_port = 'COM3'  # Adjust for your system
baud_rate = 9600       # Match baud rate with your Arduino code
ser = serial.Serial(arduino_port, baud_rate)

# Create the main window for the Tkinter GUI
root = tk.Tk()
root.title("DHT11 Temperature & Humidity Monitor")
root.geometry("350x250")
root.configure(bg='#f0f0f0')

# Define custom fonts for the labels
font_title = font.Font(family="Helvetica", size=18, weight="bold")
font_data = font.Font(family="Helvetica", size=14)

# Add a title label
title_label = Label(root, text="Sensor Readings", font=font_title, bg='#f0f0f0', fg='#333')
title_label.pack(pady=10)

# Create labels to display temperature and humidity
temp_label = Label(root, text="Temperature: -- °C", font=font_data, bg='#f0f0f0', fg='#000')
temp_label.pack(pady=10)

humidity_label = Label(root, text="Humidity: -- %", font=font_data, bg='#f0f0f0', fg='#000')
humidity_label.pack(pady=10)

# Add a status label for error messages
status_label = Label(root, text="", font=("Helvetica", 10), bg='#f0f0f0', fg='red')
status_label.pack(pady=10)

# Function to update the temperature and humidity values
def update_values():
    if ser.in_waiting > 0:
        try:
            # Read the serial input from Arduino
            line = ser.readline().decode('utf-8').strip()
            if "Temperature" in line:
                # Extract and display temperature data
                temp_value = line.split(": ")[1].replace(" °C", "")
                temp_label.config(text=f"Temperature: {temp_value} °C")
                temp_label.config(fg='green')  # Change color to green for valid reading

            elif "Humidity" in line:
                # Extract and display humidity data
                humidity_value = line.split(": ")[1].replace(" %", "")
                humidity_label.config(text=f"Humidity: {humidity_value} %")
                humidity_label.config(fg='blue')  # Change color to blue for valid reading

        except Exception as e:
            status_label.config(text=f"Error: {e}")
            print(f"Error: {e}")
    
    # Schedule the next update after 2 seconds
    root.after(2000, update_values)

# Start the value update loop
update_values()

# Run the Tkinter event loop
root.mainloop()
