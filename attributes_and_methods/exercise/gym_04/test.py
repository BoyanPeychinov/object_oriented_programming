from exercise.gym_04.customer import Customer
from exercise.gym_04.equipment import Equipment
from exercise.gym_04.exercise_plan import ExercisePlan
from exercise.gym_04.gym import Gym
from exercise.gym_04.subscription import Subscription
from exercise.gym_04.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
