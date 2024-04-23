import customtkinter as ct
import sqlite3

s = ct.CTk()

# Frame settings
width = 1310
height = 550
s.geometry(f"{width}x{height}+90+265")
s.overrideredirect(1)

# Main window frame
main_f = ct.CTkFrame(master=s, height=height - 150, width=width - 50, fg_color="black")
main_f.pack(side=ct.TOP, pady=20)
main_f.propagate(False)

# Function to fetch button click counts and costs from the database
def fetch_button_click_counts():
    conn = sqlite3.connect('button_clicks.db')
    c = conn.cursor()
    c.execute("SELECT button_text, COUNT(*), cost FROM button_clicks GROUP BY button_text")
    button_click_counts = c.fetchall()
    conn.close()
    return button_click_counts

# Function to calculate total cost
def calculate_total_cost(button_click_counts):
    total_cost = 0
    for button_text, click_count, cost in button_click_counts:
        total_cost += click_count * cost
    return total_cost

# Function to display cart page
def display_cart_page():
    # Clear the previous content
    for widget in main_f.winfo_children():
        widget.destroy()
    
    # Fetch button click counts and costs
    button_click_counts = fetch_button_click_counts()
    
    # Create table header
    ct.CTkLabel(main_f, text="Button", font=('Consolas', 12)).grid(row=0, column=0, padx=5, pady=5)
    ct.CTkLabel(main_f, text="Qnty", font=('Consolas', 12)).grid(row=0, column=1, padx=5, pady=5)
    ct.CTkLabel(main_f, text="Cost", font=('Consolas', 12)).grid(row=0, column=2, padx=5, pady=5)  # Cost column
    ct.CTkLabel(main_f, text="Total", font=('Consolas', 12)).grid(row=0, column=3, padx=5, pady=5)  # Total column
    
    total_sum = 0  # Initialize total sum
    
    # Display button click counts and costs
    for i, (button_text, click_count, cost) in enumerate(button_click_counts, start=1):
        # Calculate total cost (cost * quantity)
        total = click_count * cost
        total_sum += total  # Update total sum
        
        # Display data in table
        ct.CTkLabel(main_f, text=button_text, font=('Consolas', 12)).grid(row=i, column=0, padx=5, pady=5)
        ct.CTkLabel(main_f, text=str(click_count), font=('Consolas', 12)).grid(row=i, column=1, padx=5, pady=5)
        ct.CTkLabel(main_f, text=f"₹{cost}", font=('Consolas', 12)).grid(row=i, column=2, padx=5, pady=5)  # Display cost in the table
        ct.CTkLabel(main_f, text=f"₹{total}", font=('Consolas', 12)).grid(row=i, column=3, padx=5, pady=5)  # Display total in the table
    
    # Create a frame for total cost
    total_frame = ct.CTkFrame(master=s, height=50, width=width - 50, fg_color="black")
    total_frame.pack(side=ct.TOP, pady=20)
    total_frame.propagate(False)
    
    # Display total cost
    ct.CTkLabel(total_frame, text="Total Cost:", font=('Consolas', 12)).pack(side=ct.LEFT, padx=5, pady=5)
    ct.CTkLabel(total_frame, text=f"₹{total_sum}", font=('Consolas', 12)).pack(side=ct.LEFT, padx=5, pady=5)

# Display cart page
display_cart_page()

# Function to print the bill
def print_bill():
    # Fetch button click counts and costs
    button_click_counts = fetch_button_click_counts()
    
    # Create or open a text file for writing
    with open("bill.txt", "w") as file:
        # Write header
        file.write("Button\tQuantity\tCost\n")
        
        # Write button click counts and costs
        print("Button Click Counts:", button_click_counts)
        for button_text, click_count, cost in button_click_counts:
            file.write(f"{button_text}\t{click_count}\t₹{cost}\n")
    
    print("Bill has been saved to bill.txt")


# BACK button
btn_back = ct.CTkButton(
    master=s,
    text="BACK",
    font=('Consolas', 12, 'bold'),
    command=lambda: clear(),
    width=100,
    height=40,
    corner_radius=10,
    fg_color="grey",
)
btn_back.place(x=1080, y=450)

# Print Bill button
btn_print_bill = ct.CTkButton(
    master=s,
    text="Print a Bill",
    font=('Consolas', 12, 'bold'),
    command=print_bill,
    width=100,
    height=40,
    corner_radius=10,
    fg_color="grey",
)
btn_print_bill.place(x=950, y=450)

def clear():
    s.destroy()

s.mainloop()
