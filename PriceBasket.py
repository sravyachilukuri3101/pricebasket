import sys

def discount_scheme_apples(price, pricepurdiscount):
    return price * (pricepurdiscount / 100)

def discount_scheme_soup(soupqty, breadqty, breadprice):
    if soupqty % 2 == 0:
        return breadprice

pricelist = {'Soup': 0.65, 'Bread': 0.80, 'Milk': 1.30, 'Apples' : 1.00}
itemlist = list(pricelist.keys())

# total arguments
itemstopurchase = len(sys.argv)

# Calculate sub total
subtotal = 0
for i in range(1, itemstopurchase):
    if(itemlist.count(sys.argv[i]) == 1):
        subtotal += pricelist[sys.argv[i]]
    else:
        print('Item not available : ' + sys.argv[i])
print ('Subtotal : £%.2f' % subtotal)

# check for discounts if any applicable
total = subtotal
for i in range(1, itemstopurchase):
    if sys.argv[i] == 'Apples':        
        discount_amt = discount_scheme_apples(pricelist[sys.argv[i]], 10)        
        print ('Apples 10% off: ' + str(discount_amt))
        total = total - discount_amt  

    # if sys.argv[i] == 'Soup':
    #     for j in range(1, itemstopurchase):
    #         if sys.argv[j] == 'Bread':
    #             discount_amt = discount_scheme_soup(soupqty, breadqty, breadprice/2)
    #             print ('Bread on half price: ' + str(discount_amt))

print ('Total: £%.2f' % total)