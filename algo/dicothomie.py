
   
def dicothomie(value: int, tab_of_n_items, n_items:int, min_n_value: int) -> bool:
    if (n_items < min_n_value):
        print(f'n_items < min_n_value => {n_items} < {min_n_value}')
        return False
    
    
    return False    


def factorielle(n: int):
    if (n > 0):
        return factorielle(n - 1) * n
    return 1
    
# main
n_items=10
min_n_value=1
tab_of_n_items = [(i + min_n_value) for i in range(n_items)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value=5
# print(tab_of_n_items)
# res= dicothomie(5, tab_of_n_items, n_items, min_n_value)
# print(res)
# res = factorielle(2)
# for x in range(0, 10):
#     print(f'factorielle({x})={factorielle(x)}')
for _ in range(2, 9):
	print(_)
