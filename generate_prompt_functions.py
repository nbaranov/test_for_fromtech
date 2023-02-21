def genegare_prompt_function(prompt_full_name):
    word_list = input_string.split("_")
    prompt_name = "_".join(word_list[:-2])
    name_and_action = "_".join(word_list[:-1])
    
    if '_null_' in prompt_full_name:
        null_condition = f"""\n    if nn.counter('{name_and_action}', '+') > 1:
        return hangup_null()"""
    else: 
        null_condition = ""
    
    output_string = f"""
@check_call_state(nv)
def {name_and_action}():{null_condition}
    nn.log('unit', '{prompt_name}_unit')
    nv.say('{prompt_full_name}')
    return {prompt_name}_play_and_detect()
"""
    print(output_string)


def generate_play_and_say_function(unit_full_name):
    unit_name = unit_full_name[:-5]
    
    output_string =f"""
@check_call_state(nv)
def {unit_name}_play_and_detect():
    \"\"\"Функция распознавания речи\"\"\"
    nv.set_default('listen', {{'no_input_timeout': 6000, 
                              'recognition_timeout': 60000, 
                              'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000
                              }}
                   )
    with nv.listen(500, entities=[
        # TODO Вставить Сущности Юнита
        ]) as response: 
        return {unit_name}_logic(response)    
"""
    print(output_string)
    

if __name__ == "__main__":
    print('input prompt name or "exit": ')

    while True:
        input_string = input().strip()
        if input_string == "":
            continue
        elif input_string == "exit":
            exit()
        elif "_prompt" in input_string:
            genegare_prompt_function(input_string)
        elif "_unit" in input_string:
            generate_play_and_say_function(input_string)
    
    

