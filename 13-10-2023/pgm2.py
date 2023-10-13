sales1={'india':100,'china':500,'usa':700}
sales2={'uk':900,'japan':700}
sales=sales1.copy()
sales2.update({'uk':20})
sales.update(sales2)
print(sales)
