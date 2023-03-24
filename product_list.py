products = []


while True:
    name = input('enter products name:')
    if name == "q":
        break
    price = input('enter price of products:')
    p = [name, price]
    products.append(p)
print(products)

for d in products:
    print(d[0], d[1])

with open('products.csv', 'w', encoding = 'utf8') as f:
    f.write('products,price' + '\n')
    for d in products:
        f.write(d[0] + ',' + d[1] + '\n')
     
