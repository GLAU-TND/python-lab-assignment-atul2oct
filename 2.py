#WAP to demonstrate exception handling for AttributeErroe, TypeError and ValueError
try:
    a=10
    b="ATUL"
    c = a + b
    b.rename()
    d=int(b)
except ValueError as e:
    print("ValueError",e)
except AttributeError as e:
    print("AttributeError",e)
except TypeError as e:
    print("TypeError",e)