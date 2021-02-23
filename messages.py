from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import text

# QUESTIONNAIRE MESSAGES:
questionnaire_start = text(emojize("Привіт!👋\nРозкажи, будь ласка: де та з ким ти хочеш жити 😏"))
questionnaire_floor = text(emojize("Де саме ти хотів би оселитися?🧳"))
questionnaire_room = text(emojize("Який номер кімнати в тебе з щасливих?🎰"))
questionnaire_roommates = text(emojize("Останнє, з ким ти хотів/ла би жити? 🐸"))
save_button = text(emojize("Зберегти📝"))
questionnaire_goodbye = text(emojize("Інформація буде передана на обробку, дякую за інформацію 📃"))

#       QUESTIONNAIRE BUTTONS:

place1 = text(emojize("На Майбороди, з коліверами"))
place2 = text(emojize("У горах, наодинці🌄"))

# FOR PLACE 1 (МАЙБОРОДА)
floor1 = text(emojize("На 1️⃣ поверсі"))
floor2 = text(emojize("На 2️⃣ поверсі"))
# FOR PLACE 2 (ГОРА)
mountain_bot = text(emojize("У підніжжя 🏞"))
mountain_msg = text(emojize("Обери собі компаньона!🙌"))
mountain_top = text(emojize("На вершині 🌄"))

# FOR FLOOR1 (МАЙБОРОДА)
room1 = text(emojize("1️⃣"))
room2 = text(emojize("2️⃣"))
room3 = text(emojize("3️⃣"))
# FOR FLOOR2 (МАЙБОРОДА)
room4 = text(emojize("4️⃣"))
room5 = text(emojize("5️⃣"))
room6 = text(emojize("6️⃣"))

# MAIBORODA FRIENDS
room1_friend1 = "Алекс"
room1_friend2 = "Фродо"
room2_friend1 = "Лазло"
room2_friend2 = "Каска"
room3_friend1 = "Іван"
room3_friend2 = "Василь"
room4_friend1 = "Олекса"
room4_friend2 = "Філіп"
room5_friend1 = "Фердинанд"
room5_friend2 = "Кіра"
room6_friend1 = "Леся"
room6_friend2 = "Валерій"

# FOR MOUNTAIN (bot)
river = text(emojize("Біля річки 🐸"))
tree = text(emojize("На дереві 🌳"))
# FOR MOUNTAIN (top)
igloo = text(emojize("В іглу ☃"))
cave = text(emojize("У печері 🗻"))

# FOR MOUNTAIN (RIVER) PET
pet_river1 = text(emojize("Золоту рибку!🐡"))
pet_river2 = text(emojize("Медведя!🐻"))
# FOR MOUNTAIN (TREE) PET
pet_tree1 = text(emojize("Білочку🐿"))
pet_tree2 = text(emojize("Сову🦉"))
#IGLOO PET
pet_igloo1 = text(emojize("Чукчу!⛄"))
pet_igloo2 = text(emojize("Привида!👻"))
# CAVE PET
pet_cave1 = text(emojize("Пані Самотність!🧘‍♂️"))
pet_cave2 = text(emojize("Сніговика!⛄"))



# SINGLE-PURPOSE MESSAGES:
start_message = text(emojize("Привіт!👋"))
registered_message = "Давно не бачилися!"
have_a_nice_lecture = text(emojize("Продуктивної лекції тобі! 😉"))
vote_thank_you = text(emojize("Дякую, твій голос враховано!⚖"))

# Q&A RESPONSES:
Q_and_A_welcoming_message = text(emojize("Привіт, тут ти можеш задати стільки питань, скільки забажаєш\n"
                                         "Коли закінчиш, натисни клавішу 'Вийти'😉"))
Q_and_A_confirmation_message = text(emojize("Записав!📃"))
exit_Q = "Вийти"
Q_and_A_goodbye_message = text(emojize("Дякую.\nЗадані питання будуть доставленими 🧭"))
# TEMPLATE = text(emojize())

MESSAGES = {

    "start_message": start_message,
    "registered_message": registered_message,
    "have_a_nice_lecture": have_a_nice_lecture,
    "vote_thank_you": vote_thank_you,
    # Q&A RESPONSES:
    "Q_and_A_welcoming_message": Q_and_A_welcoming_message,
    "Q_and_A_confirmation_message": Q_and_A_confirmation_message,
    "exit_Q": exit_Q,
    "Q_and_A_goodbye_message": Q_and_A_goodbye_message,
    # QUESTIONNAIRE RESPONSES:
    "questionnaire_start": questionnaire_start,
    "questionnaire_floor": questionnaire_floor,
    "questionnaire_room": questionnaire_room,
    "questionnaire_roommates": questionnaire_roommates,
    "save_button": save_button,
    "questionnaire_goodbye": questionnaire_goodbye,
    # QUESTIONNAIRE BUTTONS
    "place1": place1,
    "place2": place2,
    "floor1": floor1,
    "floor2": floor2,
    "mountain_bot": mountain_bot,
    "mountain_top": mountain_top,
    "mountain_msg": mountain_msg,

}
ROOMS = {
    "room1": room1,
    "room2": room2,
    "room3": room3,
    "room4": room4,
    "room5": room5,
    "room6": room6,
    "river": river,
    "tree": tree,
    "igloo": igloo,
    "cave": cave,
}

PETS_AND_FRIENDS = {
    "pet_river1": pet_river1,
    "pet_river2": pet_river2,
    "pet_tree1": pet_tree1,
    "pet_tree2": pet_tree2,
    "pet_igloo1": pet_igloo1,
    "pet_igloo2": pet_igloo2,
    "pet_cave1": pet_cave1,
    "pet_cave2": pet_cave2,

    "room1_friend1": room1_friend1,
    "room1_friend2": room1_friend2,
    "room2_friend1": room2_friend1,
    "room2_friend2": room2_friend2,
    "room3_friend1": room3_friend1,
    "room3_friend2": room3_friend2,
    "room4_friend1": room4_friend1,
    "room4_friend2": room4_friend2,
    "room5_friend1": room5_friend1,
    "room5_friend2": room5_friend2,
    "room6_friend1": room6_friend1,
    "room6_friend2": room6_friend2,
}