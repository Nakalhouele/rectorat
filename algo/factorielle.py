
def factorielle(n: int):
    if (n > 0):
        return factorielle(n - 1) * n
    return 1
    
# main
for x in range(0, 10):
    print(f'factorielle({x})={factorielle(x)}')

# output
# factorielle(0)=1
# factorielle(1)=1
# factorielle(2)=2
# factorielle(3)=6
# factorielle(4)=24
# factorielle(5)=120
# factorielle(6)=720
# factorielle(7)=5040
# factorielle(8)=40320
# factorielle(9)=362880