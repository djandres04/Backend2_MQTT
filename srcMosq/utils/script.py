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

            'False': 'False',
            'false': 'False',
            'falso': 'False',
            'Falso': 'False',
            '0': 'False'

        }
        try:
            temp = scripting[message]
            return True, temp
        except Exception as ex:
            return False, None