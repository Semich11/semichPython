class LoanContract:
    def __init__(self, name="Chris", interest_rate=6.00, loan_amount=100000, loan_period=1):
        self.name = name
        self.interest_rate = interest_rate
        self.loan_amount = loan_amount
        self.loan_period = loan_period
    #end

    def monthly_interest(self):
        interest_to_decimal = self.interest_rate / 100
        return interest_to_decimal / (self.loan_period * 12)
    #end

    def commute_monthly_payment(self):
        numerator = self.loan_amount * self.monthly_interest()
        denominator = 1 - (1 / (1 + self.monthly_interest()) ** (self.loan_period * 12))
        return numerator / denominator
    #end
    def compute_total_payment(self):
        return self.commute_monthly_payment() * (self.loan_period * 12)


loan = LoanContract()
print("MONTHLY: ",loan.commute_monthly_payment())
print(loan.monthly_interest())