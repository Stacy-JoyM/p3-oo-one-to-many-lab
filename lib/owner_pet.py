class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name

    def pets(self):
        """Return a list of pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to this owner, ensuring the pet is of type Pet."""
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of the owner's pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string.")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}.")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class or None.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add the pet instance to the all list
        Pet.all.append(self)

# Example Usage
# Create Owners
alice = Owner("Alice")

# Create Pets
tom = Pet("Tom", "cat", alice)
rex = Pet("Rex", "dog")

# Add a pet to an owner
alice.add_pet(rex)

# Retrieve pets owned by Alice
print(alice.pets())  # [Tom, Rex]

# Retrieve sorted pets by name
print(alice.get_sorted_pets())  # [Rex, Tom]