FIXTURES_FILLING = [
    ('testerr', 'testerr'),
    ('test_2', 'test_2'),
]

FIXTURES_SIZE = [
    (['11', '2', 'ddd'], 3),
    ('1', 1)
]

FIXTURES_BALANCE = [
    ('(((([{}]))))', 'сбалансировано'),
    ('[([])((([[[]]])))]{()}', 'сбалансировано'),
    ('{{[()]}}', 'сбалансировано'),
    ('}{}', 'несбалансировано'),
    ('{{[(])]}}', 'несбалансировано'),
    ('[[{())}]', 'несбалансировано')
]


