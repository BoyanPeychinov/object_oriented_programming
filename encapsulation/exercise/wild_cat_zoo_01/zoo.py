class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker):
        worker_object = [w for w in self.workers if w.name == worker]
        if not worker_object:
            return f"There is no {worker} in the zoo"
        self.workers.remove(worker_object[0])
        return f"{worker} fired successfully"

    def pay_workers(self):
        total_salaries = sum([w.salary for w in self.workers])
        if not self.__budget >= total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_tend_expenses = sum(a.get_needs() for a in self.animals)
        if not self.__budget >= total_tend_expenses:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_tend_expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def __for_filtering(self, array, class_name):
        filtered_arr = [x for x in array if x.__class__.__name__ == class_name]
        return filtered_arr

    def animals_status(self):
        lions_list = self.__for_filtering(self.animals, "Lion")
        cheetahs_list = self.__for_filtering(self.animals, "Cheetah")
        tigers_list = self.__for_filtering(self.animals, "Tiger")
        result = f"You have {len(self.animals)} animals"
        result += f"\n----- {len(lions_list)} Lions:\n"
        result += '\n'.join(repr(lion) for lion in lions_list)
        result += f"\n----- {len(tigers_list)} Tigers:\n"
        result += '\n'.join(repr(tiger) for tiger in tigers_list)
        result += f"\n----- {len(cheetahs_list)} Cheetahs:\n"
        result += '\n'.join(repr(cheetah) for cheetah in cheetahs_list)
        return result

    def workers_status(self):
        keepers_list = self.__for_filtering(self.workers, "Keeper")
        caretakers_list = self.__for_filtering(self.workers, "Caretaker")
        vets_list = self.__for_filtering(self.workers, "Vet")
        result = f"You have {len(self.workers)} workers"
        result += f"\n----- {len(keepers_list)} Keepers:\n"
        result += '\n'.join(repr(keeper) for keeper in keepers_list)
        result += f"\n----- {len(caretakers_list)} Caretakers:\n"
        result += '\n'.join(repr(caretaker) for caretaker in caretakers_list)
        result += f"\n----- {len(vets_list)} Vets:\n"
        result += '\n'.join(repr(vet) for vet in vets_list)
        return result