#Question 2
#Write a class called "Organism". Have the class initialize with the organism's complete taxonomic lineage (KPCOFGS) and common name.
#Write methods which allow a user to see these values in informative ways.

class Organism:
    def __init__(self, kingdom, phylum, org_class, order, family, genus, species, common_name):
        self.kingdom = kingdom
        self.phylum = phylum
        self.org_class = org_class
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species
        self.common_name = common_name

    def description(self):
        return 'Kingdom: ' +self.kingdom+ '\nPhylum: ' +self.phylum+ '\nClass: ' +self.org_class+ '\nOrder: ' +self.order+ '\nFamily: ' +self.family+ '\nGenus: ' +self.genus+ '\nSpecies: ' +self.species+ '\nCommon Name: ' +self.common_name

scabbies = Organism('Plantae', 'Tracheophyta', 'Magnoliopsida', 'Dipsacales', 'Caprifoliaceae', 'Scabiosa', 'columbaria', 'Dove pincushion')


print(scabbies.description())


#what is the point of a class?
