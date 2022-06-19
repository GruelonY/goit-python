from collections import UserDict
import re
from datetime import datetime


class AddressBook(UserDict):
    def add_record(self, record):
        if isinstance(record, list):
            for value in record:
                self.data[value.name.value] = value
        else:
            self.data[record.name.value] = record
        return self.data


    def iterator(self, step=10):
        contact_list = []
        for info in self.data.values():
            contact_list.append(f'Name: {info.name.value}, Phones: {info.phones.value}, Birthday: {info.birthday.value}')
        for n in range(0, len(contact_list), step):
            yield contact_list[n:n + step]


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Phone(Field):

    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @property
    def value(self):
        return self.__value


    @value.setter
    def value(self, new_value):
        new_list = []
        if isinstance(new_value, list):
            try:
                for item in new_value:
                    new_list.append(item) if len(item) == 12 and item.isdigit() else print(f'Invalid number: {item}!!!')
                self.__value = new_list if len(new_list) != 0 else []
            except TypeError:
                print('Invalid phone format or length, phone must be only digit and 12 numbers!!!')
                self.__value = []
        elif isinstance(new_value, str):
            value_valid = len(new_value) == 12 and new_value.isdigit()
            self.__value = [new_value] if value_valid else []
            valid_message = f'Number was added successfully: {new_value}!!!'
            error_message = f'Invalid number: {new_value} for class Phone!!!'
            print(valid_message if value_valid else error_message)


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value is not None:
            try:
                get_date_numbers = re.findall(r'\d{1,4}', new_value)
                date_format = datetime(int(get_date_numbers[2]), int(get_date_numbers[1]), int(get_date_numbers[0]))
                get_age = datetime.today().year - date_format.year
                if len(get_date_numbers) != 3 or get_age > 100:
                    print('Invalid date for class Birthday!!!')
                    self.__value = None
                else:
                    self.__value = date_format.date()
                    print(f'Successfully set date')
            except IndexError as info:
                print(f"Invalid date for class Birthday!!! {info}")
                self.__value = None
            except TypeError as info:
                print(f"Invalid date for class Birthday!!! {info}")
                self.__value = None
            except ValueError as info:
                print(f"Invalid date for class Birthday!!! {info}")
                self.__value = None


class Record:
    def __init__(self, name, phones=Phone(None), birthday=Birthday(None)):
        self.name = name
        self.phones = phones
        self.birthday = birthday

    def add_phone(self, phones):
        len(phones) == 12 and phones.isdigit() and self.phones.value.append(phones)
        return f'valid number: {phones}!!!' if len(phones) == 12 and phones.isdigit() else f'Invalid number: {phones}!!!'

    def change_phone(self, old_phone, new_phone):
        if old_phone in self.phones.value:
            if len(new_phone) == 12 and new_phone.isdigit():
                self.phones.value.remove(old_phone)
                self.phones.value.append(new_phone)
                return f'Successfully changed phone for user: {self.name.value}!!'
            else:
                return f'Invalid phone: {new_phone}'
        else:
            return 'Error i dont have such phone in my AddressBook!!'

    def delete_phone(self, phone):
        is_phone_in_contacts = phone in self.phones.value
        is_phone_in_contacts and self.phones.value.remove(phone)
        valid_message = f'Successfully deleted phone for user: {self.name.value}!!'
        error_message = 'Error i dont have such phone in my AddressBook!!'
        return valid_message if is_phone_in_contacts else error_message

    def get_days_to_birthday(self):
        get_valid_year = self.birthday.value.replace(year=datetime.now().year)
        if get_valid_year.month < datetime.now().month:
            get_days = get_valid_year - datetime(datetime.now().year - 1, datetime.now().month, datetime.now().day).date()
            return f'Birthday in {get_days.days} days!!!'
        else:
            get_days = get_valid_year - datetime(datetime.now().year, datetime.now().month, datetime.now().day).date()
            return f'Birthday in {get_days.days} days!!!'


if __name__ == '__main__':
    pass