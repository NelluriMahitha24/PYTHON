product_Prices=[1000,50,20,30,500,600,2000]
map_obj=filter(lambda price:price<1000,product_Prices)
new_prices=list(map_obj)
print(new_prices)