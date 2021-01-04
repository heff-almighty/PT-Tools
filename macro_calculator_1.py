# script to take information from client and calculate macros accordingly
print('Welcome to the Archetype Fitness Macronutrient Calculator')
print('')

weight = input('What is your clients body weight in kilos?: ')
sex = input('Are they a biological male or female?: ')
is_male = sex == 'male'
is_female = sex == 'female'
# insert code to assign M or F and calculate BMR macros accordingly
# male = BW/kg x 24.2 // female = BW/kg x22
goal = input('Is their goal fat loss (respond: loss) or muscle gain (respond: gain): ')
is_loss = goal == 'loss'
is_gain = goal == 'gain'

if is_male:
    macros = int(weight) * 24.2
    if is_loss:
        loss_variable = input('Please select the desired daily caloric deficit ranging from 100 to 500 cals: ')
        macros = int(macros) - int(loss_variable)

    if is_gain:
        gain_variable = input('Please select the desired daily caloric surplus ranging from 100 to 500 cals: ')
        macros = int(macros) + int(gain_variable)

    print(f'Your daily baseline calories are: {round(macros)}kcals')
    print(f'Your weekly baseline calories are: {round(macros * 7)}kcals')
    print('')
    protein_percentage = input('Desired percentage daily protein using 0 to 0.5: ')
    grams_pro = (float(protein_percentage) * float(macros) / 4)
    fat_percentage = input('Desired percentage daily fat using 0 to 0.5: ')
    grams_fat = (float(fat_percentage) * float(macros) / 9)
    carb_percentage = input('Desired percentage daily carbohydrate using 0 to 0.5: ')
    grams_cho = (float(carb_percentage) * float(macros) / 4)

    print('')
    print('Your daily macros are as follows: ')
    print(f'Daily protein target: {round(grams_pro)}')
    print(f'Daily healhy dietary fat target: {round(grams_fat)}')
    print(f'Daily carbohydrate target: {round(grams_cho)}')

if is_female:
    macros = int(weight) * 22
    if is_loss:
        loss_variable = input('Please select the desired daily caloric deficit ranging from 100 to 500 cals: ')
        macros = int(macros) - int(loss_variable)

    if is_gain:
        gain_variable = input('Please select the desired daily caloric surplus ranging from 100 to 500 cals: ')
        macros = int(macros) + int(gain_variable)

    print(f'Your daily baseline calories are: {round(macros)}kcals')
    print(f'Your weekly baseline calories are: {round(macros * 7)}kcals')
    print('')
    protein_percentage = input('Desired percentage daily protein using 0 to 0.5: ')
    grams_pro = (float(protein_percentage) * float(macros) / 4)
    fat_percentage = input('Desired percentage daily fat using 0 to 0.5: ')
    grams_fat = (float(fat_percentage) * float(macros) / 9)
    carb_percentage = input('Desired percentage daily carbohydrate using 0 to 0.5: ')
    grams_cho = (float(carb_percentage) * float(macros) / 4)

    print('')
    print(f'Your daily baseline calories are: {round(macros)}kcals')
    print(f'Your weekly baseline calories are: {round(macros * 7)}kcals')
    print('')
    print('Your daily macros are as follows: ')
    print(f'Daily protein target: {round(grams_pro)}')
    print(f'Daily healhy dietary fat target: {round(grams_fat)}')
    print(f'Daily carbohydrate target: {round(grams_cho)}')
