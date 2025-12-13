import random

# # random_integer = random.randint(1, 10)
# # print(random_integer)
# random_floating_point = random.random()
# print(f"{random_floating_point:.5f}")

# random_integer = random.randint(0, 1)
# if random_integer == 1:
#     print("Heads")
# else:
#     print("Tails")


friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# random_name = random.choice(friends)
# print(random_name)

random_name = random.randint(0, len(friends) - 1)
print(friends[random_name])

