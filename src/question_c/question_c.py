#write functions here, don't add input('') statements here!
def reverse_string(string1):
    stack = list(string1)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str