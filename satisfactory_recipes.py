building = {
    'Smelter':       {'power':-4, 'somersloop':1},
    'Foundry':       {'power':-16, 'somersloop':2},
    'Constructor':   {'power':-4, 'somersloop':1},
    'Assembler':     {'power':-15, 'somersloop':2},
    'Manufacturer':  {'power':-55, 'somersloop':4},
    'Refinery':      {'power':-30, 'somersloop':2},
    'Blender':       {'power':-75, 'somersloop':4},
    'Packager':      {'power':-10, 'somersloop':0},
    'Miner Mk.3':    {'power':-45, 'somersloop':0},
    'Oil Extractor': {'power':-40, 'somersloop':0},
    'Particle Accelerator':      {'power':-500, 'somersloop':4},
    'Quantum Encoder':           {'power':-1000, 'somersloop':4},
    'Converter':                 {'power':-250, 'somersloop':2},
    'Water Extractor':           {'power':-20, 'somersloop':0},
    'Nuclear Power Plant':       {'power':2500, 'somersloop':0},
    'Fuel-Powered Generator':    {'power':250, 'somersloop':0},
    'Coal-Powered Generator':    {'power':75, 'somersloop':0},
    'Resource Well Pressurizer': {'power':-150, 'somersloop':0}
}

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


items = []
def add_recipe(i, o, build, power=0):
    if power == 0:
        power = building[build]['power']
    for item in i:
        i[item] *= -1
    info = i | o
    info |= {'Power':power}
    items.append(info)

add_recipe({'Caterium Ore':45}, 
           {'Caterium Ingot':15}, 'Smelter')
add_recipe({'Copper Ore':30}, 
           {'Copper Ingot':30}, 'Smelter')
add_recipe({'Iron Ore':30}, 
           {'Iron Ingot':30}, 'Smelter')
add_recipe({'Aluminum Scrap':60}, 
           {'Aluminum Ingot':30}, 'Smelter')
add_recipe({'Aluminum Scrap':90, 'Silica':75}, 
           {'Aluminum Ingot':60}, 'Foundry')
add_recipe({'Iron Ore':45, 'Coal':45}, 
           {'Steel Ingot':45}, 'Foundry')
add_recipe({'Iron Ore':25, 'Limestone':40}, 
           {'Iron Ingot':50}, 'Foundry')
add_recipe({'Iron Ore':75, 'Petroleum Coke':75}, 
           {'Steel Ingot':100}, 'Foundry')
add_recipe({'Iron Ore':5, 'Compacted Coal':2.5}, 
           {'Steel Ingot':10}, 'Foundry')
add_recipe({'Copper Ore':50, 'Iron Ore':50}, 
           {'Copper Ingot':100}, 'Foundry')
add_recipe({'Raw Quartz':75, 'Coal':36}, 
           {'Quartz Crystal':54}, 'Foundry')
add_recipe({'Iron Ore':40, 'Copper Ore':10}, 
           {'Iron Ingot':75}, 'Foundry')
add_recipe({'Steel Ingot':120, 'Concrete':80}, 
           {'Steel Beam':45}, 'Foundry')
add_recipe({'Steel Ingot':50, 'Concrete':30}, 
           {'Steel Pipe':50}, 'Foundry')
add_recipe({'Iron Ingot':40, 'Coal':40}, 
           {'Steel Ingot':60}, 'Foundry')
add_recipe({'Iron Ingot':15, 'Steel Ingot':15}, 
           {'Iron Plate':45}, 'Foundry')
add_recipe({'Caterium Ore':45, 'Petroleum Coke':15}, 
           {'Caterium Ingot':22.5}, 'Foundry')
add_recipe({'Copper Ore':25, 'Petroleum Coke':40}, 
           {'Copper Ingot':60}, 'Foundry')
add_recipe({'Aluminum Ingot':90}, 
           {'Aluminum Casing':60}, 'Constructor')
add_recipe({'Wire':60}, 
           {'Cable':30}, 'Constructor')
add_recipe({'Limestone':45}, 
           {'Concrete':15}, 'Constructor')
add_recipe({'Copper Ingot':300}, 
           {'Copper Powder':50}, 'Constructor')
add_recipe({'Copper Ingot':20}, 
           {'Copper Sheet':10}, 'Constructor')
add_recipe({'Plastic':30}, 
           {'Empty Canister':60}, 'Constructor')
