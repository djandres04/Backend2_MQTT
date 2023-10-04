import utils.implementingData as implementingData
from utils.script import scriptType

def topic_process(topic_in,value):
    topicos = {
        "sub/light/1":"light",
        "sub/light/2":"light",
        "sub/light/3":"light",
        "sub/door/1":"door",
        "sub/buzzer/1":"buzzer",
        "sub/tempe":"tempe"
    }

    ids = {
        "sub/light/1":"1",
        "sub/light/2":"2",
        "sub/light/3":"3",
        "sub/door/1":"1",
        "sub/buzzer/1":"1"
    }
    value_temp = value.strip("b").strip("'")
    temp,value_out = scriptType.validate(value_temp)

    topicOut = topicos[topic_in]
    id = ids[topic_in]

    if temp:
        if topicOut == "tempe":     implementingData.data_tempe(topicOut, value_out)
        if topicOut == "buzzer":    implementingData.data_buzzer(id, topicOut, value_out)
        else:                       implementingData.data_status(id, topicOut, value_out)
    else:
        print("Invalid value or status")