contacts = []

def create_contact(name, email):
    contacts.append({'name': name, 'email': email})

def read_contact(index=None):
    if index is not None:
        return contacts[index]
    else:
        return contacts

def update_contact(index, name=None, email=None):
    contact = contacts[index]
    if name is not None:
        contact['name'] = name
    if email is not None:
        contact['email'] = email

def delete_contact(index):
    del contacts[index]

    # create a new contact
create_contact('Iswarya', 'iswarya@example.com')

# read all contacts
all_contacts = read_contact()
print(all_contacts)

# read a specific contact
contact = read_contact(0)
print(contact)

# update a contact
update_contact(0, name='Iswarya Shakthi')
updated_contact = read_contact(0)
print(updated_contact)

# delete a contact
delete_contact(0)
all_contacts = read_contact()
print(all_contacts)