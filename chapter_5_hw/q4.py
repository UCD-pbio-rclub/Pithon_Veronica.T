#Question 4
#Write a function which allows a user to
#compare and/or contrast two instances of your class "LongOrganism"

from q2 import Organism
from q3 import LongOrganism

def CompareTaxa():
    a = input('First Organism: ')
    b = input('Second Organism: ')
    print(a.LongDescription())
    print(b.LongDescription())

#'Plantae', 'Tracheophyta', 'Magnoliopsida', 'Dipsacales', 'Caprifoliaceae', 'Scabiosa', 'columbaria', 'Dove pincushion', 'Europe and South Africa'
#'Animalia', 'Chordata', 'Mammalia', 'Carnivora', 'Canidae', 'Canis', 'lupus', 'global'
