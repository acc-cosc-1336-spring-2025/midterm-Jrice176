#add import
import question_d
def main():
    sales = input("Enter your sales number:")
    result = question_d.get_bonus_pay_amount(int(sales))
    print(result)
main()