add_recipe({'Aluminum Ingot':60}, 
           {'Empty Fluid Tank':60}, 'Constructor')
add_recipe({'Ficsite Ingot':10}, 
           {'Ficsite Trigon':30}, 'Constructor')
add_recipe({'Iron Ingot':30}, 
           {'Iron Plate':20}, 'Constructor')
add_recipe({'Iron Ingot':15}, 
           {'Iron Rod':15}, 'Constructor')
add_recipe({'Raw Quartz':37.5}, 
           {'Quartz Crystal':22.5}, 'Constructor')
add_recipe({'Caterium Ingot':12}, 
           {'Quickwire':60}, 'Constructor')
add_recipe({'SAM':120}, 
           {'Reanimated SAM':30}, 'Constructor')
add_recipe({'Iron Rod':10}, 
           {'Screw':40}, 'Constructor')
add_recipe({'Raw Quartz':22.5}, 
           {'Silica':37.5}, 'Constructor')
add_recipe({'Steel Ingot':60}, 
           {'Steel Beam':15}, 'Constructor')
add_recipe({'Steel Ingot':30}, 
           {'Steel Pipe':20}, 'Constructor')
add_recipe({'Copper Ingot':15}, 
           {'Wire':30}, 'Constructor')
add_recipe({'Aluminum Ingot':22.5}, 
           {'Steel Beam':22.5}, 'Constructor')
add_recipe({'Aluminum Ingot':7.5}, 
           {'Iron Rod':52.5}, 'Constructor')
add_recipe({'Iron Ingot':12.5}, 
           {'Screw':50}, 'Constructor')
add_recipe({'Caterium Ingot':15}, 
           {'Wire':120}, 'Constructor')
add_recipe({'Iron Ingot':100}, 
           {'Steel Pipe':25}, 'Constructor')
add_recipe({'Iron Ingot':12.5}, 
           {'Wire':22.5}, 'Constructor')
add_recipe({'Steel Ingot':40}, 
           {'Empty Canister':40}, 'Constructor')
add_recipe({'Steel Ingot':12}, 
           {'Iron Rod':48}, 'Constructor')
add_recipe({'Steel Beam':5}, 
           {'Screw':260}, 'Constructor')
add_recipe({'Copper Sheet':25, 'Quickwire':100}, 
           {'AI Limiter':5}, 'Assembler')
add_recipe({'Aluminum Ingot':30, 'Copper Ingot':10}, 
           {'Alclad Aluminum Sheet':30}, 'Assembler')
add_recipe({'Adaptive Control Unit':1.5, 'Supercomputer':0.75}, 
           {'Assembly Director System':0.75}, 'Assembler')
add_recipe({'Stator':2.5, 'Cable':50}, 
           {'Automated Wiring':2.5}, 'Assembler')
add_recipe({'Coal':15, 'Sulfur':15}, 
           {'Black Powder':30}, 'Assembler')
add_recipe({'Copper Sheet':15, 'Plastic':30}, 
           {'Circuit Board':7.5}, 'Assembler')
add_recipe({'Stator':6, 'AI Limiter':4}, 
           {'Electromagnetic Control Rod':4}, 'Assembler')
add_recipe({'Steel Beam':18, 'Concrete':36}, 
           {'Encased Industrial Beam':6}, 'Assembler')
add_recipe({'Plutonium Pellet':10, 'Concrete':20}, 
           {'Encased Plutonium Cell':5}, 'Assembler')
add_recipe({'Alclad Aluminum Sheet':37.5, 'Copper Sheet':22.5}, 
           {'Heat Sink':7.5}, 'Assembler')
add_recipe({'Rifle Ammo':50, 'High-Speed Connector':2.5}, 
           {'Homing Rifle Ammo':25}, 'Assembler')
add_recipe({'Versatile Framework':2.5, 'Electromagnetic Control Rod':1}, 
           {'Magnetic Field Generator':1}, 'Assembler')
add_recipe({'Reinforced Iron Plate':3, 'Iron Rod':12}, 
           {'Modular Frame':2}, 'Assembler')
add_recipe({'Rotor':10, 'Stator':10}, 
           {'Motor':5}, 'Assembler')
add_recipe({'Fused Modular Frame':1, 'Radio Control Unit':2}, 
           {'Pressure Conversion Cube':1}, 'Assembler')
add_recipe({'Iron Plate':30, 'Screw':60}, 
           {'Reinforced Iron Plate':5}, 'Assembler')
