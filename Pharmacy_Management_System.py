import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class PharmacyManagementSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")

        # Initialize variables
        self.inventory = {}
        self.sales = []

        # Create and set up notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(padx=10, pady=10, expand=True, fill="both")

        # Create tabs
        self.inventory_tab = ttk.Frame(self.notebook)
        self.sales_tab = ttk.Frame(self.notebook)

        # Add tabs to notebook
        self.notebook.add(self.inventory_tab, text="Medication Management")
        self.notebook.add(self.sales_tab, text="Sales")

        # Apply background to notebook and tabs
        self.notebook.configure(style="Custom.TNotebook")
        self.style = ttk.Style()
        self.style.configure("Custom.TNotebook", background="#e0f7fa")  # خلفية التبويب الرئيسي
        self.style.configure("Custom.TNotebook.Tab", background="#b2ebf2")  # خلفية التبويب

        # Create a label to display in the "Medication Management" tab
        medication_label = tk.Label(self.inventory_tab, text="This is the Medication Management Page", bg="#2196F3")  # لون الخلفية هنا
        medication_label.pack(padx=10, pady=10)
      
        # Create treeviews for inventory and sales
        self.create_inventory_treeview()
        self.create_sales_treeview()

        

        # Create buttons for inventory
        self.add_item_button = tk.Button(self.inventory_tab, text="Add Item", command=self.add_item, bg="#E0FFFF", fg="black")
        self.edit_item_button = tk.Button(self.inventory_tab, text="Edit Item", command=self.edit_item, bg="#e0f7fa", fg="black")
        self.delete_item_button = tk.Button(self.inventory_tab, text="Delete Item", command=self.delete_item, bg="#e0f7fa", fg="black")
        self.clear_inventory_button = tk.Button(self.inventory_tab, text="Clear Inventory", command=self.clear_inventory, bg="#e0f7fa", fg="black")
        self.add_item_button.pack(pady=5)
        self.edit_item_button.pack(pady=5)
        self.delete_item_button.pack(pady=5)
        self.clear_inventory_button.pack(pady=5)

        # Create buttons for sales
        self.sell_item_button = tk.Button(self.sales_tab, text="Sell Item", command=self.sell_item, bg="#e0f7fa", fg="black")
        self.clear_person_sales_button = tk.Button(self.sales_tab, text="Clear Sales", command=self.clear_person_sales, bg="#e0f7fa", fg="black")
        self.sell_item_button.pack(pady=10)
        self.clear_person_sales_button.pack(pady=10)
        # # Create buttons for inventory
        # self.add_item_button = tk.Button(self.inventory_tab, text="Add Item", command=self.add_item)
        # self.edit_item_button = tk.Button(self.inventory_tab, text="Edit Item", command=self.edit_item)
        # self.delete_item_button = tk.Button(self.inventory_tab, text="Delete Item", command=self.delete_item)
        # self.clear_inventory_button = tk.Button(self.inventory_tab, text="Clear Inventory", command=self.clear_inventory)
        # self.add_item_button.pack(pady=5)
        # self.edit_item_button.pack(pady=5)
        # self.delete_item_button.pack(pady=5)
        # self.clear_inventory_button.pack(pady=5)

        # # Create buttons for sales
        # self.sell_item_button = tk.Button(self.sales_tab, text="Sell Item", command=self.sell_item)
        # self.sell_item_button.pack(pady=10)

        # Create labels and entry widgets for selling medicines
        tk.Label(self.sales_tab, text="Item ID:").pack(pady=5)
        self.sell_item_id_entry = tk.Entry(self.sales_tab)
        self.sell_item_id_entry.pack(pady=5)

        tk.Label(self.sales_tab, text="Quantity to Sell:").pack(pady=5)
        self.sell_quantity_entry = tk.Entry(self.sales_tab)
        self.sell_quantity_entry.pack(pady=5)

        # Button to clear sales for the current person
        self.clear_person_sales_button = tk.Button(self.sales_tab, text="Clear Sales", command=self.clear_person_sales)
        self.clear_person_sales_button.pack(pady=10)

        # Label to display total quantity and total price of medicines sold for the day
        self.total_sold_label = tk.Label(self.sales_tab, text="Total Sold: 0 items, Total Price: $0.00")
        self.total_sold_label.pack(pady=10)

        # Load initial inventory data
        self.load_inventory()

    def create_inventory_treeview(self):
        self.inventory_tree = ttk.Treeview(self.inventory_tab, columns=("ID", "Name", "Price", "Quantity"), show="headings")
        self.inventory_tree.heading("ID", text="ID")
        self.inventory_tree.heading("Name", text="Name")
        self.inventory_tree.heading("Price", text="Price")
        self.inventory_tree.heading("Quantity", text="Quantity")

        # Add vertical and horizontal scroll bars
        scroll_y = ttk.Scrollbar(self.inventory_tab, orient="vertical", command=self.inventory_tree.yview)
        scroll_x = ttk.Scrollbar(self.inventory_tab, orient="horizontal", command=self.inventory_tree.xview)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        self.inventory_tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.inventory_tree.pack(pady=10)

    def create_sales_treeview(self):
        self.sales_tree = ttk.Treeview(self.sales_tab, columns=("Timestamp", "Item", "Price", "Quantity"), show="headings")
        self.sales_tree.heading("Timestamp", text="Timestamp")
        self.sales_tree.heading("Item", text="Item")
        self.sales_tree.heading("Price", text="Price")
        self.sales_tree.heading("Quantity", text="Quantity")

        # Add vertical and horizontal scroll bars
        scroll_y = ttk.Scrollbar(self.sales_tab, orient="vertical", command=self.sales_tree.yview)
        scroll_x = ttk.Scrollbar(self.sales_tab, orient="horizontal", command=self.sales_tree.xview)

        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        self.sales_tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.sales_tree.pack(pady=10)

    def load_inventory(self):
        # Load initial inventory data (you can replace this with your own data loading logic)
        # For simplicity, using static data here
        self.inventory = {
            '1': {'name': 'Aspirin', 'price': 5.99, 'quantity': 100},
            '2': {'name': 'Cough Syrup', 'price': 8.99, 'quantity': 50},
            '3': {'name': 'Bandages', 'price': 3.99, 'quantity': 200},
        }

        # Display inventory in the treeview
        self.display_inventory()

    def apply_changes(self, item_id, new_name, new_price, new_quantity, edit_window):
      try:
          # Validate input
          if not new_name or not new_price or not new_quantity:
              messagebox.showinfo("Error", "Please fill in all the fields.")
              return

          # Update the inventory dictionary with the new values
          self.inventory[item_id]['name'] = new_name
          self.inventory[item_id]['price'] = float(new_price)
          self.inventory[item_id]['quantity'] = int(new_quantity)

          # Update the tree view
          self.display_inventory()

          # Close the edit window
          edit_window.destroy()

      except ValueError:
          messagebox.showinfo("Error", "Invalid input. Please enter valid numbers.")

    def edit_item(self):
      # Implement logic to edit item in inventory
      selected_item = self.inventory_tree.selection()
      if selected_item:
          # Get the item id
          item_id = self.inventory_tree.item(selected_item, 'values')[0]

          # Create a popup window for editing
          edit_window = tk.Toplevel(self.root)
          edit_window.title("Edit Item")

          # Labels and Entry widgets for editing
          tk.Label(edit_window, text="New Name:").grid(row=0, column=0)
          new_name_entry = tk.Entry(edit_window)
          new_name_entry.grid(row=0, column=1)

          tk.Label(edit_window, text="New Price:").grid(row=1, column=0)
          new_price_entry = tk.Entry(edit_window)
          new_price_entry.grid(row=1, column=1)

          tk.Label(edit_window, text="New Quantity:").grid(row=2, column=0)
          new_quantity_entry = tk.Entry(edit_window)
          new_quantity_entry.grid(row=2, column=1)

          # Button to apply changes
          apply_button = tk.Button(edit_window, text="Apply Changes", command=lambda: self.apply_changes(item_id,
                                                                                                   new_name_entry.get(),
                                                                                                   new_price_entry.get(),
                                                                                                   new_quantity_entry.get(),
                                                                                                   edit_window))
          apply_button.grid(row=3, column=0, columnspan=2)

      else:
          messagebox.showinfo("Error", "Please select an item to edit.")

    def delete_item(self):
      # Get selected item
      selected_item = self.inventory_tree.selection()

      # Check if an item is selected
      if selected_item:
          # Get the item id
          item_id = self.inventory_tree.item(selected_item, 'values')[0]

          # Delete the item from the inventory dictionary
          del self.inventory[item_id]

          # Update the tree view
          self.display_inventory()
      else :
        messagebox.showinfo("Error", "Please select an item to delete.")

    def display_inventory(self):
      # Clear previous items
      for item in self.inventory_tree.get_children():
          self.inventory_tree.delete(item)

      # Insert new items
      for item_id, item in self.inventory.items():
          self.inventory_tree.insert("", "end", values=(item_id, item['name'], item['price'], item['quantity']))

    def add_item(self):
        # Create a popup window for adding an item
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Item")

        # Labels and Entry widgets for adding an item
        tk.Label(add_window, text="ID:").grid(row=0, column=0)
        id_entry = tk.Entry(add_window)
        id_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Price:").grid(row=2, column=0)
        price_entry = tk.Entry(add_window)
        price_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Quantity:").grid(row=3, column=0)
        quantity_entry = tk.Entry(add_window)
        quantity_entry.grid(row=3, column=1)

        # Button to add the item
        add_button = tk.Button(add_window, text="Add Item", command=lambda: self.add_item_to_inventory(id_entry.get(),
                                                                                                       name_entry.get(),
                                                                                                       price_entry.get(),
                                                                                                       quantity_entry.get(),
                                                                                                       add_window))
        add_button.grid(row=4, column=0, columnspan=2)

    def add_item_to_inventory(self, item_id, name, price, quantity, add_window):
        try:
            # Validate input
            if not item_id or not name or not price or not quantity:
                messagebox.showinfo("Error", "Please fill in all the fields.")
                return

            # Add the item to inventory
            self.inventory[item_id] = {'name': name, 'price': float(price), 'quantity': int(quantity)}

            # Display updated inventory
            self.display_inventory()

            # Close the add window
            add_window.destroy()
        except ValueError:
            messagebox.showinfo("Error", "Invalid input. Please enter valid numbers.")

    def clear_inventory(self):
        # Implement logic to clear the entire inventory
        confirm = messagebox.askyesno("Confirm Clear", "Are you sure you want to clear the entire inventory?")
        if confirm:
            self.inventory = {}
            # Display updated inventory
            self.display_inventory()

    def sell_item(self):
        # Implement logic to sell item
        item_id = self.sell_item_id_entry.get()
        quantity_to_sell = self.sell_quantity_entry.get()

        if item_id and quantity_to_sell:
            try:
                # Validate item ID and quantity
                item_id = str(int(item_id))
                quantity_to_sell = int(quantity_to_sell)

                if item_id in self.inventory and quantity_to_sell <= self.inventory[item_id]['quantity']:
                    # Update inventory
                    self.inventory[item_id]['quantity'] -= quantity_to_sell

                    # Record the sale
                    sale = {
                        'timestamp': str(datetime.now()),
                        'item': self.inventory[item_id]['name'],
                        'price': self.inventory[item_id]['price'],
                        'quantity': quantity_to_sell
                    }
                    self.sales.append(sale)

                    # Display updated inventory and sales
                    self.display_inventory()
                    self.display_sales()
                    self.display_total_sold()

                else:
                    messagebox.showinfo("Error", "Invalid item ID or insufficient quantity in inventory.")

            except ValueError:
                messagebox.showinfo("Error", "Invalid input. Please enter valid numbers.")
        else:
            messagebox.showinfo("Error", "Please enter item ID and quantity to sell.")

    def display_sales(self):
        # Clear previous items
        for item in self.sales_tree.get_children():
            self.sales_tree.delete(item)

        # Insert new items
        for sale in self.sales:
            self.sales_tree.insert("", "end", values=(sale['timestamp'], sale['item'], sale['price'], sale['quantity']))

    def display_total_sold(self):
        # Calculate and display the total quantity and total price of medicines sold for the day
        total_quantity = sum(sale['quantity'] for sale in self.sales)
        total_price = sum(sale['price'] * sale['quantity'] for sale in self.sales)
        self.total_sold_label.config(text=f"Total Sold: {total_quantity} items, Total Price: ${total_price:.2f}")

    def clear_person_sales(self):
        # Clear all sales
        self.sales = []
        self.display_sales()
        self.display_total_sold()

if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyManagementSystemGUI(root)
    root.geometry("800x600")
    root.configure(bg="#E0FFFF")
    root.mainloop()
