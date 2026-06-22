import inventory
try:
    db=inventory.dbcode()
    while True:
        print("---------inventory system----------")
        c=int(input("1.ADD\n2.UPDATE\n3.VIEW\n4.DELETE\n5.EXIT\n---Enter the option:"))
        if c==1:
            n=input("Enter the Product Name :")
            ca=input("Enter the Category :")
            pr=int(input("Enter the Product Price$:"))
            q=float(input("Enter the Product Quantity:"))
            db.insertdata(n,ca,pr,q)
        elif c==2:
            p=int(input("New price:"))
            i=int(input("product ID :"))
            db.updatedata(p,i)
        elif c==3:
            print("product details")
            db.viewdata()
        elif c==4:
            i=int(input("enter the product id :"))
            db.deletedata(i)
        
        elif c==5:
            print("app closed")
            break
        else :
            print("invalid choice")
except Exception as e:
    print(e)


