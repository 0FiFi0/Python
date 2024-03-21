# Tutaj pisz swój kod, młody padawanie ;-)
expenses = {
    'styczeń': 2700,
    'luty': 2900,
    'marzec': 3000,
    'kwiecień': 2900,
    'maj': 3000
}

min_expenses = min(expenses.values())
max_expenses = max(expenses.values())
sum_expenses = sum(expenses.values())
avg_expenses = sum_expenses / len(expenses)

last_month = list(expenses.keys())[-1]
amount_last_month = expenses[last_month]

if amount_last_month > avg_expenses:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")

print("Minimalna wartość: ", min_expenses)
print("Maksymalna wartość: ", max_expenses)
print("Suma wydatków: ", sum_expenses)
print("Średnia wartość: ", avg_expenses)
