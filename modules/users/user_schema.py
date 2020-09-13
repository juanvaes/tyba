from core.utilities.string_utils import lower_string

USER_SCHEMA = {
    'first_name': {
        'type': 'string',
        'required': True
    },
    'last_name': {
        'type': 'string',
        'required': True
    },
    'email': {
        'type': 'string',
        'unique': True,
        'required': True,
        'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        'coerce': lower_string,
    },
    'password': {
        'type': 'string',
        'empty': False,
        'required': True
    }
}
