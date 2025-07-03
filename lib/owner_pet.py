class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = Pet.confirm_pet_type(pet_type)
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name={self.name} type={self.pet_type} owner={self.owner.name if self.owner else None}>"
        
    @classmethod
    def confirm_pet_type(cls, pet_type):
        if pet_type in cls.PET_TYPES:
            return pet_type
        else:
            raise Exception("Enter another pet type")

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        # In the Owner class write a method called add_pet(self, pet) that checks that the the pet is of type Pet and adds the owner to the pet.
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Pet must be an instance of Pet class")
    
    def get_sorted_pets(self):
        # In the Owner class write a method called get_sorted_pets(self) returns a sorted list of pets by their names.
        return sorted(self.pets(), key = lambda pet: pet.name)
        # return sorted(Pet.all)

owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)
owner.get_sorted_pets()
print([pet2, pet1, pet4, pet3])
print(owner.get_sorted_pets() == [pet2, pet1, pet4, pet3])
# print(pet1)
# pet = Pet("Bosco","horse")