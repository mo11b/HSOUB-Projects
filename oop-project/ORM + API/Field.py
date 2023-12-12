from abc import ABC

class Field(ABC):
    field_type = None

    def __init__(self, unique = None, max_length = 255):
        if unique is True:
            self.unique = "UNIQUE"
        else:
            self.unique = ''
        if max_length:
            self.max_lenght = max_length

    def __repr__(self):
        columns = []
        if self.field_type == 'VARCHAR':
            columns.append(f'VARCHAR({self.max_length})')
        else:
            columns.append(self.field_type)
            columns.append(self.unique)

        return "".join(columns).strip()
    
class CharField(Field):
    field_type = 'VARCHAR'

    def __init__(self, max_length=225, unique=None):
        self.max_length = max_length
        self.unique = unique
        super().__init__(max_length=max_length, unique=unique)


class TextField(Field):
    field_type = 'TEXT'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class IntegerField(Field):
    field_type = 'INTEGER'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class FloatField(Field):
    field_type = 'REAL'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class BooleanField(Field):
    field_type = 'INTEGER'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class DateTimeField(Field):
    field_type = 'TIMESTAMP'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)



    
