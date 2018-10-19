def my_docre(func):
    def doc():
        print("decoreting...")
        func()
        print("finished...")
    return doc
@my_docre
def example():
    print("hello")

example()

