import os
products = []
if os.path.isfile('products.csv'):
    print("File exist")
    with open('products.csv', 'r', encoding = 'utf8' ) as f:
        for line in f:
            if 'products,price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
            print(products)
else:
    print("File doesn't exist")

# Let users enter        
while True:
    name = input('enter products name:')
    if name == "q":
        break
    price = input('enter price of products:')
    p = [name, price]
    products.append(p)
print(products)
# Print purchase history
for d in products:
    print(d[0], d[1])
# write a file
with open('products.csv', 'w', encoding = 'utf8') as f:
    f.write('products,price' + '\n')
    for d in products:
        f.write(d[0] + ',' + d[1] + '\n')
     
