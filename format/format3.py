# formatted string  literals , f or F
# Using the f or F
list1 = ['man', 'woman', 'child', 89, 1234, 'Hi']
guest = 'Charly'
price  = 940

visitors = {'name': ['Jone', 'Emmy', 'lorrie', 'kenn', 'jude'],
            'gift': ['shoes', 'bags', 'pens', 'clock', 'printer']}

print(f'The book was sold at ${price}')

for keys, values in visitors.items():
    print(f'{keys}: {values}')
    for i in values:
        print(f'{keys.upper()}: {i}')