add_recipe({'Copper Sheet':15, 'Smokeless Powder':10}, 
           {'Rifle Ammo':75}, 'Assembler')
add_recipe({'Iron Rod':20, 'Screw':100}, 
           {'Rotor':4}, 'Assembler')
add_recipe({'Reinforced Iron Plate':2, 'Rotor':2}, 
           {'Smart Plating':2}, 'Assembler')
add_recipe({'Steel Pipe':15, 'Wire':40}, 
           {'Stator':5}, 'Assembler')
add_recipe({'Modular Frame':2.5, 'Steel Beam':30}, 
           {'Versatile Framework':5}, 'Assembler')
add_recipe({'Iron Plate':11.25, 'Rubber':3.75}, 
           {'Reinforced Iron Plate':3.75}, 'Assembler')
add_recipe({'Aluminum Ingot':150, 'Copper Ingot':75}, 
           {'Aluminum Casing':112.5}, 'Assembler')
add_recipe({'Reinforced Iron Plate':7.5, 'Screw':140}, 
           {'Modular Frame':5}, 'Assembler')
add_recipe({'Iron Plate':90, 'Screw':250}, 
           {'Reinforced Iron Plate':15}, 'Assembler')
add_recipe({'Plastic':12.5, 'Quickwire':37.5}, 
           {'Circuit Board':8.75}, 'Assembler')
add_recipe({'Raw Quartz':22.5, 'Limestone':37.5}, 
           {'Silica':52.5}, 'Assembler')
add_recipe({'Iron Plate':30, 'Copper Sheet':15}, 
           {'Empty Canister':60}, 'Assembler')
add_recipe({'Iron Ingot':37.5, 'Plastic':7.5}, 
           {'Iron Plate':75}, 'Assembler')
add_recipe({'Coal':25, 'Sulfur':25}, 
           {'Compacted Coal':25}, 'Assembler')
add_recipe({'Copper Sheet':22.5, 'Screw':195}, 
           {'Rotor':11.25}, 'Assembler')
add_recipe({'Circuit Board':5, 'Crystal Oscillator':5/3}, 
           {'Computer':10/3}, 'Assembler')
add_recipe({'Electromagnetic Control Rod':3.75, 'Rotor':7.5}, 
           {'Motor':7.5}, 'Assembler')
add_recipe({'Rubber':20, 'Petroleum Coke':40}, 
           {'Circuit Board':5}, 'Assembler')
add_recipe({'Stator':8, 'High-Speed Connector':4}, 
           {'Electromagnetic Control Rod':8}, 'Assembler')
add_recipe({'Steel Pipe':24, 'Concrete':20}, 
           {'Encased Industrial Beam':4}, 'Assembler')
add_recipe({'Sulfur':7.5, 'Compacted Coal':15}, 
           {'Black Powder':45}, 'Assembler')
add_recipe({'Silica':15, 'Limestone':60}, 
           {'Concrete':50}, 'Assembler')
add_recipe({'Caterium Ingot':7.5, 'Copper Ingot':37.5}, 
           {'Quickwire':90}, 'Assembler')
add_recipe({'Copper Ingot':12, 'Caterium Ingot':3}, 
           {'Wire':90}, 'Assembler')
add_recipe({'Aluminum Casing':30, 'Rubber':30}, 
           {'Heat Sink':10}, 'Assembler')
add_recipe({'Wire':45, 'Rubber':30}, 
           {'Cable':100}, 'Assembler')
add_recipe({'Radio Control Unit':6, 'Cooling System':6}, 
           {'Supercomputer':3}, 'Assembler')
add_recipe({'Quickwire':120, 'Plastic':28}, 
           {'AI Limiter':8}, 'Assembler')
add_recipe({'Encased Plutonium Cell':10, 'Pressure Conversion Cube':0.5}, 
           {'Plutonium Fuel Rod':0.5}, 'Assembler')
add_recipe({'Quickwire':7.5, 'Rubber':5}, 
           {'Cable':27.5}, 'Assembler')
add_recipe({'Steel Pipe':16, 'Quickwire':60}, 
           {'Stator':8}, 'Assembler')
add_recipe({'Limestone':100, 'Rubber':20}, 
           {'Concrete':90}, 'Assembler')
add_recipe({'Copper Sheet':27.5, 'Silica':27.5}, 
           {'Circuit Board':12.5}, 'Assembler')
