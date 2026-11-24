products = [
    {"id": 1, "name": "Laptop", "price": 50000, "quantity": 5},
    {"id": 2, "name": "Mouse", "price": 500, "quantity": 20},
    {"id": 3, "name": "Keyboard", "price": 1500, "quantity": 10},
    {"id": 4, "name": "Monitor", "price": 12000, "quantity": 3},
    {"id": 5, "name": "Headphones", "price": 2500, "quantity": 0}
]

menuList = [
    "1. Display all products.",
    "2. Search products by ID.",
    "3. Add a new product.",
    "4. Update product price.",
    "5. Update product quantity.",
    "6. Delete a product.",
    "7. Calculate total inventory value.",
    "8. Display out-of-stock products.",
    "9. Find the most expensive product.",
    "0. Exit.",
]



def displayInventoryDetails():
    print(f"{'ID':<5} {'NAME':<15} {'PRICE':>10} {'QUANTITY':>10}")
    for product in products:
        print(
            f"{product['id']:<5} "
            f"{product['name']:<15} "
            f"{product['price']:>10,} "
            f"{product['quantity']:>10}"
        )
        
def searchProductDetails():

    pId = int(input("Enter the product ID:  "))
              
    for product in products:
        if(product["id"]==pId):
            print("\n\n====PRODUCT DETAILS=====\n")
            print(f"Product ID : {product['id']}")
            print(f"Product Name : {product['name']}")
            print(f"Product Price : {product['price']}")
            print(f"Product Quantity : {product['quantity']}")
            break
        else:
            print("Product not found")
            
            
def addNewProd():
    global products
    
    print("\n\n====ADD NEW PRODUCT====\n\n")
    pid=int(input("Enter the Product ID:  "))
    pName = str(input("Enter the Product Name:  ")) 
    pPrice = (input("Enter the Product Price:  "))
    pQuantity = (input("Enter the Product Quantity:  "))
    
    newProduct = {
    "id":pid,
    "name":pName,
    "price":pPrice,
    "quantity":pQuantity
    }
    products.append(newProduct)
    print("\n\nProduct added successfully\n\n")


def updatePrice():
    global products
    
    pid = int(input("Enter the Product ID: "))
    
    for prod in products:
        if (prod['id']==pid):
            newPrice = float(input("Enter the new price: "))
            prod['price'] = newPrice
            print("\n\nPrice updated successfully\n\n")
            break
        else:
            print("\n\nProduct not found\n\n")
    
    
def updateQuantity():
    global products
    
    pid = int(input("Enter the Product ID: "))
    
    for prod in products:
        if (prod['id']==pid):
            newQuantity = int(input("Enter the new quantity: "))
            prod['quantity'] = newQuantity
            print("\n\nQuantity updated successfully\n\n")
            break
        else:
            print("\n\nProduct not found\n\n")
            


def deleteProduct():
    global products
    
    pid = int(input("Enter the Product ID: "))
    
    deletedProduct=0
    
    for prod in products:
        if (prod['id']==pid):
            products.remove(prod)
            print("\n\nProduct deleted successfully\n\n")
            deletedProduct += 1
            break
    if(deletedProduct==0):
        print("\n\nProduct not found\n\n") 

def totalInventoryValue():
    global products
    
    totalValue = 0
    for prod in products:
        totalValue += prod['price'] * prod['quantity']
    print("\n\nTotal inventory value: ", totalValue, "\n\n")
    

def outOfStockProducts():
    
    for prod in products:
        if (prod['quantity']==0):
            print("\n\nProduct not found\n\n")
            break
        

def mostExpensiveProduct():
    
    pName=""
    pPrice=0
    
    for prod in products:
        if (prod['price']>pPrice):
            pPrice=prod['price']
            pName=prod['name']
    
    print("\n\nThe most expensive product is: ", pName, "\n\n")


def dispMenu():
    while True:
        print("\n" + "=" * 25)
        for menu in menuList:
            print(menu)
        print("=" * 25)
        
        searchId = int(input("Choose the menu: "))
        
        if searchId == 0:
            print("\nExiting program. Goodbye!\n")
            break
        elif searchId == 1:
            displayInventoryDetails()
        elif searchId == 2:
            searchProductDetails()
        elif searchId == 3:
            addNewProd()
        elif searchId == 4:
            updatePrice()
        elif searchId == 5:
            updateQuantity()
        elif searchId == 6:
            deleteProduct()
        elif searchId == 7:
            totalInventoryValue()
        elif searchId == 8:
            outOfStockProducts()
        elif searchId == 9:
            mostExpensiveProduct()
        else:
            print("\nInvalid choice. Please try again.")
    



#Main menu
dispMenu()









