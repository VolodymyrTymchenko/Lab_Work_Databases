
class View:
    def show_message(self, message):
        print(message)

    def get_value_input(self, message):
        return input(message)

# table 'owner':

    def owner_show_all_rows(self, owners):
        print(f"{'-':-<69}")
        print(f"|{'owner':^67}|")
        print(f"{'-':-<69}")
        print(f"|{'email':^30}|{'phone_number':^15}|{'name':^20}|")
        print(f"{'-':-<69}")
        for owner in owners:
            print(f"|{owner[0]:>30}|{owner[1]:>15}|{owner[2]:>20}|")
            print(f"{'-':-<69}")

    def get_owner_input(self):
        phome_number = input("Enter owner phome number: ")
        name = input("Enter owner name: ")
        return phome_number, name

    def get_owner_email(self):
        email = input("Enter owner email: ")
        return email

    def get_owner_old_email(self):
        old_email = input("Enter owner old email: ")
        return old_email
    
# table 'tenant':

    def tenant_show_all_rows(self, tenants):
        print(f"{'-':-<69}")
        print(f"|{'tenant':^67}|")
        print(f"{'-':-<69}")
        print(f"|{'email':^30}|{'phone_number':^15}|{'name':^20}|")
        print(f"{'-':-<69}")
        for tenant in tenants:
            print(f"|{tenant[0]:>30}|{tenant[1]:>15}|{tenant[2]:>20}|")
            print(f"{'-':-<69}")

    def get_tenant_input(self):
        phome_number = input("Enter tenant phome number: ")
        name = input("Enter tenant name: ")
        return phome_number, name

    def get_tenant_email(self):
        email = str(input("Enter tenant email: "))
        return email

    def get_tenant_old_email(self):
        old_email = input("Enter tenant old email: ")
        return old_email

# table 'sports_facility':

    def sports_facility_show_all_rows(self, sports_facilities):
        print(f"{'-':-<127}")
        print(f"|{'sports_facility':^125}|")
        print(f"{'-':-<127}")
        print(f"|{'address':^32}|{'email':^30}|{'type':^30}|{'name':^30}|")
        print(f"{'-':-<127}")
        for sports_facility in sports_facilities:
            print(f"|{sports_facility[0]:>32}|{sports_facility[1]:>30}|{sports_facility[2]:>30}|{sports_facility[3]:>30}|")
            print(f"{'-':-<127}")

    def get_sports_facility_input(self):
        email = input("Enter sports_facility email: ")
        type = input("Enter sports_facility type: ")
        name = input("Enter sports_facility name: ")
        return email, type, name

    def get_sports_facility_address(self):
        address = input("Enter sports_facility address: ")
        return address

    def get_sports_facility_old_address(self):
        old_address = input("Enter sports_facility old address: ")
        return old_address

# table 'rent':

    def rent_show_all_rows(self, rent):
        print(f"{'-':-<124}")
        print(f"|{'rent':^122}|")
        print(f"{'-':-<124}")
        print(f"|{'address':^32}|{'email':^30}|{'start_of_rent':^20}|{'end_of_rent':^20}|{'rent_price_in_us':^16}|")
        print(f"{'-':-<124}")
        for rent_elem in rent:
            print(f"|{rent_elem[0]:>32}|{rent_elem[1]:>30}| {rent_elem[2]}| {rent_elem[3]}|{rent_elem[4]:>16}|")
            print(f"{'-':-<124}")

    def get_rent_input(self):
        email = input("Enter rent email: ")
        end_of_rent = input("Enter end of rent: ")
        rent_price_in_us = input("Enter rent price in us: ")
        return email, end_of_rent, rent_price_in_us

    def get_rent_address_and_start(self):
        address = input("Enter rent address: ")
        start_of_rent = input("Enter start of rent: ")
        return address, start_of_rent

    def get_rent_old_address_and_old_start(self):
        old_address = input("Enter rent old address: ")
        old_start_of_rent = input("Enter old start of rent: ")
        return old_address, old_start_of_rent

# interesting requests:

    def owner_total_income_rating_show(self, income_rating, execution_time):
        print(f"{'-':-<77}")
        print(f"|{'Rating of the total income of the owners':^75}|")
        print(f"{'-':-<77}")
        print(f"|{'rating':^16}|{'name':^20}|{'email':^20}|{'total_income':^16}|")
        print(f"{'-':-<77}")
        for income in income_rating:
            print(f"|{income[0]:>16}|{income[1]:>20}|{income[2]:>20}|{income[3]:>16}|")
            print(f"{'-':-<77}")
        print(f"Total query runtime: {execution_time} msec.\n")

    def tenant_total_count_rented_facilities_rating_show(self, count_rating, execution_time):
        print(f"{'-':-<77}")
        print(f"|{'Rating of the total number of leased objects of tenants':^75}|")
        print(f"{'-':-<77}")
        print(f"|{'rating':^16}|{'name':^20}|{'email':^20}|{'total_count':^16}|")
        print(f"{'-':-<77}")
        for count in count_rating:
            print(f"|{count[0]:>16}|{count[1]:>20}|{count[2]:>20}|{count[3]:>16}|")
            print(f"{'-':-<77}")
        print(f"Total query runtime: {execution_time} msec.\n")

    def get_row_count_input(self):
        row_count = input("Enter the number of rows: ")
        return row_count

    def get_min_sum_input(self):
        min_sum = input("Enter the minimum sum: ")
        return min_sum

    def get_time_range_limits_input(self):
        start_timestamp = input("Enter start timestamp: ")
        end_timestamp = input("Enter end timestamp: ")
        return start_timestamp, end_timestamp
