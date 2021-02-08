# Case 1: User asks to create an account
@dp.message_handler(lambda msg: msg.text == MESSAGES['start_register'], state=States.start)
async def first_register(msg: types.Message, state: FSMContext):
    await States.email_input.set()
    await msg.reply("Будь ласка, введи свою пошту:")


@dp.message_handler(content_types=ContentType.ANY, state=States.email_input)
async def first_register(msg: types.Message, state: FSMContext):
    login_information = []
    if "%@%.%" in msg:
        login_information.append(msg)
        return await States.password_input.set()
    else:
        return await msg.reply("Я очікую твою пошту 😉")


@dp.message_handler(content_types=ContentType.ANY, state=States.email_input)
async def phone_registered(message: types.Message):
    if message.content_type is ContentType.CONTACT:
        if message.contact.user_id == message.from_user.id:  # check if own contact is sent
            user_number = str(message.contact.phone_number)
            await States.entered_number.set()
            return await message.reply(MESSAGES['satisfied'] + user_number, reply_markup=kb.GoBack)
        else:
            return await message.reply(MESSAGES['tricked'], reply_markup=kb.markup_PH_request)  # retry number input
    else:
        return await message.reply(MESSAGES['unsatisfied'], reply_markup=kb.markup_PH_request)


@dp.message_handler(content_types=ContentType.ANY, state=States.email_input)
async def first_register(msg: types.Message, state: FSMContext):
    login_information = []
    if "%@%.%" in msg:
        login_information.append(msg)
        return await States.password_input.set()
    else:
        return await msg.reply("Я очікую твою пошту 😉")


# End Of Case 1

## Case 2: User wants to log into existing account
@dp.message_handler(lambda msg: msg.text == MESSAGES['i_have_an_account'], state=States.start)
async def first_register(msg: types.Message, state: FSMContext):
    await States.email_check.set()
    await msg.reply("Будь ласка, введи свою пошту:")


## End Of Case 2

# User has account
@dp.message_handler(lambda msg: msg.text == MESSAGES['start_registered'], state=States.start)
async def login(msg: types.Message, state: FSMContext):
    # await
    await msg.reply(MESSAGES['THE JOURNAL'])
