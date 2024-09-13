def change_case(func):
    def inner(name):
        print("HI "+ name.upper())
    return inner

@change_case
def display(name):
    print(name)
display("mahi")
print("*****")
display("yasin")