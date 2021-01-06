# script to take information from client and calculate macros accordingly
print('Welcome to the Archetype Fitness Macronutrient Calculator')
print('')

weight = input('What is your clients body weight in kilos?: ')
sex = input('Are they a biological male or female?: ')
is_male = sex == 'male'
is_female = sex == 'female'

print('BMR without activity: ')
if is_male:
    bmr_male = int(weight) * 24.2
    print(f'-{round(bmr_male)} calories/day')
    print(f'-{round(bmr_male) * 7} calories/week')
if is_female:
    bmr_female = int(weight) * 22
    print(f'Approximately {round(bmr_female)} calories/day')
    print(f'Approximately {round(bmr_female) * 7} calories/week')
print('')

goal = input('Is the clients goal fat loss (respond: loss) or muscle gain (respond: gain): ')
is_loss = goal == 'loss'
is_gain = goal == 'gain'

activity_mult = input('Please select an activity multiplier from 1.0 to 1.9: ')

if is_male:
    macros = int(weight) * 24.2
    macros = float(macros) * float(activity_mult)

    if is_loss:
        loss_variable = input('Please select the desired daily caloric deficit: ')
        macros = int(macros) - int(loss_variable)

    if is_gain:
        gain_variable = input('Please select the desired daily caloric surplus: ')
        macros = int(macros) + int(gain_variable)

    print(f'Daily caloric target is: {round(macros)}kcals')
    print(f'Weekly caloric target is: {round(macros * 7)}kcals')
    print('')
    protein_percentage = input('Desired percentage daily protein using 0 to 0.5: ')
    grams_pro = (float(protein_percentage) * float(macros) / 4)
    fat_percentage = input('Desired percentage daily fat using 0 to 0.5: ')
    grams_fat = (float(fat_percentage) * float(macros) / 9)
    carb_percentage = input('Desired percentage daily carbohydrate using 0 to 0.5: ')
    grams_cho = (float(carb_percentage) * float(macros) / 4)

    print('')
    print('Your daily macros are as follows: ')
    print(f'Daily protein target: {round(grams_pro)}g / {round(grams_pro * 4)} calories')
    print(f'Daily dietary fat target: {round(grams_fat)}g / {round(grams_fat * 9)} calories')
    print(f'Daily carbohydrate target: {round(grams_cho)}g / {round(grams_cho * 4)} calories')

if is_female:
    macros = int(weight) * 22
    macros = float(macros) * float(activity_mult)

    if is_loss:
        loss_variable = input('Please select the desired daily caloric deficit: ')
        macros = float(macros) - float(loss_variable)

    if is_gain:
        gain_variable = input('Please select the desired daily caloric surplus: ')
        macros = float(macros) + float(gain_variable)

    print(f'Daily caloric target is: {round(macros)}kcals')
    print(f'Weekly caloric target is: {round(macros * 7)}kcals')
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
    print(f'Daily protein target: {round(grams_pro)}g / {round(grams_pro * 4)} calories')
    print(f'Daily dietary fat target: {round(grams_fat)}g / {round(grams_fat * 9)} calories')
    print(f'Daily carbohydrate target: {round(grams_cho)}g / {round(grams_cho * 4)} calories')
