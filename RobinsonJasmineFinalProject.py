
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#Creates the main window.
root = tk.Tk()
root.title("Coffee Xpress")
root.geometry("800x900") 

#Load images and resize them for display.
try:
    logoImage = Image.open("logo.jpg")
    logoImage = logoImage.resize((200, 100)) 
    logoImage = ImageTk.PhotoImage(logoImage)

    backgroundImage = Image.open("order background.png")
    backgroundImage = backgroundImage.resize((800, 850))  
    backgroundImage = ImageTk.PhotoImage(backgroundImage)

    bannerImage = Image.open("order banner.jpg")
    bannerImage = bannerImage.resize((800, 200))  
    bannerImage = ImageTk.PhotoImage(bannerImage)
except Exception as e:
    print(f"Error loading images: {e}")

#Defines the menu items and their prices.
menuItems = {
    "Brewed Coffee": 2.95,
    "Americano": 4.55,
    "Latte": 4.95,
    "Flat White": 5.45,
    "Cold Brew": 4.65,
    "Matcha": 5.65,
    "Hot Chocolate": 4.45,
}

#Defines all syrup options and their upcharges.
syrupOptions = {
    "No Syrup": 0.0,  
    "Brown Sugar": 0.5,
    "Caramel": 0.5,
    "Hazelnut": 0.5,
    "Vanilla": 0.5,
    "Cinnamon Dolce": 0.5,
}

#Defines all milk options and their upcharges.
milkOptions = {
    "2% Milk": 0.0,  
    "Almond": 0.25,
    "Coconut": 0.25,
    "Oatmilk": 0.25,
    "Heavy Cream": 0.25,
    "Whole Milk": 0.5,
}

#Defines temperature options.
tempOptions = ["Hot", "Iced"]

#Initializing dropdown values to placeholders.
selectedItem = tk.StringVar(value="Select a Drink")
selectedSyrup = tk.StringVar(value="Select Syrup")
selectedMilk = tk.StringVar(value="Select Milk")
selectedTemp = tk.StringVar(value="Select Temperature")

#Creates the dropdown for the drink items.
def createDrinkDropdown():
    drinkLabel = tk.Label(root, text="Choose Your Drink:")
    drinkLabel.grid(row=2, column=0, padx=20, pady=20, sticky="W")

    drinkMenu = tk.OptionMenu(root, selectedItem, *menuItems.keys())
    drinkMenu.grid(row=3, column=0, padx=20, pady=5, sticky="W")

#Creates the dropdown for the syrup options.
def createSyrupDropdown():
    syrupLabel = tk.Label(root, text="Choose Your Syrup:")
    syrupLabel.grid(row=2, column=1, padx=20, pady=20, sticky="W")

    syrupMenu = tk.OptionMenu(root, selectedSyrup, *syrupOptions.keys())
    syrupMenu.grid(row=3, column=1, padx=20, pady=5, sticky="W")

#Creates the dropdown for the milk options.
def createMilkDropdown():
    milkLabel = tk.Label(root, text="Choose Your Milk:")
    milkLabel.grid(row=2, column=2, padx=20, pady=20, sticky="W")

    milkMenu = tk.OptionMenu(root, selectedMilk, *milkOptions.keys())
    milkMenu.grid(row=3, column=2, padx=20, pady=5, sticky="W")

#Creates the dropdown for the temperature options.
def createTempDropdown():
    tempLabel = tk.Label(root, text="Choose Your Temperature:")
    tempLabel.grid(row=4, column=0, padx=20, pady=20, sticky="W")

    tempMenu = tk.OptionMenu(root, selectedTemp, *tempOptions)
    tempMenu.grid(row=5, column=0, columnspan=3, padx=20, pady=5, sticky="W")

#Calculates the total price.
def calculateTotal():
    totalPrice = 0
    orderSummary = []

    #Checks if a drink is selected.
    selectedDrink = selectedItem.get()
    if selectedDrink == "Select a Drink":
        messagebox.showwarning("No Selection", "Please Select a Drink.")
        return

    totalPrice += menuItems[selectedDrink]
    orderSummary.append(f"{selectedDrink} - ${menuItems[selectedDrink]}")

    #Checks if a syrup is selected.
    selectedSyrupOption = selectedSyrup.get()
    if selectedSyrupOption == "Select Syrup":
        messagebox.showwarning("No Selection", "Please Select a Syrup.")
        return

    if selectedSyrupOption != "No Syrup":
        totalPrice += syrupOptions[selectedSyrupOption]
        orderSummary.append(f"{selectedSyrupOption} - ${syrupOptions[selectedSyrupOption]}")

    #Checks if a milk is selected.
    selectedMilkOption = selectedMilk.get()
    if selectedMilkOption == "Select Milk":
        messagebox.showwarning("No Selection", "Please Select a Milk.")
        return

    totalPrice += milkOptions[selectedMilkOption]
    orderSummary.append(f"{selectedMilkOption} - ${milkOptions[selectedMilkOption]}")

    #Checks if the temperature is selected.
    selectedTemperature = selectedTemp.get()
    if selectedTemperature == "Select Temperature":
        messagebox.showwarning("No Selection", "Please Select a Temperature.")
        return

    orderSummary.append(f"Temperature: {selectedTemperature}")
    orderSummary.append(f"Total: ${totalPrice}")
    messagebox.showinfo("Order Summary", "\n".join(orderSummary))

#Clears all the selections made.
def clearSelection():
    selectedItem.set("Select a Drink")
    selectedSyrup.set("Select Syrup")
    selectedMilk.set("Select Milk")
    selectedTemp.set("Select Temperature")

#Adds "Place Order" button.
def createButtons():
    orderButton = tk.Button(root, text="Place Order", command=calculateTotal)
    orderButton.grid(row=6, column=0, columnspan=2, padx=20, pady=80)

    #Adds "Clear Selection" button.
    clearButton = tk.Button(root, text="Clear Selection", command=clearSelection)
    clearButton.grid(row=6, column=2, padx=20, pady=80)

    #Adds "Exit" button.
    exitButton = tk.Button(root, text="Exit", command=exitApp)
    exitButton.grid(row=6, column=0, columnspan=3, padx=20, pady=10)

#Function to exit the application.
def exitApp():
    root.quit()

#Adds banner image.
def banner():
    if bannerImage:
        bannerLabel = tk.Label(root, image=bannerImage)
        bannerLabel.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

#Adds logo image.
def logo():
    if logoImage:
        logoLabel = tk.Label(root, image=logoImage)
        logoLabel.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

#Adds background image and configures grid.
def background():
    if backgroundImage:
        backgroundLabel = tk.Label(root, image=backgroundImage)
        backgroundLabel.grid(row=0, column=0, rowspan=100, columnspan=100, sticky="nsew")

#Configure the grid to have the layout.
root.grid_rowconfigure(0, weight=1)  
root.grid_rowconfigure(1, weight=1) 
root.grid_rowconfigure(2, weight=1)  
root.grid_rowconfigure(3, weight=1)  
root.grid_rowconfigure(4, weight=1)  
root.grid_rowconfigure(5, weight=1)  
root.grid_rowconfigure(6, weight=1)   
root.grid_columnconfigure(0, weight=1)  
root.grid_columnconfigure(1, weight=1)  
root.grid_columnconfigure(2, weight=1)  

#Calls functions.
background()
banner()
logo()
createDrinkDropdown()
createSyrupDropdown()
createMilkDropdown()
createTempDropdown()
createButtons()

#Runs the GUI
root.mainloop()