from typing import Tuple, Any


class scriptType:

    def validate(message) -> tuple[bool, Any] | tuple[bool, None]:
        scripting = {
            'True': 'True',
            'true': 'True',
            'Verdadero': 'True',
            'verdadero': 'True',
            'Verdad': 'True',
            'verdad': 'True',
            '1': 'True',
            'on':'True',
            'ON':'True',

            'False': 'False',
            'false': 'False',
            'falso': 'False',
            'Falso': 'False',
            '0': 'False',
            'off':'False',
            '0FF':'False',

            "True": "True",
            "true": "True",
            "Verdadero": "True",
            "verdadero": "True",
            "Verdad": "True",
            "verdad": "True",
            "1": "True",

            "False": "False",
            "false": "False",
            "falso": "False",
            "Falso": "False",
            "0": "False"
            }
        try:
            mensaje_temp = scripting[message]
            return True, mensaje_temp
        except Exception as ex:
            return False, None
