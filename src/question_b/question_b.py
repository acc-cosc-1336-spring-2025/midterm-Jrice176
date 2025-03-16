#write functions here, don't add input('') statements here!

def get_sum_of_evens(num):
    sum = 0

    for number in range(0, num):
        if number % 2 == 0:
            print(number)
            sum = number + sum

    print("The sum of total even numbers are:", sum + num)
    