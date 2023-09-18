
with open("life-expectancy.csv") as LE_dataset:
    year_of_interest = input("Enter the year of interest: ")

    final_year_max = " "
    final_entity_max = " "
    final_life_exp_max = 0
    final_entity_max_user = " "
    final_life_exp_max_user = 0
    final_year_min = " "
    final_entity_min = " "
    final_life_exp_min = 100
    final_entity_min_user = " "
    final_life_exp_min_user = 100
    lista_ave = []
    for linea in LE_dataset:
        no_blanks = linea.strip()
        parts = no_blanks.split(",")
        entity = parts[0]
        year = parts[2]
        life_exp = float(parts[3])  
        if life_exp < final_life_exp_min:
            final_life_exp_min = life_exp
            final_entity_min = entity
            final_year_min = year 
        if life_exp > final_life_exp_max:
            final_life_exp_max = life_exp
            final_entity_max = entity
            final_year_max = year 
        if year == year_of_interest:
            lista_ave.append(life_exp)            
            if life_exp < final_life_exp_max:
                 final_life_exp_max_user = life_exp
                 final_entity_max_user = entity
            else:
            # if life_exp < final_life_exp_min:
                 final_life_exp_min_user = life_exp
                 final_entity_min_user = entity
    ave = sum(lista_ave) / len(lista_ave)
    print()
    print(f"The overall max life expectancy is: {final_life_exp_max} from {final_entity_max} in {final_year_max}")
    print(f"The overall min life expectancy is: {final_life_exp_min} from {final_entity_min} in {final_year_min}")
    print()
    print(f"For the year {year_of_interest}:")
    print()
    print(f"The average life expectancy across all countries was {ave:.2f}")
    print(f"The max life expectancy was in {final_entity_max_user} with {final_life_exp_max_user}")
    print(f"The min life expectancy was in {final_entity_min_user} with {final_life_exp_min_user}")


#Entity,Code,Year,Life expectancy (years)




    