#write functions here, don't add input('') statements here!
def test_config():
    return True
def get_person_category(age):
    if 1 >= age and age != 0:
        print("infant")
    elif age > 1 and age < 13:
        print("child")
    elif age >= 13 and age < 20:
        print("teenager")
    elif age >= 20 and age < 125:
        print("adult")
    elif age >= 125:
        print("Invalid Number")
    elif age == 0:
        print("Invalid Number")