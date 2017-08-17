def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print (answer)

my_data = [17,10,0]

health_calculator(my_data[0], my_data[1], my_data[2])
health_calculator(*my_data)
