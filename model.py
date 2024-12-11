import psycopg2
import time

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(dbname = 'postgres', user = 'postgres', password = 'v0v@1234', host = 'localhost', port = 5432)

# table 'owner':

    def owner_add(self, email, phome_number, name):
        curs = self.conn.cursor()
        curs.execute('INSERT INTO owner (email, phone_number, name) VALUES (%s, %s, %s)', (email, phome_number, name))
        self.conn.commit()

    def owner_get_all_rows(self):
        curs = self.conn.cursor()
        curs.execute('SELECT * FROM owner')
        return curs.fetchall()

    def owner_update(self, old_email, email, phome_number, name):
        curs = self.conn.cursor()
        curs.execute('UPDATE owner SET email=%s, phone_number=%s, name=%s WHERE email=%s', (email, phome_number, name, old_email))
        self.conn.commit()

    def owner_delete(self, email):
        curs = self.conn.cursor()
        curs.execute('DELETE FROM owner WHERE email=%s', (email,))
        self.conn.commit()

    def owner_random_generate(self, row_count):
        curs = self.conn.cursor()
        curs.execute("""
            INSERT INTO owner (email, phone_number, name) 
            SELECT email1, phone_number1, name1
            FROM
            (
                SELECT (Lower(name1) || '.' || to_char(trunc(random()*999999)::int, 'FM000000') || '@ukr.net')::varchar(20) AS email1,
                    ('+380' || to_char(trunc(random()*99)::int, '00') || to_char(trunc(random()*9999999)::int, '0000000'))::varchar(20) AS phone_number1, 
                    (name1)::varchar(20)
                FROM 
                (
                    SELECT (ARRAY['Mary', 'Eddy', 'Denis', 'Jack', 'Garry', 'Alice', 'Bob', 'Tom', 'Linda', 'John'])[trunc(random() * 10 + 1)::int] AS name1
                    FROM generate_series(1, %s)
                ) subquery1
            ) subquery2
            ON CONFLICT(email) DO NOTHING;
        """, (row_count,))
        self.conn.commit()

    def owner_row_search(self, email):
        curs = self.conn.cursor()
        curs.execute('SELECT * FROM owner WHERE email=%s', (email,))
        return curs.fetchone()

# table 'tenant':

    def tenant_add(self, email, phome_number, name):
        curs = self.conn.cursor()
        curs.execute('INSERT INTO tenant (email, phone_number, name) VALUES (%s, %s, %s)', (email, phome_number, name))
        self.conn.commit()

    def tenant_get_all_rows(self):
        curs = self.conn.cursor()
        curs.execute('SELECT * FROM tenant')
        return curs.fetchall()

    def tenant_update(self, old_email, email, phome_number, name):
        curs = self.conn.cursor()
        curs.execute('UPDATE tenant SET email=%s, phone_number=%s, name=%s WHERE email=%s', (email, phome_number, name, old_email))
        self.conn.commit()

    def tenant_delete(self, email):
        curs = self.conn.cursor()
        curs.execute('DELETE FROM tenant WHERE email=%s', (email,))
        self.conn.commit()

    def tenant_random_generate(self, row_count):
        curs = self.conn.cursor()
        curs.execute("""
            INSERT INTO tenant (email, phone_number, name) 
            SELECT email1, phone_number1, name1
            FROM
            (
                SELECT (Lower(name1) || '.' || to_char(trunc(random()*999999)::int, 'FM000000') || '@ukr.net')::varchar(20) AS email1,
                    ('+380' || to_char(trunc(random()*99)::int, '00') || to_char(trunc(random()*9999999)::int, '0000000'))::varchar(20) AS phone_number1, 
                    (name1)::varchar(20)
                FROM 
                (
                    SELECT (ARRAY['Ann', 'John', 'Paul', 'Max', 'Tom', 'Carl', 'Antony', 'Garry', 'Kevin', 'Fred'])[trunc(random() * 10 + 1)::int] AS name1
                    FROM generate_series(1, %s)
                ) subquery1
            ) subquery2
            ON CONFLICT(email) DO NOTHING;
        """, (row_count,))
        self.conn.commit()

    def tenant_row_search(self, email):
        curs = self.conn.cursor()
        curs.execute("SELECT * FROM tenant WHERE email=%s", (email,))
        return curs.fetchone()

