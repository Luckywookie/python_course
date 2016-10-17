if len(frac1) > 1:
    fraction1 = frac1[1]
    unit1 = abs(int(frac1[0]))
else:
    fraction1 = frac1[0]
    unit1 = 0

if len(frac2) > 1:
    fraction2 = frac2[1]
    unit2 = abs(int(frac2[0]))
else:
    fraction2 = frac2[0]
    unit2 = 0

numerator1, denominator1 = str(fraction1).split('/')
numerator2, denominator2 = str(fraction2).split('/')

sign1 = frac1[0][0]
sign2 = frac2[0][0]

# приводим целую и дробую часть к знаменателю, вычислив числитель для каждой дроби
sum_num1 = int(unit1) * int(denominator1) + abs(int(numerator1))
sum_num2 = int(unit2) * int(denominator2) + abs(int(numerator2))



# print frac1, frac2, unit1, unit2, sum_num1, sum_num2, sign1, sign2, ch1, ch2, ch, number, dr