add_recipe({'Steel Pipe':10, 'Wire':30}, 
           {'Rotor':5}, 'Assembler')
add_recipe({'Reinforced Iron Plate':2, 'Steel Pipe':10}, 
           {'Modular Frame':3}, 'Assembler')
add_recipe({'Iron Plate':18.75, 'Wire':37.5}, 
           {'Reinforced Iron Plate':5.625}, 'Assembler')
add_recipe({'Automated Wiring':5, 'Circuit Board':5, 'Heavy Modular Frame':1, 'Computer':2}, 
           {'Adaptive Control Unit':1}, 'Manufacturer')
add_recipe({'Thermal Propulsion Rocket':1, 'Singularity Cell':5, 'Superposition Oscillator':2, 'Dark Matter Crystal':40}, 
           {'Ballistic Warp Drive':1}, 'Manufacturer', -1000)
add_recipe({'Circuit Board':10, 'Cable':20, 'Plastic':40}, 
           {'Computer':2.5}, 'Manufacturer')
add_recipe({'Quartz Crystal':18, 'Cable':14, 'Reinforced Iron Plate':2.5}, 
           {'Crystal Oscillator':1}, 'Manufacturer')
add_recipe({'Modular Frame':10, 'Steel Pipe':40, 'Encased Industrial Beam':10, 'Screw':240}, 
           {'Heavy Modular Frame':2}, 'Manufacturer')
add_recipe({'Quickwire':210, 'Cable':37.5, 'Circuit Board':3.75}, 
           {'High-Speed Connector':3.75}, 'Manufacturer')
add_recipe({'Motor':2, 'Rubber':15, 'Smart Plating':2}, 
           {'Modular Engine':1}, 'Manufacturer')
add_recipe({'Encased Plutonium Cell':7.5, 'Steel Beam':4.5, 'Electromagnetic Control Rod':1.5, 'Heat Sink':2.5}, 
           {'Plutonium Fuel Rod':0.25}, 'Manufacturer')
add_recipe({'Aluminum Casing':40, 'Crystal Oscillator':1.25, 'Computer':2.5}, 
           {'Radio Control Unit':2.5}, 'Manufacturer')
add_recipe({'Reanimated SAM':60, 'Wire':50, 'Steel Pipe':30}, 
           {'SAM Fluctuator':10}, 'Manufacturer')
add_recipe({'Nuclear Pasta':1, 'Dark Matter Crystal':20, 'Iron Plate':100, 'Concrete':200}, 
           {'Singularity Cell':10}, 'Manufacturer', 0)
add_recipe({'Computer':7.5, 'AI Limiter':3.75, 'High-Speed Connector':5.625, 'Plastic':52.5}, 
           {'Supercomputer':1.875}, 'Manufacturer')
add_recipe({'Modular Engine':2.5, 'Turbo Motor':1, 'Cooling System':3, 'Fused Modular Frame':1}, 
           {'Thermal Propulsion Rocket':1}, 'Manufacturer')
add_recipe({'Cooling System':7.5, 'Radio Control Unit':3.75, 'Motor':7.5, 'Rubber':45}, 
           {'Turbo Motor':1.875}, 'Manufacturer')
add_recipe({'Rifle Ammo':125, 'Aluminum Casing':15, 'Packaged Turbofuel':15}, 
           {'Turbo Rifle Ammo':250}, 'Manufacturer')
add_recipe({'Encased Uranium Cell':20, 'Encased Industrial Beam':1.2, 'Electromagnetic Control Rod':2}, 
           {'Uranium Fuel Rod':0.4}, 'Manufacturer')
add_recipe({'Stator':3.75, 'Wire':75, 'High-Speed Connector':1.875}, 
           {'Automated Wiring':7.5}, 'Manufacturer')
add_recipe({'Circuit Board':15, 'Quickwire':52.5, 'Rubber':22.5}, 
           {'Computer':3.75}, 'Manufacturer')
add_recipe({'Sulfur':45, 'Alclad Aluminum Sheet':52.5, 'Plastic':60, 'Wire':90}, 
           {'Battery':30}, 'Manufacturer')
add_recipe({'Modular Frame':3.75, 'Steel Beam':22.5, 'Rubber':30}, 
           {'Versatile Framework':7.5}, 'Manufacturer')
