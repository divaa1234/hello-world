def part1(annualInterestRate,monthlyPaymentRate,balance):
    month = 0
    totalPay = 0
    monthlyInterestRate = annualInterestRate / 12.0
    while month <12:
        minPay = monthlyPaymentRate * balance
        unpayBal = balance - minPay
        totalPay += minPay
        balance = unpayBal + (monthlyInterestRate * unpayBal)
        month += 1
        print('Month: ' + str(month))
        print('Minimum monthly payment: ' + str(round(minPay,2)))
        print('Remaining balance: ' + str(round(balance,2)))
    print('Total paid: ' + str(round(totalPay,2)))
    print(' Remaining balance: ' + str(round(balance,2)))


def part2(annualInterestRate,balance):
    initBalance = balance
    monthlyInterestRate = annualInterestRate / 12.0
    month = 0
    minPay = 10
    def calculate(month, balance, minPay, monthlyInterestRate):
        while month <12:
            unpaidBalance = balance - minPay
            balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
            month += 1
        return balance
    while calculate(month, balance, minPay, monthlyInterestRate) > 0:
        balance = initBalance
        minPay +=10
        month = 0
        calculate(month, balance, minPay, monthlyInterestRate)
    print('Lowest Payment: ' + str(minPay))
    
    
def part3(annualInterestRate,balance):
    initBalance = balance
    monthlyInterestRate = annualInterestRate/12.0
    low = balance/12.0
    high = (balance * ((1.0 + monthlyInterestRate)**12))/12.0
    epsilon = 0.01
    minPay = (high + low)/2.0
    month = 0
    def calculate(month, balance, minPay, monthlyInterestRate):
        while month <12:
            unpaidBalance = balance - minPay
            balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
            month += 1
        return balance   
    while abs(balance) >= epsilon:
        balance = initBalance
        month = 0
        balance = calculate(month, balance, minPay, monthlyInterestRate)
        if balance > 0:
            low = minPay
        else:
            high = minPay
        minPay = (high + low)/2.0
    minPay = round(minPay,2)
    print('Lowest Payment: ' + str(minPay))    
    