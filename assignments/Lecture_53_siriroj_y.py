def VatCalculate(price):
    result = price+(price*7/100)
    return result

print(VatCalculate(float(input("your price : "))))