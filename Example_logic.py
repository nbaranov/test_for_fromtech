import datetime


if __name__ == '__main__':
    """Библиотеки нейронет"""
    import libneuro
    nn = libneuro.NeuroNetLibrary()
    nlu = libneuro.NeuroNluLibrary()
    nv = libneuro.NeuroVoiceLibrary()
    InvalidCallStateError = libneuro.InvalidCallStateError
    check_call_state = libneuro.check_call_state


def main():
    nn.call('+7' + nn.dialog['msisdn'], entry_point='main_online_container',
            on_success_call='after_call_succes',
            on_failed_call='after_call_fail',
            )
    return main_online_container()


def main_online_container():
    """Настройки проекта"""
    try:
        nn.env('bot_duration', 0)
        nn.env('msisdn', nn.dialog['msisdn'])
        nn.env('start_time', str(datetime.datetime.now()))
        nn.env('success_call', 0)
        nn.env('result', 'incomplete')
        now = datetime.datetime.now()
        main_online()
    except InvalidCallStateError:
        nn.log("Звонок завершен, пропускается выполнение функций")
        nn.env('bot_duration', 0)


def main_online():
       return hello_main()


#  HELLO_UNIT

@check_call_state(nv)
def hello_main_play_and_detect():
    """Функция распознавания речи"""
    nv.set_default('listen', {'no_input_timeout': 6000, 
                              'recognition_timeout': 60000, 
                              'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000}
                   )
    with nv.listen(500, entities=[
        "who_is_it",
        "what_do",
        "not_sure",
        "not_boss",
        "repeat",
        "dont_disturb",
        "confirm",
        "robot"
    ]) as r:
        pass
    return hello_logic(r)


@check_call_state(nv)
def hello_main():
    """Функции проигрывания записанных промтов"""
    nn.log('unit', 'hello_unit')
    nv.say('hello_main_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_null():
    if nn.counter('hello_null', '+') > 1:
        attempt = nn.env('attempt')
        return hangup_null()
    nn.log('unit', 'hello_unit')
    nv.say('hello_null_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_default():
    nn.log('unit', 'hello_main')
    nv.say('hello_default_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_who_are_we():
    nn.log('unit', 'hello_main')
    nv.say('hello_who_are_we_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_what_do():
    nn.log('unit', 'hello_main')
    nv.say('hello_what_do_prompt')
    return hello_main_play_and_detect()

@check_call_state(nv)
def hello_repeat():
    nn.log('unit', 'hello_main')
    nv.say('hello_repeat_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_robot():
    nn.log('unit', 'hello_main')
    nv.say('hello_robot_prompt')
    return hello_main_play_and_detect()

# //--//--//--//--//--//--//


# WORK_TYPE_UNIT

@check_call_state(nv)
def work_type_play_and_detect():
    nv.set_default('listen', {'no_input_timeout': 6000, 'recognition_timeout': 60000, 'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000})
    with nv.listen(500, entities=[
        "facade",
        "roof",
        "not_sure",
        "both",
        "repeat",
        "robot"
    ]) as r:
        pass
    return work_type_logic(r)


@check_call_state(nv)
def work_type_main():
    nn.log('unit', 'work_type_main')
    nv.say('work_type_main_prompt')
    return work_type_play_and_detect()


@check_call_state(nv)
def work_type_null():
    if nn.counter('work_type_null', '+') > 1:
        attempt = nn.env('attempt')
        return hangup_null()
    nn.log('unit', 'work_type_unit')
    nv.say('work_type_null_prompt')
    return work_type_play_and_detect()


@check_call_state(nv)
def work_type_default():
    nn.log('unit', 'work_type_unit')
    nv.say('work_type_default_prompt')
    return work_type_play_and_detect()


@check_call_state(nv)
def work_type_repeat():
    nn.log('unit', 'work_type_unit')
    nv.say('work_type_repeat_prompt')
    return work_type_play_and_detect()


@check_call_state(nv)
def work_type_robot():
    nn.log('unit', 'work_type_unit')
    nv.say('work_type_robot_prompt')
    return work_type_play_and_detect()


# //--//--//--//--//--//--//

# CAN_CALLBACK
@check_call_state(nv)
def can_callback_play_and_detect():
    nv.set_default('listen', {'no_input_timeout': 6000, 'recognition_timeout': 60000, 'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000})
    with nv.listen(500, entities=[
        "repeat",
        "callback",
        "confirm",
        "robot"
    ]) as r:
        pass
    return can_callback_logic(r)


@check_call_state(nv)
def can_callback_main():
    nn.log('unit', 'can_callback_main')
    nv.say('can_callback_main_prompt')
    return can_callback_play_and_detect()


@check_call_state(nv)
def can_callback_null():
    if nn.counter('can_callback_null', '+') > 1:
        attempt = nn.env('attempt')
        return hangup_null()
    nn.log('unit', 'can_callback_main')
    nv.say('can_callback_null')
    return can_callback_play_and_detect()


@check_call_state(nv)
def can_callback_default():
    nn.log('unit', 'can_callback_main')
    nv.say('can_callback_default_prompt')
    return can_callback_play_and_detect()


@check_call_state(nv)
def can_callback_repeat():
    nn.log('unit', 'can_callback_main')
    nv.say('can_callback_repeat_prompt')
    return can_callback_play_and_detect()


@check_call_state(nv)
def can_callback_robot():
    nn.log('unit', 'can_callback_main')
    nv.say('can_callback_robot_prompt')
    return can_callback_play_and_detect()

# //--//--//--//--//--//--//

# HANGUP_UNIT

def hangup_dont_disturb():
    nn.log('unit', 'hangup_main')
    nv.say('hangup_dont_disturb')
    nn.log("set_output", "set_output=не беспокоить")
    nv.hangup()
    return


def hangup_callback():
    nn.log('unit', 'hangup_main')
    nv.say('hangup_callback_prompt')
    nn.log("set_output", "set_output=надо перезвонить")
    nv.hangup()
    return


def hangup_goodbye():
    nn.log('unit', 'hangup_main')
    nv.say('hangup_goodbye_prompt')
    nn.log("set_output", "set_output=надо перезвонить")
    nv.hangup()
    return


def hangup_null():
    nn.log('unit', 'hangup_main')
    nv.say('hangup_null_prompt')
    nn.log("set_output", "set_output=тишина")
    nv.hangup()
    return


def hangup_not_callback():
    nn.log('unit', 'hangup_main')
    nv.say('hangup_not_callback_prompt')
    nn.log("set_output", "set_output=не перезванивать")
    nv.hangup()
    return

# //--//--//--//--//--//--//

def after_call_succes():
    pass


def after_call_fail():
    pass

# ЛОГИКА условий для HELLO_UNIT
@check_call_state(nv)
def hello_logic(r):
    """Функция проверки сущностей """
    nn.log('unit', 'hello_unit')
    hello_unit_exec_count = nn.env('hello_unit_exec_count')
    if not hello_unit_exec_count:
        nn.env('hello_unit_exec_count', 1)
    else:
        hello_unit_exec_count = hello_unit_exec_count + 1
        nn.env('hello_unit_exec_count', hello_unit_exec_count)
        if hello_unit_exec_count and hello_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return hello_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return hello_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return hello_repeat()

    if r.has_entity("who_is_it"):
        if r.entity("who_is_it") == 'true':
            nn.log("condition", "who_is_it=True")
            return hello_who_are_we()

    if r.has_entity("what_do"):
        if r.entity("what_do") == 'true':
            nn.log("condition", "what_do=True")
            return hello_what_do()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return hello_robot()

    if r.has_entity("not_sure"):
        if r.entity("not_sure") == 'true':
            nn.log("condition", "not_sure=True")
            return can_callback_main()

    if r.has_entity("dont_disturb"):
        if r.entity("dont_disturb") == 'true':
            nn.log("condition", "dont_disturb=True")
            return hangup_dont_disturb()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return work_type_main()
        if r.entity("confirm") == 'false':
            nn.log("condition", "confirm=False")
            return hangup_goodbye()

    if r.has_entity("not_boss"):
        if r.entity("not_boss") == 'true':
            nn.log("condition", "confirm=True")
            return can_callback_main()
    return hello_default()


# //--//--//--//--//--//--//

# ЛОГИКА условий для WORK_TYPE_UNIT
@check_call_state(nv)
def work_type_logic(r):
    nn.log('unit', 'work_type_unit')
    work_type_unit_exec_count = nn.env('work_type_unit_exec_count')
    if not work_type_unit_exec_count:
        nn.env('work_type_unit_exec_count', 1)
    else:
        work_type_unit_exec_count = work_type_unit_exec_count + 1
        nn.env('work_type_unit_exec_count', work_type_unit_exec_count)
        if work_type_unit_exec_count and work_type_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return work_type_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return work_type_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return work_type_repeat()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return hello_robot()

    if r.has_entity("facade"):
        if r.entity("facade") == 'true':
            nn.log("condition", "facade=True")
            return hangup_callback()

    if r.has_entity("roof"):
        if r.entity("roof") == 'true':
            nn.log("condition", "roof=True")
            return hangup_callback()

    if r.has_entity("both"):
        if r.entity("both") == 'true':
            nn.log("condition", "both=True")
            return hangup_callback()

    if r.has_entity("not_sure"):
        if r.entity("not_sure") == 'true':
            nn.log("condition", "not_sure=True")
            return can_callback_main()
    return work_type_default()

# //--//--//--//--//--//--//

# ЛОГИКА условий для CAN_CALLBACK

@check_call_state(nv)
def can_callback_logic(r):
    nn.log('unit', 'work_type_unit')
    can_callback_unit_exec_count = nn.env('can_callback_unit_exec_count')
    if not can_callback_unit_exec_count:
        nn.env('can_callback_unit_exec_count', 1)
    else:
        can_callback_unit_exec_count = can_callback_unit_exec_count + 1
        nn.env('can_callback_unit_exec_count', can_callback_unit_exec_count)
        if can_callback_unit_exec_count and can_callback_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return can_callback_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return can_callback_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return can_callback_repeat()

    if r.has_entity("callback"):
        if r.entity("callback") == 'true':
            nn.log("condition", "callback=True")
            return hangup_callback()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return hangup_callback()

        elif r.entity("conform") == 'false':
            nn.log("condition", "confirm=False")
            return hangup_not_callback()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return can_callback_robot()
    return can_callback_default()

# //--//--//--//--//--//--//