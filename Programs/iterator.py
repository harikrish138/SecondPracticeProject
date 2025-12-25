lst = 1,2,4,6,0,7

it=iter(lst)
print(next(it))
print(next(it))
print(next(it))
print(next(it))



# Exaample 2

class Count:
    def __init__(self,limit):
        self.limit=limit
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.limit:
            self.current+=1
            return self.current
        else:
            raise StopIteration
itr=Count(4)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

