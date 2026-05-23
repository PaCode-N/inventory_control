import os

#Array stock ordered in the following order: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
stock = [
    ["A01", "Procesadores", 0, 20],
    ["A02", "Memorias RAM", 0, 40],
    ["A03", "Discos duros", 0, 50],
    ["A04", "Tarjetas graficas", 0, 10],
    ["A05", "Fuentes de poder", 0, 25]
]


# Function to calculate the items to buy
def missing_items(actual_stock, minimum_stock):
    if actual_stock < minimum_stock:   #Conditional to calculate the items to buy
        to_buy = minimum_stock - actual_stock   #Items to buy
    else: #Not needed to buy more items
        to_buy = 0
    return to_buy #return the result

print("\nBienvenido a su herramienta de control de inventario :) \n")

#Request information
items_to_buy = []
for row in stock:   #Loop to update stock values

    article_name = row[1] #Taking name from array to ask the user for the value
    current_stock = int(input(f"Por favor digite la cantidad actual de {article_name} disponibles: ")) #Asking for the stock value
    while current_stock < 0: #Loop to avoid negative numbers
        print("Por favor ingrese un numero valido (mayor o igual a 0)")
        current_stock = int(input(f"Por favor digite la cantidad actual de {article_name} disponibles: "))
    row[2] = current_stock #Assigning value
    items_to_buy.append([row[0], article_name, missing_items(row[2], row[3])]) #New list with the items to buy

#Print results
os.system('cls')
print("\nEs necesario comprar los siguientes artículos: \n")
for row in items_to_buy:    #Loop to print the items to buy
    print(f"- {row[0]} {row[1]}: {row[2]}")

















