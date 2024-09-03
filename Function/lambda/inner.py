def outer():
    print("outer")
    def inner():
        print("inner")
    return inner
inner=outer()
inner()