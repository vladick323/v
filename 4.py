#assert 2+2==5, "dumay krache"

#"""
#>>> 2+2
#6
#result
#"""

#if __name__=="__main__":
    #import doctest
    #doctest.testmod()
def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result