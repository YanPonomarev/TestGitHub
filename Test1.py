from statistics import geometric_mean

import numpy as np

from PIL.Image import Image

library = np.array([[3], [1], [0]])
message_1 = 'Привет Git'


message_2 = 'Привет отец'
message_3 = 'Куку'

message_4 = 'Че не спишь'


mean = geometric_mean([1, 2, 3, 4])

im = Image.open('file.txt')
