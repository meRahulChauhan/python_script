class test:
    @classmethod
    def f(cls):
        print(id(cls))
print(id(test))
test.f()
