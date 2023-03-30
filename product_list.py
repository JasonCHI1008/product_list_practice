import os
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf8' ) as f:
        for line in f:
            if 'products,price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products
# Let users enter
def user_input(products):    
    while True:
        name = input('enter products name:')
        if name == "q":
            break
        price = input('enter price of products:')
        p = [name, price]
        products.append(p)
    print(products)
    return products
# Print purchase history
def print_products(products):
    for d in products:
        print(d[0], d[1])
# write a file
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf8') as f:
        f.write('products,price' + '\n')
        for d in products:
            f.write(d[0] + ',' + d[1] + '\n')
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print("file exist!")
        products = read_file(filename)
    else:
        print('file does not exist')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()