add_recipe({'Modular Frame':7.5, 'Encased Industrial Beam':9.375, 'Steel Pipe':33.75, 'Concrete':20.625}, 
           {'Heavy Modular Frame':2.8125}, 'Manufacturer')
add_recipe({'Modular Frame':18.75, 'Encased Industrial Beam':11.25, 'Rubber':75, 'Screw':390}, 
           {'Heavy Modular Frame':3.75}, 'Manufacturer')
add_recipe({'Uranium':25, 'Silica':15, 'Sulfur':25, 'Quickwire':75}, 
           {'Encased Uranium Cell':20}, 'Manufacturer')
add_recipe({'Quartz Crystal':18.75, 'Rubber':13.125, 'AI Limiter':1.875}, 
           {'Crystal Oscillator':1.875}, 'Manufacturer')
add_recipe({'Reinforced Iron Plate':2.5, 'Rotor':2.5, 'Plastic':7.5}, 
           {'Smart Plating':5}, 'Manufacturer')
add_recipe({'Heat Sink':15, 'High-Speed Connector':7.5, 'Quartz Crystal':45}, 
           {'Radio Control Unit':3.75}, 'Manufacturer')
add_recipe({'Crystal Oscillator':1.5, 'Circuit Board':15, 'Aluminum Casing':90, 'Rubber':45}, 
           {'Radio Control Unit':4.5}, 'Manufacturer')
add_recipe({'Rotor':3.75, 'Stator':3.75, 'Crystal Oscillator':1.25}, 
           {'Motor':7.5}, 'Manufacturer')
add_recipe({'Quickwire':90, 'Silica':37.5, 'Circuit Board':3}, 
           {'High-Speed Connector':3}, 'Manufacturer')
add_recipe({'Computer':7.2, 'Electromagnetic Control Rod':2.4, 'Battery':24, 'Wire':60}, 
           {'Supercomputer':2.4}, 'Manufacturer')
add_recipe({'Motor':6.5625, 'Radio Control Unit':8.4375, 'Electromagnetic Control Rod':4.6875, 'Rotor':6.5625}, 
           {'Turbo Motor':2.8125}, 'Manufacturer')
add_recipe({'Motor':7.5, 'Pressure Conversion Cube':1.875, 'Packaged Nitrogen Gas':45, 'Stator':15}, 
           {'Turbo Motor':3.75}, 'Manufacturer')
add_recipe({'Encased Uranium Cell':20, 'Electromagnetic Control Rod':2, 'Crystal Oscillator':0.6, 'Rotor':2}, 
           {'Uranium Fuel Rod':0.6}, 'Manufacturer')
add_recipe({'Bauxite':120, 'Water':180}, 
           {'Alumina Solution':120, 'Silica':50}, 'Refinery')
add_recipe({'Alumina Solution':240, 'Coal':120}, 
           {'Aluminum Scrap':360, 'Water':120}, 'Refinery')
add_recipe({'Crude Oil':60}, 
           {'Fuel':40, 'Polymer Resin':30}, 'Refinery')
add_recipe({'Rocket Fuel':40, 'Power Shard':2.5}, 
           {'Ionized Fuel':40, 'Compacted Coal':5}, 'Refinery')
add_recipe({'Heavy Oil Residue':40}, 
           {'Petroleum Coke':120}, 'Refinery')
add_recipe({'Crude Oil':30}, 
           {'Plastic':20, 'Heavy Oil Residue':10}, 'Refinery')
add_recipe({'Heavy Oil Residue':60}, 
           {'Fuel':40}, 'Refinery')
add_recipe({'Polymer Resin':60, 'Water':20}, 
           {'Plastic':20}, 'Refinery')
add_recipe({'Polymer Resin':40, 'Water':40}, 
           {'Rubber':20}, 'Refinery')
add_recipe({'Crude Oil':30}, 
           {'Rubber':20, 'Heavy Oil Residue':20}, 'Refinery')
add_recipe({'Black Powder':20, 'Heavy Oil Residue':10}, 
           {'Smokeless Powder':20}, 'Refinery')
add_recipe({'Sulfur':50, 'Water':50}, 
           {'Sulfuric Acid':50}, 'Refinery')
add_recipe({'Wire':37.5, 'Heavy Oil Residue':15}, 
           {'Cable':67.5}, 'Refinery')
add_recipe({'Heavy Oil Residue':30, 'Packaged Water':60}, 
           {'Packaged Fuel':60}, 'Refinery')