# table 'sports_facility':

    def sports_facility_add(self, address, email, type, name):
        curs = self.conn.cursor()
        curs.execute('INSERT INTO sports_facility (address, email, type, name) VALUES (%s, %s, %s, %s)', (address, email, type, name))
        self.conn.commit()

    def sports_facility_get_all_rows(self):
        curs = self.conn.cursor()
        curs.execute('SELECT * FROM sports_facility')
        return curs.fetchall()

    def sports_facility_update(self, old_address, address, email, type, name):
        curs = self.conn.cursor()
        curs.execute('UPDATE sports_facility SET address=%s, email=%s, type=%s, name=%s WHERE address=%s', (address, email, type, name, old_address))
        self.conn.commit()

    def sports_facility_delete(self, address):
        curs = self.conn.cursor()
        curs.execute('DELETE FROM sports_facility WHERE address=%s', (address,))
        self.conn.commit()

    def sports_facility_random_generate(self, row_count):
        curs = self.conn.cursor()
        curs.execute("""
            INSERT INTO sports_facility (address, email, type, name) 
            SELECT address1, email1, type1, name1
            FROM
            (
                SELECT  (city || ',' || ' ' || (trunc(random()*999)::int)::text || letter || ' ' || street || ' ' || 'st.')::varchar(32) AS address1,
                        email1, type1::varchar(30), (city || name2)::varchar(30) AS name1
                FROM
                (
                    SELECT (ARRAY['Kyiv', 'Lviv', 'Odesa', 'Kharkiv', 'Dnipro', 'Poltava', 'Sumy', 'Rivne', 'Lutsk', 'Uman', 'Brovary', 'Irpin', 'Nizhyn', 'Kovel', 'Obukhov'])[trunc(random() * 15 + 1)::int] AS city,
                           (ARRAY['', 'a', 'b', 'c', 'd', 'e'])[trunc(random() * 6 + 1)::int] AS letter,
                           (ARRAY['Shevchenko', 'Hrushevskogo', 'Grecheskya', 'Vyshneva', 'Parkova', 'Azovska', 'Abrikosova', 'Baikova', 'Berezova', 'Verbova', 'Galitska', 'Dachna', 'Druzhby', 'Zalisna', 'Lipneva'])[trunc(random() * 15 + 1)::int] AS street,
                           (ARRAY['swiming pool', 'tennis court', 'football field', 'golf course', 'basketball court', 'volleyball court', 'rugby field', 'ice skating rink', 'gym'])[trunc(random() * 9 + 1)::int] AS type1,
                           (ARRAY['Sport', 'Fitness', 'Life'])[trunc(random() * 3 + 1)::int] AS name2,
                           email AS email1
                    FROM generate_series(1, %(count)s),
                    (
                        SELECT email
                        FROM owner
                        ORDER BY random()
                        
                    ) subquery1
                ) subquery2 
                LIMIT %(count)s
            ) subquery3
        ON CONFLICT(address) DO NOTHING;
        """, {'count' : row_count})
        self.conn.commit()

    def sports_facility_row_search(self, address):
        curs = self.conn.cursor()
        curs.execute('SELECT * FROM sports_facility WHERE address=%s', (address,))
        return curs.fetchone()

