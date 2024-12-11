import os
import sys
from datetime import datetime

from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def main_menu(self):
        os.system('cls')
        choice = self.show_main_menu()
        if choice == '1':
            self.owner_menu()
        elif choice == '2':
            self.rent_menu()
        elif choice == '3':
            self.sports_facility_menu()
        elif choice == '4':
            self.tenant_menu()
        elif choice == '5':
            self.interesting_requests_menu()
        elif choice == '0':
            os.system('cls')

    def show_main_menu(self):
        self.view.show_message("\nTables:\n")
        self.view.show_message("1. Owner")
        self.view.show_message("2. Rent")
        self.view.show_message("3. Sports_facility")
        self.view.show_message("4. Tenant")
        self.view.show_message("5. Interesting requests")
        self.view.show_message("0. Quit")
        return self.view.get_value_input("Enter your choice: ")

# table 'owner':

    def owner_menu(self):
        os.system('cls')
        choice = self.show_owner_menu()
        if choice == '1':
            os.system('cls')
            self.add_owner()
        elif choice == '2':
            os.system('cls')
            self.view_owner()
        elif choice == '3':
            os.system('cls')
            self.update_owner()
        elif choice == '4':
            os.system('cls')
            self.delete_owner()
        elif choice == '5':
            os.system('cls')
            self.random_generate_owner()
        elif choice == '0':
            os.system('cls')
            self.main_menu()

    def show_owner_menu(self):
        self.view.show_message("\nOwner:\n")
        self.view.show_message("1. Add row")
        self.view.show_message("2. Show all rows")
        self.view.show_message("3. Update row")
        self.view.show_message("4. Delete row")
        self.view.show_message("5. Generate random rows")
        self.view.show_message("0. Quit")
        return self.view.get_value_input("Enter your choice: ")

    def add_owner(self):
        email = self.view.get_owner_email()
        phone_number, name = self.view.get_owner_input()
        if len(email) > 20:
            sys.exit("Error: Owner: email is long")
        if len(phone_number) > 15:
            sys.exit("Error: Owner: phone_number is long")
        if len(name) > 20:
            sys.exit("Error: Owner: name is long")
        if bool(self.model.owner_row_search(email)):
            sys.exit("Error: Owner: this primary key already exists")
        self.model.owner_add(email, phone_number, name)
        self.view.show_message("Owner: added successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.owner_menu()

    def view_owner(self):
        owners = self.model.owner_get_all_rows()
        self.view.owner_show_all_rows(owners)
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.owner_menu()

    def update_owner(self):
        old_email = self.view.get_owner_old_email()
        email = self.view.get_owner_email()
        phone_number, name = self.view.get_owner_input()
        if len(old_email) > 20:
            sys.exit("Error: Owner: old_email is long")
        if len(email) > 20:
            sys.exit("Error: Owner: email is long")
        if len(phone_number) > 15:
            sys.exit("Error: Owner: phone_number is long")
        if len(name) > 20:
            sys.exit("Error: Owner: name is long")
        if not bool(self.model.owner_row_search(old_email)):
            sys.exit("Error: Owner: old_primary key is not exist")
        if bool(self.model.owner_row_search(email)):
            sys.exit("Error: Owner: this primary key already exists")
        self.model.owner_update(old_email, email, phone_number, name)
        self.view.show_message("Owner: updated successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.owner_menu()

    def delete_owner(self):
        email = self.view.get_owner_email()
        if len(email) > 20:
            sys.exit("Error: Owner: email is long")
        if not bool(self.model.owner_row_search(email)):
            sys.exit("Error: Owner: email is not exist")
        self.model.owner_delete(email)
        self.view.show_message("Owner: delted successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.owner_menu()

    def random_generate_owner(self):
        row_count = self.view.get_row_count_input()
        if not self.is_positive_int(row_count):
            sys.exit("Error: Owner: row_count is not positive integer number")
        if int(row_count) > 200000:
            sys.exit("Error: Owner: row_count is to many")
        self.model.owner_random_generate(row_count)
        self.view.show_message("Owner: generated successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.owner_menu()

# table 'tenant':

    def tenant_menu(self):
        os.system('cls')
        choice = self.show_tenant_menu()
        if choice == '1':
            os.system('cls')
            self.add_tenant()
        elif choice == '2':
            os.system('cls')
            self.view_tenant()
        elif choice == '3':
            os.system('cls')
            self.update_tenant()
        elif choice == '4':
            os.system('cls')
            self.delete_tenant()
        elif choice == '5':
            os.system('cls')
            self.random_generate_tenant()
        elif choice == '0':
            os.system('cls')
            self.main_menu()

    def show_tenant_menu(self):
        self.view.show_message("\nTenant:\n")
        self.view.show_message("1. Add row")
        self.view.show_message("2. Show all rows")
        self.view.show_message("3. Update row")
        self.view.show_message("4. Delete row")
        self.view.show_message("5. Generate random rows")
        self.view.show_message("0. Quit")
        return self.view.get_value_input("Enter your choice: ")

    def add_tenant(self):
        email = self.view.get_tenant_email()
        phone_number, name = self.view.get_tenant_input()
        if len(email) > 20:
            sys.exit("Error: Tenant: email is long")
        if len(phone_number) > 15:
            sys.exit("Error: Tenant: phone_number is long")
        if len(name) > 20:
            sys.exit("Error: Tenant: name is long")
        if bool(self.model.tenant_row_search(email)):
            sys.exit("Error: Tenant: this primary key already exists")
        self.model.tenant_add(email, phone_number, name)
        self.view.show_message("Tenant: added successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.tenant_menu()

    def view_tenant(self):
        tenants = self.model.tenant_get_all_rows()
        self.view.tenant_show_all_rows(tenants)
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.tenant_menu()

    def update_tenant(self):
        old_email = self.view.get_tenant_old_email()
        email = self.view.get_tenant_email()
        phone_number, name = self.view.get_tenant_input()
        if len(old_email) > 20:
            sys.exit("Error: Tenant: old_email is long")
        if len(email) > 20:
            sys.exit("Error: Tenant: email is long")
        if len(phone_number) > 15:
            sys.exit("Error: Tenant: phone_number is long")
        if len(name) > 20:
            sys.exit("Error: Tenant: name is long")
        if not bool(self.model.tenant_row_search(old_email)):
            sys.exit("Error: Tenant: old_primary key is not exist")
        if bool(self.model.tenant_row_search(email)):
            sys.exit("Error: Tenant: new_primary key already exists")
        self.model.tenant_update(old_email, email, phone_number, name)
        self.view.show_message("Tenant: updated successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.tenant_menu()

    def delete_tenant(self):
        email = self.view.get_tenant_email()
        if len(email) > 20:
            sys.exit("Error: Tenant: email is long")
        if not bool(self.model.tenant_row_search(email)):
            sys.exit("Error: Tenant: email is not exist")
        self.model.tenant_delete(email)
        self.view.show_message("Tenant: delted successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.tenant_menu()

    def random_generate_tenant(self):
        row_count = self.view.get_row_count_input()
        if not self.is_positive_int(row_count):
            sys.exit("Error: Tenant: row_count is not positive integer number")
        if int(row_count) > 200000:
            sys.exit("Error: Tenant: row_count is to many")
        self.model.tenant_random_generate(row_count)
        self.view.show_message("Tenant: generated successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.tenant_menu()

# table 'sports_facility':

    def sports_facility_menu(self):
        os.system('cls')
        choice = self.show_sports_facility_menu()
        if choice == '1':
            os.system('cls')
            self.add_sports_facility()
        elif choice == '2':
            os.system('cls')
            self.view_sports_facility()
        elif choice == '3':
            os.system('cls')
            self.update_sports_facility()
        elif choice == '4':
            os.system('cls')
            self.delete_sports_facility()
        elif choice == '5':
            os.system('cls')
            self.random_generate_sports_facility()
        elif choice == '0':
            os.system('cls')
            self.main_menu()


    def show_sports_facility_menu(self):
        self.view.show_message("\nSports_facility:\n")
        self.view.show_message("1. Add row")
        self.view.show_message("2. Show all rows")
        self.view.show_message("3. Update row")
        self.view.show_message("4. Delete row")
        self.view.show_message("5. Generate random rows")
        self.view.show_message("0. Quit")
        return self.view.get_value_input("Enter your choice: ")

    def add_sports_facility(self):
        address = self.view.get_sports_facility_address()
        email, type, name = self.view.get_sports_facility_input()
        if len(address) > 30:
            sys.exit("Error: Sports_facility: address is long")
        if len(email) > 20:
            sys.exit("Error: Sports_facility: Owner email is long")
        if len(type) > 30:
            sys.exit("Error: Sports_facility: type is long")
        if len(name) > 30:
            sys.exit("Error: Sports_facility: name is long")
        if not bool(self.model.owner_row_search(email)):
            sys.exit("Error: Sports_facility: Owner email is not exist")
        if bool(self.model.sports_facility_row_search(address)):
            sys.exit("Error: Sports_facility: this primary key already exists")
        self.model.sports_facility_add(address, email, type, name)
        self.view.show_message("Sports_facility: added successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.sports_facility_menu()

    def view_sports_facility(self):
        sports_facilities = self.model.sports_facility_get_all_rows()
        self.view.sports_facility_show_all_rows(sports_facilities)
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.sports_facility_menu()

    def update_sports_facility(self):
        old_address = self.view.get_sports_facility_old_address()
        address = self.view.get_sports_facility_address()
        email, type, name = self.view.get_sports_facility_input()
        if len(old_address) > 30:
            sys.exit("Error: Sports_facility: old_address is long")
        if len(address) > 30:
            sys.exit("Error: Sports_facility: address is long")
        if len(email) > 20:
            sys.exit("Error: Sports_facility: Owner email is long")
        if len(type) > 30:
            sys.exit("Error: Sports_facility: type is long")
        if len(name) > 30:
            sys.exit("Error: Sports_facility: name is long")
        if not bool(self.model.sports_facility_row_search(old_address)):
            sys.exit("Error: Sports_facility: old_primary key is not exist")
        if not bool(self.model.owner_row_search(email)):
            sys.exit("Error: Sports_facility: Owner email is not exist")
        if bool(self.model.sports_facility_row_search(address)):
            sys.exit("Error: Sports_facility: new_primary key already exists")
        self.model.sports_facility_update(old_address, address, email, type, name)
        self.view.show_message("Sports_facility: updated successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.sports_facility_menu()

    def delete_sports_facility(self):
        address = self.view.get_sports_facility_address()
        if len(address) > 30:
            sys.exit("Error: Sports_facility: address is long")
        if not bool(self.model.sports_facility_row_search(address)):
            sys.exit("Error: Sports_facility: address is not exist")
        self.model.sports_facility_delete(address)
        self.view.show_message("Sports_facility: delted successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.sports_facility_menu()

    def random_generate_sports_facility(self):
        row_count = self.view.get_row_count_input()
        if not self.is_positive_int(row_count):
            sys.exit("Error: Sports_facility: row_count is not positive integer number")
        if int(row_count) > 100000:
            sys.exit("Error: Sports_facility: row_count is to many")
        self.model.sports_facility_random_generate(row_count)
        self.view.show_message("Sports_facility: generated successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.sports_facility_menu()

# table 'rent':

    def rent_menu(self):
        os.system('cls')
        choice = self.show_rent_menu()
        if choice == '1':
            os.system('cls')
            self.add_rent()
        elif choice == '2':
            os.system('cls')
            self.view_rent()
        elif choice == '3':
            os.system('cls')
            self.update_rent()
        elif choice == '4':
            os.system('cls')
            self.delete_rent()
        elif choice == '5':
            os.system('cls')
            self.random_generate_rent()
        elif choice == '0':
            os.system('cls')
            self.main_menu()

    def show_rent_menu(self):
        self.view.show_message("\nRent:\n")
        self.view.show_message("1. Add row")
        self.view.show_message("2. Show all rows")
        self.view.show_message("3. Update row")
        self.view.show_message("4. Delete row")
        self.view.show_message("5. Generate random rows")
        self.view.show_message("0. Quit")
        return self.view.get_value_input("Enter your choice: ")

    def add_rent(self):
        address, start_of_rent = self.view.get_rent_address_and_start()
        email, end_of_rent, rent_price_in_us = self.view.get_rent_input()
        if len(address) > 30:
            sys.exit("Error: Rent: address is long")
        if len(start_of_rent) > 19:
            sys.exit("Error: Rent: start_of_rent is long")
        if len(email) > 20:
            sys.exit("Error: Rent: email is long")
        if len(end_of_rent) > 19:
            sys.exit("Error: Rent: end_of_rent is long")
        if len(rent_price_in_us) > 16:
            sys.exit("Error: Rent: rent_price_in_us is long")
        if not bool(self.model.sports_facility_row_search(address)):
            sys.exit("Error: Rent: Sports_facility address is not exist")
        if not bool(self.model.tenant_row_search(email)):
            sys.exit("Error: Rent: Tenant email is not exist")
        if not self.is_timestamp(start_of_rent):
            sys.exit("Error: Rent: start_of_rent is not match the format")
        if not self.is_timestamp(end_of_rent):
            sys.exit("Error: Rent: end_of_rent is not match the format")
        if self.timestamps_comparing(start_of_rent, end_of_rent):
            sys.exit("Error: Rent: start_of_rent exceeds end_of_rent")
        if not self.is_positive_float(rent_price_in_us):
            sys.exit("Error: Rent: rent_price_in_us is not positive real number")
        if bool(self.model.rent_row_search(address, start_of_rent)):
            sys.exit("Error: Rent: this primary key already exists")
        self.model.rent_add(address, email, start_of_rent, end_of_rent, rent_price_in_us)
        self.view.show_message("Rent: added successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.rent_menu()

    def view_rent(self):
        rent = self.model.rent_get_all_rows()
        self.view.rent_show_all_rows(rent)
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.rent_menu()

    def update_rent(self):
        old_address, old_start_of_rent = self.view.get_rent_old_address_and_old_start()
        address, start_of_rent = self.view.get_rent_address_and_start()
        email, end_of_rent, rent_price_in_us = self.view.get_rent_input()
        if len(old_address) > 30:
            sys.exit("Error: Rent: old_address is long")
        if len(old_start_of_rent) > 19:
            sys.exit("Error: Rent: old_start_of_rent is long")
        if len(address) > 30:
            sys.exit("Error: Rent: address is long")
        if len(start_of_rent) > 19:
            sys.exit("Error: Rent: start_of_rent is long")
        if len(email) > 20:
            sys.exit("Error: Rent: email is long")
        if len(end_of_rent) > 19:
            sys.exit("Error: Rent: end_of_rent is long")
        if len(rent_price_in_us) > 16:
            sys.exit("Error: Rent: rent_price_in_us is long")
        if not bool(self.model.sports_facility_row_search(address)):
            sys.exit("Error: Rent: Sports_facility address is not exist")
        if not bool(self.model.tenant_row_search(email)):
            sys.exit("Error: Rent: Tenant email is not exist")
        if not self.is_timestamp(old_start_of_rent):
            sys.exit("Error: Rent: old_start_of_rent is not match the format")
        if not self.is_timestamp(start_of_rent):
            sys.exit("Error: Rent: start_of_rent is not match the format")
        if not self.is_timestamp(end_of_rent):
            sys.exit("Error: Rent: end_of_rent is not match the format")
        if self.timestamps_comparing(start_of_rent, end_of_rent):
            sys.exit("Error: Rent: start_of_rent exceeds end_of_rent")
        if not bool(self.model.rent_row_search(old_address, old_start_of_rent)):
            sys.exit("Error: Rent: old_primary key is not exist")
        if not self.is_positive_float(rent_price_in_us):
            sys.exit("Error: Rent: rent_price_in_us is not positive real number")
        if bool(self.model.rent_row_search(address, start_of_rent)):
            sys.exit("Error: Rent: new_primary key already exists")
        self.model.rent_update(old_address, old_start_of_rent, address, email, start_of_rent, end_of_rent, rent_price_in_us)
        self.view.show_message("Rent: updated successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.rent_menu()

    def delete_rent(self):
        address, start_of_rent = self.view.get_rent_address_and_start()
        if len(address) > 30:
            sys.exit("Error: Rent: address is long")
        if len(start_of_rent) > 19:
            sys.exit("Error: Rent: start_of_rent is long")
        if not self.is_timestamp(start_of_rent):
            sys.exit("Error: Rent: start_of_rent is not match the format")
        if not bool(self.model.rent_row_search(address, start_of_rent)):
            sys.exit("Error: Rent: this primary key is not exist")
        self.model.rent_delete(address, start_of_rent)
        self.view.show_message("Rent: delted successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.rent_menu()

    def random_generate_rent(self):
        row_count = self.view.get_row_count_input()
        if not self.is_positive_int(row_count):
            sys.exit("Error: Rent: row_count is not positive integer number")
        if int(row_count) > 200000:
            sys.exit("Error: Rent: row_count is to many")
        self.model.rent_random_generate(row_count)
        self.view.show_message("Rent: generated successfully!")
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.rent_menu()

# interesting requests:

    def interesting_requests_menu(self):
        os.system('cls')
        choice = self.show_interesting_requests_menu()
        if choice == '1':
            os.system('cls')
            self.total_income_rating_owner()
        elif choice == '2':
            os.system('cls')
            self.total_count_rented_facilities_rating_tenant()
        elif choice == '0':
            os.system('cls')
            self.main_menu()

    def show_interesting_requests_menu(self):
        self.view.show_message("\nInteresting requests:\n")
        self.view.show_message("1. Rating of the total income of the owners")
        self.view.show_message("2. Rating of the total number of leased objects of tenants")
        self.view.show_message("0. Quit")
        return self.view.get_value_input("Enter your choice: ")

    def total_income_rating_owner(self):
        row_count = self.view.get_row_count_input()
        min_sum = self.view.get_min_sum_input()
        if not self.is_positive_int(row_count):
            sys.exit("Error: Interesting requests: row_count is not positive integer number")
        if not self.is_positive_float(min_sum):
            sys.exit("Error: Interesting requests: min_sum is not positive real number")
        income_rating, execution_time = self.model.owner_total_income_rating(min_sum, row_count)
        self.view.owner_total_income_rating_show(income_rating, execution_time)
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.interesting_requests_menu()

    def total_count_rented_facilities_rating_tenant(self):
        row_count = self.view.get_row_count_input()
        start_timestamp, end_timestamp = self.view.get_time_range_limits_input()
        if not self.is_positive_int(row_count):
            sys.exit("Error: Interesting requests: row_count is not positive integer number")
        if len(start_timestamp) > 19:
            sys.exit("Error: Interesting requests: start_timestamp is long")
        if len(end_timestamp) > 19:
            sys.exit("Error: Interesting requests: end_timestamp is long")
        if not self.is_timestamp(start_timestamp):
            sys.exit("Error: Interesting requests: start_timestamp is not match the format")
        if not self.is_timestamp(end_timestamp):
            sys.exit("Error: Interesting requests: end_timestamp is not match the format")
        if self.timestamps_comparing(start_timestamp, end_timestamp):
            sys.exit("Error: Interesting requests: start_timestamp exceeds end_timestamp")
        count_rating, execution_time = self.model.tenant_total_count_rented_facilities_rating(start_timestamp, end_timestamp, row_count)
        self.view.tenant_total_count_rented_facilities_rating_show(count_rating, execution_time)
        self.view.show_message("0. Quit")
        if(self.view.get_value_input("Enter your choice: ") == '0'):
            self.interesting_requests_menu()

# additional functions:

    def is_positive_float(self, number):
        try:
            if(float(number) > 0):
                return True 
            return False
        except ValueError:
            return False 

    def is_positive_int(self, number):
        try:
            if(int(number) > 0):
                return True 
            return False
        except ValueError:
            return False

    def is_timestamp(self, timestamp):
        try:
            datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            return True 
        except ValueError:
            return False
    
    def timestamps_comparing(self, timestamp1, timestamp2):
        return datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S") >= datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")