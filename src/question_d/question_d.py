#write functions here, don't add input('') statements here!
def get_bonus_pay_amount(sales):
    bonus_pay = 0
    if sales > 0 and sales < 499:
        bonus_pay = (sales * 0.05)
    elif sales >= 500 and sales < 999:
        bonus_pay = (sales * 0.06)
    elif sales >= 1000 and sales < 1499:
        bonus_pay = (sales * 0.07)
    elif sales >= 1500 and sales < 1999:
        bonus_pay = (sales * 0.08)
    elif sales >= 2000:
        bonus_pay = "Invalid number"
    return bonus_pay
