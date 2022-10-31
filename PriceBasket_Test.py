import unittest

class PriceBasketTest(unittest.TestCase):
    def discount_scheme_apples(price, pricepurdiscount):
        return price * (pricepurdiscount / 100)

    def discount_scheme_soup(soupqty, breadqty, breadprice):
        if soupqty % 2 == 0:
            return breadprice

    def pricebasket(items):
        pricelist = {'Soup': 0.65, 'Bread': 0.80, 'Milk': 1.30, 'Apples' : 1.00}
        itemlist = list(pricelist.keys())

        # total arguments
        itemstopurchase = len(items)

        # Calculate sub total
        subtotal = 0
        for i in range(0, itemstopurchase):
            if(itemlist.count(items[i]) == 1):
                subtotal += pricelist[items[i]]
            else:
                print('Item not available : ' + items[i])
        print ('Subtotal : £%.2f' % subtotal)

        # check for discounts if any applicable
        total = subtotal
        for i in range(1, itemstopurchase):
            if items[i] == 'Apples':        
                discount_amt = PriceBasketTest.discount_scheme_apples(pricelist[items[i]], 10)        
                print ('Apples 10% off: ' + str(discount_amt))
                total = total - discount_amt  

            # if items[i] == 'Soup':
            #     for j in range(1, itemstopurchase):
            #         if sys.argv[j] == 'Bread':
            #             discount_amt = PriceBasketTest.discount_scheme_soup(soupqty, breadqty, breadprice/2)
            #             print ('Bread on half price: ' + str(discount_amt))

        print ('Total: £%.2f' % total)

def make_test_function(description, itemlist):
    def test(self):
        PriceBasketTest.pricebasket(itemlist)
    return test

if __name__ == '__main__':
    testcases = {'case1': ['Apples',  'Milk',  'Bread'],
                'case2' : ['Apples', 'Milk'],
                'case3' : ['Bread']}

    for case in testcases:
        test_func = make_test_function(case, testcases[case])
        setattr(PriceBasketTest, 'test_{0}'.format(case), test_func)

    unittest.main()