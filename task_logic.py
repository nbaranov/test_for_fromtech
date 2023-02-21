import datetime
import libneuro


# Вынес импорт в начало файла, остальное скопировал из примера 
if __name__ == '__main__':
    """Библиотеки нейронет"""
    nn = libneuro.NeuroNetLibrary()
    nlu = libneuro.NeuroNluLibrary()
    nv = libneuro.NeuroVoiceLibrary()
    InvalidCallStateError = libneuro.InvalidCallStateError
    check_call_state = libneuro.check_call_state

# Поднял настройки проекта выше, мне так показалось логичнее
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

def main():
    nn.call('+7' + nn.dialog['msisdn'], entry_point='main_online_container',
            on_success_call='after_call_succes',
            on_failed_call='after_call_fail',
            )
    return main_online_container()

def main_online():
       return hello_main()


#  HELLO_UNIT

@check_call_state(nv)
def hello_main_play_and_detect():
    """Функция распознавания речи"""
    nv.set_default('listen', {'no_input_timeout': 6000, 
                              'recognition_timeout': 60000, 
                              'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000
                              }
                   )
    with nv.listen(500, entities=[
        "payment_problem",
        "internet_problem",
        "tv_problem",
        "repeat",
        "robot",
        "operator",]) as response: # заменил r из примера на response для наглядного понимания
        return hello_logic(response) # убрал pass вместо него сразу return


# Функции проигрывания записанных промтов

