from faker import Faker
fake = Faker()

class BaseContact:

    def __init__(self, fname, lname, phone, email):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email

    def contact(self):
        return "Wybieram numer " + self.phone + " i dzwonie do "+self.fname +" "+self.lname

    @property
    def letters(self):
        return len(self.fname.replace(" ", "")+self.lname)


class BusinesContact(BaseContact):
    def __init__(self, fname, lname, phone, email, position, company, busines_phone):
        super().__init__(fname, lname, phone, email)
        self.position = position
        self.company = company
        self.busines_phone = busines_phone

    def busines_contact(self):
        return "Wybieram numer " + self.busines_phone + " i dzwonie do "+self.fname+" "+self.lname

    @property
    def letters(self):
            return len(self.fname.replace(" ", "") + self.lname)


def create_contacts(card_amount):
    names = []
    for i in range(0, card_amount):
        names.append(fake.last_name())
    return names

person1 = BusinesContact(fake.name(),fake.last_name(),"adam","nowak","manager", "mdmdm@yt","78787878",)
print(person1.busines_contact())

name_lenght = person1.letters
print(name_lenght)


create = create_contacts(8)
print(create)





