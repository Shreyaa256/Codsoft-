import sys

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\n--- Add New Contact ---")
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email Address: ").strip()
        address = input("Enter Address: ").strip()

        if not name or not phone:
            print("Name and Phone Number are required fields.")
            return

        # Check if contact with same name and phone exists
        for contact in self.contacts:
            if contact['name'].lower() == name.lower() and contact['phone'] == phone:
                print("A contact with this name and phone number already exists.")
                return

        self.contacts.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        print("Contact added successfully.")

    def view_contacts(self):
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts to display.")
            return

        print(f"{'Name':<25} {'Phone Number':<15}")
        print("-" * 40)
        for contact in self.contacts:
            print(f"{contact['name']:<25} {contact['phone']:<15}")

    def search_contacts(self):
        print("\n--- Search Contacts ---")
        query = input("Enter name or phone number to search: ").strip().lower()
        if not query:
            print("Search query cannot be empty.")
            return

        results = [c for c in self.contacts if query in c['name'].lower() or query in c['phone']]
        if not results:
            print("No matching contacts found.")
            return

        print(f"\n{'Name':<25} {'Phone Number':<15} {'Email':<25} {'Address':<30}")
        print("-" * 95)
        for contact in results:
            print(f"{contact['name']:<25} {contact['phone']:<15} {contact['email']:<25} {contact['address']:<30}")

    def update_contact(self):
        print("\n--- Update Contact ---")
        self.view_contacts()
        if not self.contacts:
            return

        name = input("Enter the exact name of the contact you want to update: ").strip()
        phone = input("Enter the phone number of the contact to update: ").strip()
        for contact in self.contacts:
            if contact['name'].lower() == name.lower() and contact['phone'] == phone:
                print(f"\nUpdating contact: {contact['name']} - {contact['phone']}")
                new_name = input(f"Enter new name [{contact['name']}]: ").strip()
                new_phone = input(f"Enter new phone [{contact['phone']}]: ").strip()
                new_email = input(f"Enter new email [{contact['email']}]: ").strip()
                new_address = input(f"Enter new address [{contact['address']}]: ").strip()

                if new_name:
                    contact['name'] = new_name
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                if new_address:
                    contact['address'] = new_address

                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self):
        print("\n--- Delete Contact ---")
        self.view_contacts()
        if not self.contacts:
            return

        name = input("Enter the exact name of the contact you want to delete: ").strip()
        phone = input("Enter the phone number of the contact to delete: ").strip()
        for i, contact in enumerate(self.contacts):
            if contact['name'].lower() == name.lower() and contact['phone'] == phone:
                confirm = input(f"Are you sure you want to delete contact {contact['name']}? (y/n): ").strip().lower()
                if confirm == 'y':
                    del self.contacts[i]
                    print("Contact deleted successfully.")
                else:
                    print("Deletion canceled.")
                return
        print("Contact not found.")

    def run(self):
        while True:
            print("\n====== Contact Book Menu ======")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Select an option (1-6): ").strip()

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contacts()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Book. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
