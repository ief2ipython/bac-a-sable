import timeit

class Foo(object): __slots__ = 'foo',

class Bar(object): pass

slotted     = Foo()
not_slotted = Bar()

def get_set_delete_fn(obj):
    def get_set_delete():
        obj.foo = 'foo'
        obj.foo
        del obj.foo
    return get_set_delete

is_slotted     = (min(timeit.repeat(get_set_delete_fn(slotted))))
is_not_slotted = (min(timeit.repeat(get_set_delete_fn(not_slotted))))

print (is_slotted,is_not_slotted, is_not_slotted/is_slotted)