# table 'rent':

    def rent_add(self, address, email, start_of_rent, end_of_rent, rent_price_in_us):
        curs = self.conn.cursor()
        curs.execute('INSERT INTO rent (address, email, start_of_rent, end_of_rent, rent_price_in_us) VALUES (%s, %s, %s, %s, %s)', (address, email, start_of_rent, end_of_rent, rent_price_in_us))
        self.conn.commit()

    def rent_get_all_rows(self):
        curs = self.conn.cursor()
        curs.execute('SELECT * FROM rent')
        return curs.fetchall()

    def rent_update(self, old_address, old_start_of_rent, address, email, start_of_rent, end_of_rent, rent_price_in_us):
        curs = self.conn.cursor()
        curs.execute('UPDATE rent SET address=%s, email=%s, start_of_rent=%s, end_of_rent=%s, rent_price_in_us=%s WHERE address=%s and start_of_rent=%s', (address, email, start_of_rent, end_of_rent, rent_price_in_us, old_address, old_start_of_rent))
        self.conn.commit()

    def rent_delete(self, address, start_of_rent):
        curs = self.conn.cursor()
        curs.execute('DELETE FROM rent WHERE address=%s and start_of_rent=%s', (address, start_of_rent))
        self.conn.commit()

    def rent_random_generate(self, row_count):
        curs = self.conn.cursor()
        curs.execute("""
            INSERT INTO rent (address, email, start_of_rent, end_of_rent, rent_price_in_us) 
            SELECT address1, email1, start_of_rent1, end_of_rent1, rent_price_in_us1
            FROM
            (
                SELECT address1, email1, random_timestamp AS start_of_rent1, random_timestamp + (floor(random() * 48)::int || ' hours')::INTERVAL AS end_of_rent1, (random() * 999)::numeric(5, 2) AS rent_price_in_us1
                FROM 
                (
                    SELECT date_trunc('second', TIMESTAMP '2020-01-01 00:00:00' + (random() * (TIMESTAMP '2024-12-07 23:59:59' - TIMESTAMP '2020-01-01 00:00:00'))) AS random_timestamp,
                    email1, address1
                    FROM generate_series(1, %(count)s),
                    (
                        SELECT 
                            t1.email AS email1, t2.address AS address1
                        FROM 
                            (SELECT email FROM tenant LIMIT 1000 OFFSET floor(random() * 99000)) t1
                        CROSS JOIN 
                            (SELECT address FROM sports_facility LIMIT 1000 OFFSET floor(random() * 99000)) t2
                    ) subquery1
                )
                LIMIT %(count)s
            ) subquery2
        ON CONFLICT(address, start_of_rent) DO NOTHING;
        """, {'count' : row_count})
        self.conn.commit()

    def rent_row_search(self, address, start_of_rent):
        curs = self.conn.cursor()
        curs.execute('SELECT * FROM rent WHERE address=%s and start_of_rent=%s', (address, start_of_rent))
        return curs.fetchone()

# interesting requests:

    def owner_total_income_rating(self, min_sum, row_count):
        curs = self.conn.cursor()
        start_time = int(time.time() * 1000)
        curs.execute("""
            SELECT DENSE_RANK() OVER (ORDER BY SUM(r.rent_price_in_us) DESC) AS rating, o.name, s.email, SUM(r.rent_price_in_us) AS total_income
            FROM owner o, rent r, sports_facility s
            WHERE o.email = s.email AND r.address = s.address
            GROUP BY s.email, o.name
            HAVING SUM(r.rent_price_in_us) > %s
            ORDER BY total_income DESC
            LIMIT %s
        """, (min_sum, row_count))
        end_time = int(time.time() * 1000) - start_time
        return curs.fetchall(), end_time

    def tenant_total_count_rented_facilities_rating(self, start_timestamp, end_timestamp, row_count):
        curs = self.conn.cursor()
        start_time = int(time.time() * 1000)
        curs.execute("""
            SELECT DENSE_RANK() OVER (ORDER BY COUNT(r.address) DESC) AS rating, t.name, r.email, COUNT(r.address) AS total_count
            FROM tenant t, rent r
            WHERE r.email = t.email AND r.start_of_rent BETWEEN %s AND %s
            GROUP BY r.email, t.name
            ORDER BY total_count DESC
            LIMIT %s
        """, (start_timestamp, end_timestamp, row_count))
        end_time = int(time.time() * 1000) - start_time
        return curs.fetchall(), end_time
