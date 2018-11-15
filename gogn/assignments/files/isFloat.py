def is_float(s):
    ''' Returns True if the given string is a float, otherwise False '''
    try:
        float(s)
        return True
    except ValueError:
        return False

# is_float function definition goes here

print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))