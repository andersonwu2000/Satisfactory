import glpk 
import json, math

with open(r'Satisfactory-Linear-Programming\satisfactory_data.json', 'r') as file:
    recipes = json.loads(file.read())

resource = {
    'Iron Ore':92100,
    'Caterium Ore':15000,
    'Copper Ore':36900,
    'Limestone':69300,
    'Coal':42300,
    'Raw Quartz':13500,
    'Sulfur':10800,
    'Uranium':2100,
    'Bauxite':12300,
    'SAM':10200,
    'Crude Oil':12600,
    'Nitrogen Gas':12000
}

# ↓↓↓↓↓ Input ↓↓↓↓↓
Lim_of_buildings = None
# Targets = {
#     'Power': 1
# }
Targets = 'Building'
Restrictions = {
    'Power': (500000, 500000),
    'Plutonium Waste': (0, 0), 
    'Uranium Waste': (0, 0),  
    'Ficsonium': (0, 0), 
    'Non-Fissile Uranium': (0, 0),
    'Plutonium Pellet': (0, 0),
    'Encased Plutonium Cell':  (0, 0),
    'Power Shard': (0, 0)
}
Overclock = True
# ↑↑↑↑↑ Input ↑↑↑↑↑


# Get all items
items = set()
for recipe in recipes:
    items |= recipe.keys()
items = list(items)

# Initialization
lp = glpk.LPX()
lp.obj.maximize = True
lp.rows.add(len(items)+1)
lp.cols.add(len(recipes))

# Objective Function
if Targets == 'Building':
    lp.obj[:] = [-1] * len(recipes)
else:
    maximize = [0] * len(recipes)
    for row_id, item in enumerate(Targets):
        for col_id, recipe in enumerate(recipes):
            if item in recipe:
                maximize[col_id] += recipe[item] * Targets[item]
    lp.obj[:] = maximize

# Constraints
matrix = []
for row_id, item in enumerate(items):
    row = [0] * len(recipes)
    for col_id, recipe in enumerate(recipes):
        if item in recipe:
            row[col_id] = recipe[item]
    matrix += row
    if item in resource:
        lp.rows[row_id].bounds = 0, resource[item]
    elif item in Restrictions:
        lp.rows[row_id].bounds = Restrictions[item]
    elif item != 'Power':
        lp.rows[row_id].bounds = 0, None

matrix += [1] * len(recipes)
if Lim_of_buildings:
    lp.rows[len(items)].bounds = 0, Lim_of_buildings * 2.5**Overclock
else:
    lp.rows[len(items)].bounds = 0, None

lp.matrix = matrix

for id, recipe in enumerate(recipes):
    item = next(iter(recipe))
    if item in resource and recipe[item]>0:
        lp.cols[id].bounds = 0, resource[item]/recipe[item]
    else:
        lp.cols[id].bounds = 0, None
    
lp.simplex()

# Statistics
items = set()
for recipe in recipes:
    items |= recipe.keys()
num_of_building = 0
total_power = 0
total_output = {key:0 for key in items}
total_resource = {}
for i, recipe in zip(lp.cols, recipes):
    num_of_building += math.ceil(i.primal / 2.5**Overclock)
    total_power += i.primal * recipe['Power']
    for item in recipe:
        if item != 'Power':
            total_output[item] += i.primal * recipe[item]
        if item in resource and recipe[item]>0:
            total_resource[item] = i.primal * recipe[item]
total_output = {key:value for key, value in total_output.items() if value>10**-5}

# Output
with open(r'Satisfactory-Linear-Programming\satisfactory_result.txt', 'w') as file:
    file.write(f'Targets: {Targets}\n\n')
    file.write(f'Number of buildings = {num_of_building}\n')
    file.write(f'Total power = {total_power}\n')
    file.write(f'Outputs:\n')
    for i in total_output:
        l = max([len(key) for key in total_output]) + 1
        file.write(f'    {i}' + ' ' * (l-len(i)))
        file.write(f'= {round(total_output[i], 3)}\n')
    file.write(f'Resources:\n')
    for i in total_resource:
        value = round(total_resource[i]/resource[i]*100, 2)
        file.write(f'    {i}' + ' ' * (13-len(i)))
        file.write('=' + ' ' * (6-len(str(value))) + f'{value}% ')
        file.write(f'= {round(total_resource[i], 3)}\n')
    file.write('\n')
    for i, recipe in zip(lp.cols, recipes):
        if i.primal > 0:
            file.write(f'{recipe}\n    number = {i.primal/2.5**Overclock}\n')
