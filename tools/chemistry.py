"""Chemistry utils"""
from utils.functions import command

table = [
    ('Ru', 'Ruthenium', 44, 101.07), 
    ('Re', 'Rhenium', 75, 186.207), 
    ('Rf', 'Rutherfordium', 104, 261.0), 
    ('Rg', 'Unununium', 111, 272.0), 
    ('Ra', 'Radium', 88, 226.0), 
    ('Rb', 'Rubidium', 37, 85.4678), 
    ('Rn', 'Radon', 86, 220.0), 
    ('Rh', 'Rhodium', 45, 102.9055), 
    ('Be', 'Beryllium', 4, 9.012182), 
    ('Ba', 'Barium', 56, 137.327), 
    ('Bh', 'Bohrium', 107, 264.0), 
    ('Bi', 'Bismuth', 83, 208.980401), 
    ('Bk', 'Berkelium', 97, 247.0), 
    ('Br', 'Bromine', 35, 79.904), 
    ('Uuh', 'Ununhexium', 116, 292.0), 
    ('H', 'Hydrogen', 1, 1.00794), 
    ('P', 'Phosphorus', 15, 30.973762), 
    ('Os', 'Osmium', 76, 190.23), 
    ('Es', 'Einsteinium', 99, 252.0), 
    ('Hg', 'Hydrargyrum', 80, 200.59), 
    ('Ge', 'Germanium', 32, 72.64), 
    ('Gd', 'Gadolinium', 64, 157.25), 
    ('Ga', 'Gallium', 31, 69.723), 
    ('Uub', 'Ununbium', 112, 285.0), 
    ('Pr', 'Praseodymium', 59, 140.90765), 
    ('Pt', 'Platinum', 78, 192.084), 
    ('Pu', 'Plutonium', 94, 244.0), 
    ('C', 'Carbon', 6, 12.0107), 
    ('Pb', 'Lead', 82, 207.2), 
    ('Pa', 'Protactinium', 91, 231.03588), 
    ('Pd', 'Palladium', 46, 106.42), 
    ('Cd', 'Cadmium', 48, 112.411), 
    ('Po', 'Polonium', 84, 210.0), 
    ('Pm', 'Promethium', 61, 145.0), 
    ('Hs', 'Hassium', 108, 277.0), 
    ('Uuq', 'Ununquadium', 114, 289.0), 
    ('Uup', 'Ununpentium', 115, 288.0), 
    ('Uuo', 'Ununoctium', 118, 294.0), 
    ('Ho', 'Holmium', 67, 164.93032), 
    ('Hf', 'Hafnium', 72, 178.49), 
    ('K', 'Potassium', 19, 39.0983), 
    ('He', 'Helium', 2, 4.002602), 
    ('Md', 'Mendelevium', 101, 258.0), 
    ('Mg', 'Magnesium', 12, 24.305), 
    ('Mo', 'Molybdaenum', 42, 95.96), 
    ('Mn', 'Manganese', 25, 54.938045), 
    ('O', 'Oxygen', 8, 15.9994), 
    ('Mt', 'Meitnerium', 109, 268.0), 
    ('S', 'Sulphur', 16, 32.065), 
    ('W', 'Tungsten', 74, 183.84), 
    ('Zn', 'Zinc', 30, 65.38), 
    ('Eu', 'Europium', 63, 151.964), 
    ('Zr', 'Zirkonium', 40, 91.224), 
    ('Er', 'Erbium', 68, 167.259), 
    ('Ni', 'Nickel', 28, 58.6934), 
    ('No', 'Nobelium', 102, 259.0), 
    ('Na', 'Sodium', 11, 22.98976928), 
    ('Nb', 'Niobium', 41, 92.90638), 
    ('Nd', 'Neodymium', 60, 144.242), 
    ('Ne', 'Neon', 10, 20.1797), 
    ('Np', 'Neptunium', 93, 237.0), 
    ('Fr', 'Francium', 87, 223.0), 
    ('Fe', 'Iron', 26, 55.845), 
    ('Fm', 'Fermium', 100, 257.0), 
    ('B', 'Boron', 5, 10.811), 
    ('F', 'Fluorine', 9, 18.9994), 
    ('Sr', 'Strontium', 38, 87.62), 
    ('N', 'Nitrogen', 7, 14.0067), 
    ('Kr', 'Krypton', 36, 83.798), 
    ('Si', 'Silicon', 14, 28.0855), 
    ('Sn', 'Tin', 50, 118.71), 
    ('Sm', 'Samarium', 62, 150.36), 
    ('V', 'Vanadium', 23, 50.9415), 
    ('Sc', 'Scandium', 21, 44.955912), 
    ('Sb', 'Antimony', 51, 121.76), 
    ('Sg', 'Seaborgium', 106, 266.0), 
    ('Se', 'Selenium', 34, 78.96), 
    ('Co', 'Cobalt', 27, 58.933195), 
    ('Cm', 'Curium', 96, 247.0), 
    ('Cl', 'Chlorine', 17, 35.453), 
    ('Ca', 'Calcium', 20, 40.078), 
    ('Cf', 'Californium', 98, 251.0), 
    ('Ce', 'Cerium', 58, 140.116), 
    ('Xe', 'Xenon', 54, 131.293), 
    ('Lu', 'Lutetium', 71, 174.9668), 
    ('Cs', 'Cesium', 55, 132.9054519), 
    ('Cr', 'Chromium', 24, 51.9961), 
    ('Cu', 'Copper', 29, 63.546), 
    ('La', 'Lanthanum', 57, 138.90547), 
    ('Li', 'Lithium', 3, 6.941), 
    ('Tl', 'Thallium', 81, 204.3833), 
    ('Tm', 'Thulium', 69, 168.93421), 
    ('Lr', 'Lawrencium', 103, 262.0), 
    ('Th', 'Thorium', 90, 232.03806), 
    ('Ti', 'Titanium', 22, 47.867), 
    ('Te', 'Tellurium', 52, 127.6), 
    ('Tb', 'Terbium', 65, 158.92535), 
    ('Tc', 'Technetium', 43, 98.0), 
    ('Ta', 'Tantalum', 73, 180.94788), 
    ('Yb', 'Ytterbium', 70, 173.054), 
    ('Db', 'Dubnium', 105, 262.0), 
    ('Dy', 'Dysprosium', 66, 162.5001), 
    ('Ds', 'Ununnilium', 110, 271.0), 
    ('I', 'Iodine', 53, 126.90447), 
    ('U', 'Uranium', 92, 238.02891), 
    ('Y', 'Yttrium', 39, 88.90585), 
    ('Ac', 'Actinium', 89, 227.0), 
    ('Ag', 'Silver', 47, 107.8682), 
    ('Uut', 'Ununtrium', 113, 284.0), 
    ('Ir', 'Iridium', 77, 192.217), 
    ('Am', 'Americium', 95, 243.0), 
    ('Al', 'Aluminium', 13, 26.9815386), 
    ('As', 'Arsenic', 33, 74.9216), 
    ('Ar', 'Argon', 18, 39.948), 
    ('Au', 'Gold', 79, 196.966569), 
    ('At', 'Astatine', 85, 210.0), 
    ('In', 'Indium', 49, 114.818)
]

table_map = dict([(element[0], element[1:]) for element in table])


@command("atomic")
def atomic_number(code):
    """Element symbols to atomic number"""
    if type(code) is not list:
        return code
    else:
        return [str(table_map.get(el, (el, el,))[1]) for el in code]