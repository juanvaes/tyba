from modules.users.user_schema import USER_SCHEMA


USER_DEFINITION = {
    'item_title': 'user',
    'schema': USER_SCHEMA,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'PATCH', 'DELETE'],
}