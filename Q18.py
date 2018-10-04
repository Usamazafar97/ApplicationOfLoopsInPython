def kinetic_energy(mass,vilocity):
    
    kineticenergy=(mass*(vilocity**2))/2.0
    return kineticenergy
mass=input("enter the value of mass in grams")
vilocity=input("enter the value of vilocity in kilmeter per second ")
Kinetic_Energy=kinetic_energy(mass,vilocity)
print Kinetic_Energy