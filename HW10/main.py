from collections import UserDict


class Record:
    def __init__(self, name, phones=''):
        self.name = name
        self.phones = list(phones)
        self.data = AddressBook()

    def add_phone(self, name, phones):
        self.phones.append(phones)
        self.data[self.name] = name
        self.data['phones'] = self.phones
        return f'Successfully added phone for user: {self.name}!!\n{self.data}'

    def change_phone(self, old_phone, new_phone):
        self.phones.remove(old_phone)
        self.phones.append(new_phone)
        self.data.pop('phones')
        self.data['phones'] = self.phones
        return f'Successfully changed phone for user: {self.name}!!\n{self.data}'

    def delete_phone(self, phone):
        self.phones.remove(phone)
        return f'Successfully deleted phone for user: {self.name}!!\n{self.data}'


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Field:
    pass


class Name:
    pass


class Phone:
    pass


if __name__ == '__main__':
    Bill = Record('Mark')
    print(Mark.add_phone('Mark', 123))
    print(Mark.add_phone('Mark', 521))
    print(Mark.change_phone(521, 1234))
    Mike = Record('Mike')
    print(Mike.add_phone('Mike', 102))
    print(Mike.change_phone(102, 1012))
    print(Mike.delete_phone(1012))
    print(Mark.name)
    print(Mark.phones)
    print(Mark.data)