add_recipe({'Alumina Solution':180, 'Petroleum Coke':60}, 
           {'Aluminum Scrap':300, 'Water':105}, 'Refinery')
add_recipe({'Crude Oil':30}, 
           {'Heavy Oil Residue':40, 'Polymer Resin':20}, 'Refinery')
add_recipe({'Caterium Ore':54, 'Sulfuric Acid':30}, 
           {'Caterium Ingot':36}, 'Refinery')
add_recipe({'Copper Ore':45, 'Sulfuric Acid':25}, 
           {'Copper Ingot':110}, 'Refinery')
add_recipe({'Iron Ore':50, 'Sulfuric Acid':10}, 
           {'Iron Ingot':100}, 'Refinery')
add_recipe({'Polymer Resin':30, 'Water':30}, 
           {'Fabric':30}, 'Refinery')
add_recipe({'Crude Oil':60}, 
           {'Polymer Resin':130, 'Heavy Oil Residue':20}, 'Refinery')
add_recipe({'Caterium Ore':24, 'Water':24}, 
           {'Caterium Ingot':12}, 'Refinery')
add_recipe({'Copper Ore':15, 'Water':10}, 
           {'Copper Ingot':37.5}, 'Refinery')
add_recipe({'Iron Ore':35, 'Water':20}, 
           {'Iron Ingot':65}, 'Refinery')
add_recipe({'Raw Quartz':67.5, 'Water':37.5}, 
           {'Quartz Crystal':52.5}, 'Refinery')
add_recipe({'Raw Quartz':120, 'Nitric Acid':10}, 
           {'Dissolved Silica':60, 'Quartz Crystal':75}, 'Refinery')
add_recipe({'Rubber':30, 'Fuel':30}, 
           {'Plastic':60}, 'Refinery')
add_recipe({'Plastic':30, 'Fuel':30}, 
           {'Rubber':60}, 'Refinery')
add_recipe({'Bauxite':200, 'Water':200}, 
           {'Alumina Solution':240}, 'Refinery')
add_recipe({'Copper Ingot':22.5, 'Water':22.5}, 
           {'Copper Sheet':22.5}, 'Refinery')
add_recipe({'Heavy Oil Residue':37.5, 'Compacted Coal':30}, 
           {'Turbofuel':30}, 'Refinery')
add_recipe({'Fuel':22.5, 'Compacted Coal':15}, 
           {'Turbofuel':18.75}, 'Refinery')
add_recipe({'Limestone':120, 'Water':100}, 
           {'Concrete':80}, 'Refinery')
add_recipe({'Sulfuric Acid':50, 'Alumina Solution':40, 'Aluminum Casing':20}, 
           {'Battery':20, 'Water':30}, 'Blender')
add_recipe({'Assembly Director System':0.5, 'Ficsite Trigon':40, 'Water':10}, 
           {'Biochemical Sculptor':2}, 'Blender', -1000)
add_recipe({'Heat Sink':12, 'Rubber':12, 'Water':30, 'Nitrogen Gas':150}, 
           {'Cooling System':6}, 'Blender')
add_recipe({'Uranium':50, 'Concrete':15, 'Sulfuric Acid':40}, 
           {'Encased Uranium Cell':25, 'Sulfuric Acid':10}, 'Blender')
add_recipe({'Heavy Modular Frame':1.5, 'Aluminum Casing':75, 'Nitrogen Gas':37.5}, 
           {'Fused Modular Frame':1.5}, 'Blender')
add_recipe({'Nitrogen Gas':120, 'Water':30, 'Iron Plate':10}, 
           {'Nitric Acid':30}, 'Blender')
add_recipe({'Uranium Waste':37.5, 'Silica':25, 'Nitric Acid':15, 'Sulfuric Acid':15}, 
           {'Non-Fissile Uranium':50, 'Water':15}, 'Blender')
add_recipe({'Turbofuel':60, 'Nitric Acid':10}, 
           {'Rocket Fuel':100, 'Compacted Coal':10}, 'Blender')
add_recipe({'Rifle Ammo':125, 'Aluminum Casing':15, 'Turbofuel':15}, 
           {'Turbo Rifle Ammo':250}, 'Blender')
add_recipe({'Heat Sink':10, 'Motor':2.5, 'Nitrogen Gas':60}, 
           {'Cooling System':5}, 'Blender')
add_recipe({'Heavy Oil Residue':50, 'Water':100}, 
           {'Fuel':100}, 'Blender')
