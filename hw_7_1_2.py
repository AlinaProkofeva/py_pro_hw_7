class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        '''проверка стека на пустоту. Метод возвращает True или False'''
        if len(self.stack) == 0:
            return True
        return False

    def push(self, item):
        '''добавляет новый элемент на вершину стека'''
        self.stack.append(item)
        return item

    def pop(self):
        '''удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        '''возвращает верхний элемент стека, но не удаляет его. Стек не меняется'''
        if len(self.stack) == 0:
            return None
        peek = self.stack[-1]
        return peek

    def size(self):
        '''возвращает количество элементов в стеке'''
        size = len(self.stack)
        return size

    def check_balance(self, tested_str):
        '''проверка сбалансированности скобок'''
        tested_str = list(tested_str)
        max_iter = (len(tested_str) / 2) ** 2 - len(tested_str) / 2
        counter = 0

        while counter <= max_iter and len(tested_str) > 0:
            for id, i in enumerate(tested_str):
                if (tested_str[id] == '[' and tested_str[id + 1] == ']') or (tested_str[id] == '(' and
                                 tested_str[id + 1] == ')') or (tested_str[id] == '{' and tested_str[id + 1] == '}'):
                    del (tested_str[id + 1])
                    del (tested_str[id])
                    counter += 1
                else:
                    counter += 1
                    continue

        if len(tested_str) == 0:
            return 'сбалансировано'
        elif len(tested_str) > 0:
            return 'несбалансировано'
