from aiogram.dispatcher.filters.state import State, StatesGroup


class NewBot(StatesGroup):
    here_token = State()
    here_username = State()
    here_name = State()
    here_template = State()
    here_start_text = State()
    here_name_text = State()
    here_group_text = State()
    here_apply_text = State()
    here_apply_yes_text = State()
    here_apply_no_text = State()
    here_final_text = State()