@check_call_state(nv)
def hello_main():
    nn.log('unit', 'hello_unit')
    nv.say('hello_main_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_default():
    nn.log('unit', 'hello_main')
    nv.say('hello_default_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_null():
    if nn.counter('hello_null', '+') > 1:
        # attempt = nn.env('attempt') 
        # в примере присваевается но не используется
        return goodbye_null()
    nn.log('unit', 'hello_unit')
    nv.say('hello_null_prompt')
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


# PAYMENT_UNIT_UNIT

@check_call_state(nv)
def payment_play_and_detect():
    """Функция распознавания речи"""
    nv.set_default('listen', {'no_input_timeout': 6000, 
                              'recognition_timeout': 60000, 
                              'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000
                              }
                   )
    with nv.listen(500, entities=[
        "pay_site",
        "offices",
        "repeat",
        "promise_pay",
        "operator",
        "confirm"]) as response: # заменил r из примера на response для наглядного понимания
        return payment_logic(response) # убрал pass вместо него сразу return

# Функции проигрывания записанных промтов
# Дальше идут функции сгенерированные с помощью функции в файлике create_prompt_functions.py
@check_call_state(nv)
def payment_main():
    nn.log('unit', 'payment_unit')
    nv.say('payment_main_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_default():
    nn.log('unit', 'payment_unit')
    nv.say('payment_default_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_null():
    nn.log('unit', 'payment_unit')
    nv.say('payment_null_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_site():
    nn.log('unit', 'payment_unit')
    nv.say('payment_site_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_offices():
    nn.log('unit', 'payment_unit')
    nv.say('payment_offices_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_repeat():
    nn.log('unit', 'payment_unit')
    nv.say('payment_repeat_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_promise_pay():
    nn.log('unit', 'payment_unit')
    nv.say('payment_promise_pay_prompt')
    return payment_play_and_detect()

# //--//--//--//--//--//--//

# А тут я совсем обленился и play_and_detect тоже сгенерировал
# TV_UNIT
@check_call_state(nv)
def tv_play_and_detect():
    """Функция распознавания речи"""
    nv.set_default('listen', {'no_input_timeout': 6000, 
                              'recognition_timeout': 60000, 
                              'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000
                              }
                   )
    with nv.listen(500, entities=[
        "repeat",
        "robot",
        "confirm",
        "operator",
        ]) as response: 
        return tv_logic(response)    


@check_call_state(nv)
def tv_main():
    nn.log('unit', 'tv_unit')
    nv.say('tv_main_prompt')
    return tv_play_and_detect()


@check_call_state(nv)
def tv_default():
    nn.log('unit', 'tv_unit')
    nv.say('tv_default_prompt')
    return tv_play_and_detect()


@check_call_state(nv)
def tv_null():
    if nn.counter('tv_null', '+') > 1:
        return goodbye_null()
    nn.log('unit', 'tv_unit')
    nv.say('tv_null_prompt')
    return tv_play_and_detect()


@check_call_state(nv)
def tv_repeat():
    nn.log('unit', 'tv_unit')
    nv.say('tv_repeat_prompt')
    return tv_play_and_detect()


@check_call_state(nv)
def tv_robot():
    nn.log('unit', 'tv_unit')
    nv.say('tv_robot_prompt')
    return tv_play_and_detect()



# //--//--//--//--//--//--//


# INTERNET_UNIT

@check_call_state(nv)
def internet_play_and_detect():
    """Функция распознавания речи"""
    nv.set_default('listen', {'no_input_timeout': 6000, 
                              'recognition_timeout': 60000, 
                              'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000
                              }
                   )
    with nv.listen(500, entities=[
        "repeat",
        "robot",
        "confirm",
        "operator",
        ]) as response: 
        return internet_logic(response)    


@check_call_state(nv)
def internet_main():
    nn.log('unit', 'internet_unit')
    nv.say('internet_main_prompt')
    return internet_play_and_detect()


@check_call_state(nv)
def internet_default():
    nn.log('unit', 'internet_unit')
    nv.say('internet_default_prompt')
    return internet_play_and_detect()


@check_call_state(nv)
def internet_null():
    if nn.counter('internet_null', '+') > 1:
        return goodbye_null()
    nn.log('unit', 'internet_unit')
    nv.say('internet_null_prompt')
    return internet_play_and_detect()


@check_call_state(nv)
def internet_robot():
    nn.log('unit', 'internet_unit')
    nv.say('internet_robot_prompt')
    return internet_play_and_detect()


@check_call_state(nv)
def internet_repeat():
    nn.log('unit', 'internet_unit')
    nv.say('internet_repeat_prompt')
    return internet_play_and_detect()


# //--//--//--//--//--//--//


# INTERNET_GREEN_UNIT
@check_call_state(nv)
def internet_green_play_and_detect():
    """Функция распознавания речи"""
    nv.set_default('listen', {'no_input_timeout': 6000, 
                              'recognition_timeout': 60000, 
                              'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000
                              }
                   )
    with nv.listen(500, entities=[
        "confirm",
        "operator",
        "repeat",
        "robot",
        ]) as response: 
        return internet_green_logic(response)    


@check_call_state(nv)
def internet_green_main():
    nn.log('unit', 'internet_green_unit')
    nv.say('internet_green_main_prompt')
    return internet_green_play_and_detect()


@check_call_state(nv)
def internet_green_default():
    nn.log('unit', 'internet_green_unit')
    nv.say('internet_green_default_prompt')
    return internet_green_play_and_detect()


@check_call_state(nv)
def internet_green_null():
    if nn.counter('internet_green_null', '+') > 1:
        return goodbye_null()
    nn.log('unit', 'internet_green_unit')
    nv.say('internet_green_null_prompt')
    return internet_green_play_and_detect()


@check_call_state(nv)
def internet_green_repeat():
    nn.log('unit', 'internet_green_unit')
    nv.say('internet_green_repeat_prompt')
    return internet_green_play_and_detect()


@check_call_state(nv)
def internet_green_robot():
    nn.log('unit', 'internet_green_unit')
    nv.say('internet_green_robot_prompt')
    return internet_green_play_and_detect()


# //--//--//--//--//--//--//


# MORE_QUASTIONS_UNIT
@check_call_state(nv)
def more_question_play_and_detect():
    """Функция распознавания речи"""
    nv.set_default('listen', {'no_input_timeout': 6000, 
                              'recognition_timeout': 60000, 
                              'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000
                              }
                   )
    with nv.listen(500, entities=[
        "payment_problem",
        "internet_problem",
        "tv_problem",
        "robot",
        "no_question",
        "operator",
        "confirm",
        ]) as response: 
        return more_question_logic(response)    


@check_call_state(nv)
def more_question_main():
    nn.log('unit', 'more_question_unit')
    nv.say('more_question_main_prompt')
    return more_question_play_and_detect()


@check_call_state(nv)
def more_question_default():
    nn.log('unit', 'more_question_unit')
    nv.say('more_question_default_prompt')
    return more_question_play_and_detect()


@check_call_state(nv)
def more_question_null():
    if nn.counter('more_question_null', '+') > 1:
        return goodbye_null()
    nn.log('unit', 'more_question_unit')
    nv.say('more_question_null_prompt')
    return more_question_play_and_detect()


@check_call_state(nv)
def more_question_robot():
    nn.log('unit', 'more_question_unit')
    nv.say('more_question_robot_prompt')
    return more_question_play_and_detect()


@check_call_state(nv)
def more_question_confirm():
    nn.log('unit', 'more_question_unit')
    nv.say('more_question_confirm_prompt')
    return more_question_play_and_detect()


# //--//--//--//--//--//--//


# Ту пришлось править сгенерированное
# GOODBYE_UNIT # HANGUP_UNIT для поиска
def goodbye_main():
    nn.log('unit', 'goodbye_unit')
    nv.say('goodbye_main_prompt')
    nn.log("set_output", "set_output=помощь оказана")
    nv.hangup()
    return 


def goodbye_null():
    nn.log('unit', 'goodbye_unit')
    nv.say('goodbye_null_prompt')
    nn.log("set_output", "set_output=тишина")
    nv.hangup()
    return 


def goodbye_operator():
    nn.log('unit', 'goodbye_unit')
    nv.say('goodbye_operator_prompt')
    nn.log("set_output", "set_output=переключен на оператора")
    nv.bridge('operator@sip.ru')
    return 


def goodbye_operator_demand():
    nn.log('unit', 'goodbye_operator_unit')
    nv.say('goodbye_operator_demand_prompt')
    nn.log("set_output", "set_output=переключен на оператора")
    nv.bridge('technikal_specialist@sip.ru')
    return 


def goodbye_internet_green():
    nn.log('unit', 'goodbye_internet_unit')
    nv.say('goodbye_internet_green_prompt')
    nn.log("set_output", "set_output=всё работает потом перезвонит")
    nv.hangup()
    return 


# //--//--//--//--//--//--//

# не вникал зачем эти заглушки, но скопировал, чтобы было
def after_call_succes():
    pass


def after_call_fail():
    pass
# //--//--//--//--//--//--//


# Тут наверное тоже можно было бы сделать генератор, 
# но лень было думать быстрее было набросать вручную 
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

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return hello_robot()
        
    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("payment_problem"):
        if r.entity("payment_problem") == 'true':
            nn.log("condition", "payment_problem=True")
            return payment_main()

    if r.has_entity("internet_problem"):
        if r.entity("internet_problem") == 'true':
            nn.log("condition", "internet_problem=True")
            return internet_main()

    if r.has_entity("tv_problem"):
        if r.entity("tv_problem") == 'true':
            nn.log("condition", "tv_problem=True")
            return tv_main()

# //--//--//--//--//--//--//

# ЛОГИКА условий для PAYMENT_UNIT 
@check_call_state(nv)
def payment_logic(r):
    nn.log('unit', 'payment_unit')
    payment_unit_exec_count = nn.env('payment_unit_exec_count')
    if not payment_unit_exec_count:
        nn.env('payment_unit_exec_count', 1)
    else:
        payment_unit_exec_count = payment_unit_exec_count + 1
        nn.env('payment_unit_exec_count', payment_unit_exec_count)
        if payment_unit_exec_count and payment_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return payment_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return payment_default()

    if r.has_entity("pay_site"):
        if r.entity("pay_site") == 'true':
            nn.log("condition", "pay_site=True")
            return payment_site()

    if r.has_entity("offices"):
        if r.entity("offices") == 'true':
            nn.log("condition", "offices=True")
            return payment_offices()

    if r.has_entity("promise_pay"):
        if r.entity("promise_pay") == 'true':
            nn.log("condition", "promise_pay=True")
            return payment_promise_pay()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return goodbye_main()
        if r.entity("confirm") == 'false':
            nn.log("condition", "confirm=False")
            return more_question_main()

# //--//--//--//--//--//--//


# ЛОГИКА условий для TV_UNIT
@check_call_state(nv)
def tv_logic(r):
    nn.log('unit', 'tv_unit')
    tv_unit_exec_count = nn.env('tv_unit_exec_count')
    if not tv_unit_exec_count:
        nn.env('tv_unit_exec_count', 1)
    else:
        tv_unit_exec_count = tv_unit_exec_count + 1
        nn.env('tv_unit_exec_count', tv_unit_exec_count)
        if tv_unit_exec_count and tv_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return tv_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return tv_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return tv_repeat()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return tv_robot()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return goodbye_main()
        if r.entity("confirm") == 'false':
            nn.log("condition", "confirm=False")
            return more_question_main()

# //--//--//--//--//--//--//


# ЛОГИКА условий для INTERNET_UNIT
@check_call_state(nv)
def internet_logic(r):
    nn.log('unit', 'internet_unit')
    internet_unit_exec_count = nn.env('internet_unit_exec_count')
    if not internet_unit_exec_count:
        nn.env('internet_unit_exec_count', 1)
    else:
        internet_unit_exec_count = internet_unit_exec_count + 1
        nn.env('internet_unit_exec_count', internet_unit_exec_count)
        if internet_unit_exec_count and internet_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return internet_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return internet_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return internet_repeat()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return internet_robot()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return goodbye_main()
        if r.entity("confirm") == 'false':
            nn.log("condition", "confirm=False")
            return more_question_main()

# //--//--//--//--//--//--//


# ЛОГИКА условий для INTERNET_GREEN_UNIT
@check_call_state(nv)
def internet_green_logic(r):
    nn.log('unit', 'internet_green_unit')
    internet_green_unit_exec_count = nn.env('internet_green_unit_exec_count')
    if not internet_green_unit_exec_count:
        nn.env('internet_green_unit_exec_count', 1)
    else:
        internet_green_unit_exec_count = internet_green_unit_exec_count + 1
        nn.env('internet_green_unit_exec_count', internet_green_unit_exec_count)
        if internet_green_unit_exec_count and internet_green_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return internet_green_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return internet_green_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return internet_green_repeat()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return internet_green_robot()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return goodbye_main()
        if r.entity("confirm") == 'false':
            nn.log("condition", "confirm=False")
            return more_question_main()

# //--//--//--//--//--//--//

# ЛОГИКА условий для MORE_QUESTIONS_UNIT
@check_call_state(nv)
def more_question_logic(r):
    nn.log('unit', 'more_question_unit')
    more_question_unit_exec_count = nn.env('more_question_unit_exec_count')
    if not more_question_unit_exec_count:
        nn.env('more_question_unit_exec_count', 1)
    else:
        more_question_unit_exec_count = more_question_unit_exec_count + 1
        nn.env('more_question_unit_exec_count', more_question_unit_exec_count)
        if more_question_unit_exec_count and more_question_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return more_question_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return more_question_default()

    if r.has_entity("payment_problem"):
        if r.entity("payment_problem") == 'true':
            nn.log("condition", "payment_problem=True")
            return payment_main()
    
    if r.has_entity("internet_problem"):
        if r.entity("internet_problem") == 'true':
            nn.log("condition", "internet_problem=True")
            return internet_main()

    if r.has_entity("tv_problem"):
        if r.entity("tv_problem") == 'true':
            nn.log("condition", "tv_problem=True")
            return tv_main()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return more_question_robot()

    if r.has_entity("no_question"):
        if r.entity("no_question") == 'true':
            nn.log("condition", "no_question=True")
            return goodbye_main()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()
        
    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return more_question_confirm()

# //--//--//--//--//--//--//