add_recipe({'Dissolved Silica':120, 'Limestone':50, 'Water':100}, 
           {'Silica':270, 'Water':80}, 'Blender')
add_recipe({'Uranium':25, 'Uranium Waste':25, 'Nitric Acid':15, 'Sulfuric Acid':25}, 
           {'Non-Fissile Uranium':100, 'Water':40}, 'Blender')
add_recipe({'Heavy Modular Frame':3, 'Aluminum Ingot':150, 'Nitric Acid':24, 'Fuel':30}, 
           {'Fused Modular Frame':3}, 'Blender')
add_recipe({'Bauxite':150, 'Coal':100, 'Sulfuric Acid':50, 'Water':60}, 
           {'Aluminum Scrap':300, 'Water':50}, 'Blender')
add_recipe({'Fuel':100, 'Nitrogen Gas':75, 'Sulfur':100, 'Coal':50}, 
           {'Rocket Fuel':150, 'Compacted Coal':25}, 'Blender')
add_recipe({'Fuel':15, 'Heavy Oil Residue':30, 'Sulfur':22.5, 'Petroleum Coke':22.5}, 
           {'Turbofuel':45}, 'Blender')
add_recipe({'Fuel':40, 'Empty Canister':40}, 
           {'Packaged Fuel':40}, 'Packager')
add_recipe({'Nitrogen Gas':240, 'Empty Fluid Tank':60}, 
           {'Packaged Nitrogen Gas':60}, 'Packager')
add_recipe({'Rocket Fuel':120, 'Empty Fluid Tank':60}, 
           {'Packaged Rocket Fuel':60}, 'Packager')
add_recipe({'Turbofuel':20, 'Empty Canister':20}, 
           {'Packaged Turbofuel':20}, 'Packager')
add_recipe({'Water':60, 'Empty Canister':60}, 
           {'Packaged Water':60}, 'Packager')
add_recipe({'Diamonds':30, 'Dark Matter Residue':150}, 
           {'Dark Matter Crystal':30}, 'Particle Accelerator', -1000)
add_recipe({'Coal':600}, 
           {'Diamonds':30}, 'Particle Accelerator')
add_recipe({'Plutonium Waste':10, 'Singularity Cell':10, 'Dark Matter Residue':200}, 
           {'Ficsonium':10}, 'Particle Accelerator', -1000)
add_recipe({'Copper Powder':100, 'Pressure Conversion Cube':0.5}, 
           {'Nuclear Pasta':0.5}, 'Particle Accelerator', -1000)
add_recipe({'Non-Fissile Uranium':100, 'Uranium Waste':25}, 
           {'Plutonium Pellet':30}, 'Particle Accelerator')
add_recipe({'Coal':240, 'Limestone':480}, 
           {'Diamonds':20}, 'Particle Accelerator')
add_recipe({'Dark Matter Residue':200}, 
           {'Dark Matter Crystal':20}, 'Particle Accelerator', -1000)
add_recipe({'Time Crystal':30, 'Dark Matter Residue':150}, 
           {'Dark Matter Crystal':60}, 'Particle Accelerator', -1000)
add_recipe({'Non-Fissile Uranium':75, 'Aluminum Casing':10}, 
           {'Encased Plutonium Cell':10}, 'Particle Accelerator')
add_recipe({'Crude Oil':200}, 
           {'Diamonds':40}, 'Particle Accelerator')
add_recipe({'Petroleum Coke':720}, 
           {'Diamonds':30}, 'Particle Accelerator')
add_recipe({'Coal':600, 'Packaged Turbofuel':40}, 
           {'Diamonds':60}, 'Particle Accelerator')
add_recipe({'Magnetic Field Generator':4, 'Neural-Quantum Processor':4, 'Superposition Oscillator':4, 'Excited Photonic Matter':100}, 
           {'AI Expansion Server':4, 'Dark Matter Residue':100}, 'Quantum Encoder')
add_recipe({'SAM Fluctuator':12.5, 'Power Shard':7.5, 'Superposition Oscillator':7.5, 'Excited Photonic Matter':60}, 
           {'Alien Power Matrix':2.5, 'Dark Matter Residue':60}, 'Quantum Encoder')
add_recipe({'Ficsonium':5, 'Electromagnetic Control Rod':5, 'Ficsite Trigon':100, 'Excited Photonic Matter':50}, 
           {'Ficsonium Fuel Rod':2.5, 'Dark Matter Residue':50}, 'Quantum Encoder')
