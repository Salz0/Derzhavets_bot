from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from messages import MESSAGES, ROOMS, PETS_AND_FRIENDS

# Q&A Keyboard
Q_and_A_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

q_and_exit_button = KeyboardButton(MESSAGES["exit_Q"])
Q_and_A_keyboard.add(q_and_exit_button)
# -----------------------------------------------------------------

# Questionnaire place keyboard

# PLACE
place_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

place1_button = KeyboardButton(MESSAGES["place1"])
place2_button = KeyboardButton(MESSAGES["place2"])

place_kb.add(place2_button).add(place1_button)

# FLOOR (PLACE1)
place1_floor_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
floor1_button = KeyboardButton(MESSAGES["floor1"])
floor2_button = KeyboardButton(MESSAGES["floor2"])

place1_floor_kb.add(floor1_button).add(floor2_button)

# FLOOR (IF PLACE2)
place2_floor_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
floor3_button = KeyboardButton(MESSAGES["mountain_bot"])
floor4_button = KeyboardButton(MESSAGES["mountain_top"])

place2_floor_kb.add(floor3_button).add(floor4_button)


# PLACE1->FLOOR1 (MAIBORODA 1st floor) (ROOMS)
place1_floor1_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
room1_button = KeyboardButton(ROOMS["room1"])
room2_button = KeyboardButton(ROOMS["room2"])
room3_button = KeyboardButton(ROOMS["room3"])


place1_floor1_kb.add(room1_button).add(room2_button).add(room3_button)

# PLACE1->FLOOR2 (MAIBORODA 2nd floor) (ROOMS)
place1_floor2_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
room4_button = KeyboardButton(ROOMS["room4"])
room5_button = KeyboardButton(ROOMS["room5"])
room6_button = KeyboardButton(ROOMS["room6"])

place1_floor2_kb.add(room4_button).add(room5_button).add(room6_button)

# PLACE2->Bottom_of_mountain (Mountain bottom)
place2_floor1_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
river_button = KeyboardButton(ROOMS["river"])
tree_button = KeyboardButton(ROOMS["tree"])

place2_floor1_kb.add(tree_button).add(river_button)

# PLACE2->TOP_OF_MOUNTAIN
place2_floor2_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
igloo_button = KeyboardButton(ROOMS["igloo"])
cave_button = KeyboardButton(ROOMS["cave"])

place2_floor2_kb.add(cave_button).add(igloo_button)


# save_button = KeyboardButton(MESSAGES["save"])
# room1
room1_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
room1_friend1_b = KeyboardButton(PETS_AND_FRIENDS["room1_friend1"])
room1_friend2_b = KeyboardButton(PETS_AND_FRIENDS["room1_friend2"])

room1_kb.add(room1_friend2_b).add(room1_friend1_b)

# room2
room2_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
room2_friend1_b = KeyboardButton(PETS_AND_FRIENDS["room2_friend1"])
room2_friend2_b = KeyboardButton(PETS_AND_FRIENDS["room2_friend2"])

room2_kb.add(room2_friend2_b).add(room2_friend1_b)

# room3
room3_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
room3_friend1_b = KeyboardButton(PETS_AND_FRIENDS["room3_friend1"])
room3_friend2_b = KeyboardButton(PETS_AND_FRIENDS["room3_friend2"])

room3_kb.add(room3_friend2_b).add(room3_friend1_b)


# room4
room4_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
room4_friend1_b = KeyboardButton(PETS_AND_FRIENDS["room4_friend1"])
room4_friend2_b = KeyboardButton(PETS_AND_FRIENDS["room4_friend2"])

room4_kb.add(room4_friend2_b).add(room4_friend1_b)

# room5
room5_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
room5_friend1_b = KeyboardButton(PETS_AND_FRIENDS["room5_friend1"])
room5_friend2_b = KeyboardButton(PETS_AND_FRIENDS["room5_friend2"])

room5_kb.add(room5_friend2_b).add(room5_friend1_b)

# room6
room6_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
room6_friend1_b = KeyboardButton(PETS_AND_FRIENDS["room6_friend1"])
room6_friend2_b = KeyboardButton(PETS_AND_FRIENDS["room6_friend2"])

room6_kb.add(room6_friend2_b).add(room6_friend1_b)

# river
river_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
river1_b = KeyboardButton(PETS_AND_FRIENDS["pet_river1"])
river2_b = KeyboardButton(PETS_AND_FRIENDS["pet_river2"])

river_kb.add(river1_b).add(river2_b)

# tree
tree_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
tree1_b = KeyboardButton(PETS_AND_FRIENDS["pet_tree1"])
tree2_b = KeyboardButton(PETS_AND_FRIENDS["pet_tree2"])

tree_kb.add(tree1_b).add(tree2_b)

# igloo
igloo_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
igloo1_b = KeyboardButton(PETS_AND_FRIENDS["pet_igloo1"])
igloo2_b = KeyboardButton(PETS_AND_FRIENDS["pet_igloo2"])

igloo_kb.add(igloo2_b).add(igloo1_b)

# cave
cave_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cave1_b = KeyboardButton(PETS_AND_FRIENDS["pet_cave1"])
cave2_b = KeyboardButton(PETS_AND_FRIENDS["pet_cave2"])

cave_kb.add(cave2_b).add(cave1_b)


# -----------------------------------------------------------------
