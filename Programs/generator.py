lst=['hello','krishna','redddy']
def gen():
    for i in lst:
        yield i
ge=gen()
print(next(ge))
print(next(ge))
print(next(ge))