add_recipe({'Time Crystal':15, 'Supercomputer':3, 'Ficsite Trigon':45, 'Excited Photonic Matter':75}, 
           {'Neural-Quantum Processor':3, 'Dark Matter Residue':75}, 'Quantum Encoder')
add_recipe({'Dark Matter Crystal':30, 'Crystal Oscillator':5, 'Alclad Aluminum Sheet':45, 'Excited Photonic Matter':125}, 
           {'Superposition Oscillator':5, 'Dark Matter Residue':125}, 'Quantum Encoder')
add_recipe({'Time Crystal':10, 'Dark Matter Crystal':10, 'Quartz Crystal':60, 'Excited Photonic Matter':60}, 
           {'Power Shard':5, 'Dark Matter Residue':60}, 'Quantum Encoder')
add_recipe({'Reanimated SAM':50}, 
           {'Dark Matter Residue':100}, 'Converter')
add_recipe({}, 
           {'Excited Photonic Matter':200}, 'Converter')
add_recipe({'Reanimated SAM':60, 'Aluminum Ingot':120}, 
           {'Ficsite Ingot':30}, 'Converter')
add_recipe({'Reanimated SAM':45, 'Caterium Ingot':60}, 
           {'Ficsite Ingot':15}, 'Converter')
add_recipe({'Reanimated SAM':40, 'Iron Ingot':240}, 
           {'Ficsite Ingot':10}, 'Converter')
add_recipe({'Diamonds':12}, 
           {'Time Crystal':6}, 'Converter')
add_recipe({'Packaged Rocket Fuel':240, 'Dark Matter Crystal':80}, 
           {'Ionized Fuel':200, 'Compacted Coal':40}, 'Converter')
add_recipe({'Coal':120, 'Quartz Crystal':45}, 
           {'Diamonds':15}, 'Converter')
add_recipe({}, 
           {'Water':120}, 'Water Extractor')
add_recipe({'Plutonium Fuel Rod':0.1, 'Water':240}, 
           {'Plutonium Waste':1}, 'Nuclear Power Plant')
add_recipe({'Uranium Fuel Rod':0.2, 'Water':240}, 
           {'Uranium Waste':10}, 'Nuclear Power Plant')
add_recipe({'Ficsonium Fuel Rod':1, 'Water':240}, 
           {}, 'Nuclear Power Plant')
add_recipe({'Fuel':20}, 
           {}, 'Fuel-Powered Generator')
add_recipe({'Turbofuel':7.5}, 
           {}, 'Fuel-Powered Generator')
add_recipe({'Rocket Fuel':12.5/3}, 
           {}, 'Fuel-Powered Generator')
add_recipe({'Ionized Fuel':3}, 
           {}, 'Fuel-Powered Generator')
add_recipe({'Coal':15}, 
           {}, 'Coal-Powered Generator')
add_recipe({'Compacted Coal':50/7}, 
           {}, 'Coal-Powered Generator')
add_recipe({'Petroleum Coke':25}, 
           {}, 'Coal-Powered Generator')
add_recipe({}, 
           {'Iron Ore':resource['Iron Ore']/(39+42+46)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'Caterium Ore':resource['Caterium Ore']/(9+8)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'Copper Ore':resource['Copper Ore']/(13+29+13)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'Limestone':resource['Limestone']/(15+50+29)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'Coal':resource['Coal']/(15+31+16)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'Raw Quartz':resource['Raw Quartz']/(3+7+7)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'Sulfur':resource['Sulfur']/(6+5+5)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'Uranium':resource['Uranium']/(2+3)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'Bauxite':resource['Bauxite']/(5+6+6)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'SAM':resource['SAM']/(10+6+3)/2.5}, 'Miner Mk.3')
add_recipe({}, 
           {'Crude Oil':resource['Crude Oil']/(10+12+8)/2.5}, 'Oil Extractor')
add_recipe({}, 
           {'Nitrogen Gas':resource['Nitrogen Gas']/(2+7+36)/2.5}, 'Resource Well Pressurizer')

import json
with open(r'Satisfactory-Linear-Programming\satisfactory_data.json', 'w') as file:
    file.write('[\n')
    for i in items:
        file.write('    ')
        json.dump(i, file)
        if i != items[-1]: file.write(',')
        file.write('\n')
    file.write(']')