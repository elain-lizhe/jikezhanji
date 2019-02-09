# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]
#问题：为什么是random.randint(1,101)？我觉得是random.randint(1,100)

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)
