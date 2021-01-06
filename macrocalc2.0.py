# script to take information from client and calculate macros accordingly
print('Welcome to the Archetype Fitness Macronutrient Calculator')
print('')

weight = input('What is your clients body weight in kilos?: ')
sex = input('Are they a biological male or female?: ')
is_male = sex == 'male'
is_female = sex == 'female'
activity_mult = input('Please select an activity multiplier from 1.0 to 1.9: ')
goal = input('Is the clients goal fat loss (respond: loss) or muscle gain (respond: gain): ')

is_loss = goal == 'loss'

is_gain = goal == 'gain'


if is_male:
    macros = int(weight) * 24.2
    macros = float(macros) * float(activity_mult)

if is_female:
    macros = int(weight) * 22
    macros = float(macros) * float(activity_mult)

if is_loss:
    loss_variable = input('Please select the desired daily caloric deficit: ')
    macros = int(macros) - int(loss_variable)

if is_gain:
    gain_variable = input('Please select the desired daily caloric surplus: ')
    macros = int(macros) + int(gain_variable)
print('')
print('Goal based calorie targets: ')
print(f'-{round(macros)} calories/day')
print(f'-{round(macros) * 7} calories/week')

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
