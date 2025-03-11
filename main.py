import tkinter as tk
from datetime import datetime

# function for calculate age
def calculate_age():
    name = name_entry.get()
    birth_date_str = dob_entry.get()
    
    try:
        # Convert input string to datetime object
        birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
        today = datetime.today()
        
        # Check if the birth date is in the future
        if birth_date > today :
            result_label.config(text="Please enter a correct date!", fg="red")
            return  # Stop execution if date is invalid
        
        # Calculate age
        age = today.year - birth_date.year - ((today.month , today.day) < (birth_date.month , birth_date.day))
        result_label.config(text=f"Hello {name}, You are {age} years old.", fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid date (dd-mm-yyyy)!" , fg="red")
    
# Create GUI Window
root= tk.Tk()
root.title("Age Calculator")
root.geometry("400x300")

# UI Components
tk.Label(root, text="Enter your name : ", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Label(root, text="Enter your Birth date (dd-mm-yyyy) : ", font=("Arial", 12)).pack(pady=5)
dob_entry = tk.Entry(root, font=("Arial", 12))
dob_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Age", font=("Arial", 12), bg="blue", fg="white",command= calculate_age)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()