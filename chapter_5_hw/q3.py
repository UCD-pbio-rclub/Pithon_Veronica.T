#Question 3
#Demonstrate inheritance by importing your class "Organism" from problem 2.
#Use it to create a new class called "LongOrganism" which inherits "Organism"
#and modifies it by adding any other attributes that may be significant about an organism
#(ie ploidy, genome size, region).
#Write new methods which allow a user to see these values in informative ways.

class LongOrganism:
    def __init__(self, kingdom, phylum, org_class, order, family, genus, species, common_name, region):
        Organism.__init__(self, kingdom, phylum, org_class, order, family, genus, species, common_name)
        LongOrganism.region = region

    def LongDescription(self):
        return 'Kingdom: ' + self.kingdom + '\nPhylum: ' + self.phylum + '\nClass: ' + self.org_class + '\nOrder: ' + self.order + '\nFamily: ' + self.family + '\nGenus: ' + self.genus + '\nSpecies: ' +self.species+ '\nCommon Name: ' +self.common_name + '\nRegion: ' +self.region
    
scabbiesL = LongOrganism('Plantae', 'Tracheophyta', 'Magnoliopsida', 'Dipsacales', 'Caprifoliaceae', 'Scabiosa', 'columbaria', 'Dove pincushion', 'Europe and South Africa')


print(scabbiesL.LongDescription())
