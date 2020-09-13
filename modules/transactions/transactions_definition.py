from modules.transactions.transactions_schema import TRANSACTION_SCHEMA


TRANSACTION_DEFINITION = {
    'item_title': 'transaction',
    'schema': TRANSACTION_SCHEMA,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'PATCH', 'DELETE'],
}