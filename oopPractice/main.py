from PersonalFi import Personalfi

account1 = Personalfi("Sofi", "savings", 6000.00, .045, 1, 750)
account2 = Personalfi("Fidelity", "Roth IRA", 10000, .12, 2, 230)
account3 = Personalfi("Pnc", "Checking", 2000, .001, 5, 0)
account4 = Personalfi("Robinhood", "Brokerage", 600, .3, 3, 10)

account3.change_reocurring_contribution()
print(account3.monthlycontribution)