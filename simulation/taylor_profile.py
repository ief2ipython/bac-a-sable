import pdb
import tracemalloc

pdb.set_trace()

#tracemalloc.start()

def factorial(n):
    if n == 0: 
        return 1.0 
    else: 
        return float(n) * factorial(n-1) 

def taylor_exp(n): 
    return [1.0/factorial(i) for i in range(n)] 


def taylor_sin(n): 
    res = []

    for i in range(n): 
        if i % 2 == 1: 
           res.append((-1)**((i-1)/2)/float(factorial(i))) 
        else: 
           res.append(0.0) 
    return res 

def benchmark():
    #snaphot1 = tracemalloc.take_snapshot()
    taylor_exp(500)
    #snaphot2 = tracemalloc.take_snapshot()
    taylor_sin(500)
    #snaphot3 = tracemalloc.take_snapshot()

    #top_stats = snaphot2.compare_to(snaphot1,"lineno")
    #top_stat2 = snaphot3.compare_to(snaphot2,"lineno")

    #for stat in top_stats[:10]:
    #    print (stat)
    #for stat2 in top_stat2[:10]:
    #    print (stat2)


if __name__ == '__main__': 
    benchmark()

