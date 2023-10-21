import tensorflow
import torch

print(tensorflow.__version__)
print(torch.__version__)

my_list = [1, 2, 3]
nested_list = [4, 5]

my_list.append(nested_list)

print(my_list)