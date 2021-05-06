from werkzeug.security import generate_password_hash
from app.models import db, User
# from faker import Faker
# fake = Faker()

# Adds a demo user, you can add other users here if you want


# def generate_users():
#     users = []
#     i = 0
#     while i < 20:
#         user = User(username=fake.user_name(),
#                     first_name=fake.first_name(),
#                     last_name=fake.last_name(),
#                     email=fake.email(),
#                     password=fake.password())
#         users.append(user)
#         i += 1
#     for user in users:
#         db.session.add(user)


def seed_users():

    demo = User(username='Demo', first_name='Demo', last_name="Lition", email='demo@lition.com', password='password')
    user2 = User(username='yvonn3', first_name='Randy', last_name="Silva", email='a@a.com', password='password')
    user3 = User(username='jimgreen', first_name='Jason', last_name="Cohen", email='b@b.com', password='password')
    user4 = User(username='ujones', first_name='Kim', last_name="Rodriguez", email='c@c.com', password='password')
    user5 = User(username='ncruz', first_name='Nicolas', last_name="Leon", email='d@d.com', password='password')
    user6 = User(username='amaxwell', first_name='David', last_name="Nelson", email='e@e.com', password='password')
    user7 = User(username='tersakim', first_name='Toni', last_name="Fowler", email='f@f.com', password='password')
    user8 = User(username='scunningham', first_name='Samantha', last_name="Bryant", email='g@g.com', password='password')
    user9 = User(username='bdavid', first_name='Joseph', last_name="Leon", email='h@h.com', password='password')
    user10 = User(username='bruce', first_name='John', last_name="Elliott", email='i@i.com', password='password')
    user11 = User(username='kimberlyfitz', first_name='Martha', last_name="Williams", email='j@j.com', password='password')
    user12 = User(username='dsynder', first_name='Jennifer', last_name="Lee", email='k@k.com', password='password')
    user13 = User(username='tarabrown', first_name='Jen', last_name="Ortiz", email='l@l.com', password='password')
    user14 = User(username='qlutz', first_name='Travis', last_name="Esparaza", email='m@m.com', password='password')
    user15 = User(username='thomasbuddy', first_name='Shelly', last_name="Wong", email='n@n.com', password='password')
    user16 = User(username='christoph', first_name='Brenda', last_name="Price", email='o@o.com', password='password')
    user17 = User(username='vkim', first_name='Nancy', last_name="Baker", email='p@p.com', password='password')
    user18 = User(username='wilsonj', first_name='Jessica', last_name="Brady", email='q@q.com', password='password')
    user19 = User(username='sramirez', first_name='Renee', last_name="Snyder", email='r@r.com', password='password')
    user20 = User(username='emilythomas', first_name='Patricia', last_name="Sims", email='s@s.com', password='password')
    user21 = User(username='jennifer20', first_name='Tamara', last_name="Anderson", email='t@t.com', password='password')

    db.session.add(demo)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.add(user9)
    db.session.add(user10)
    db.session.add(user11)
    db.session.add(user12)
    db.session.add(user13)
    db.session.add(user14)
    db.session.add(user15)
    db.session.add(user16)
    db.session.add(user17)
    db.session.add(user18)
    db.session.add(user19)
    db.session.add(user20)
    db.session.add(user21)
    # generate_users()
    db.session.commit()


# [... 'add_provider', 'address', 'am_pm', 'android_platform_token', 'ascii_company_email', 'ascii_email', 'ascii_free_email', 'ascii_safe_email', 'bank_country', 'bban', 'binary', 'boolean', 'bothify', 'bs', 'building_number', 'cache_pattern', 'catch_phrase', 'century', 'chrome', 'city', 'city_prefix', 'city_suffix', 'color', 'color_name', 'company', 'company_email', 'company_suffix', 'coordinate', 'country', 'country_calling_code', 'country_code', 'credit_card_expire', 'credit_card_full', 'credit_card_number', 'credit_card_provider', 'credit_card_security_code', 'cryptocurrency', 'cryptocurrency_code', 'cryptocurrency_name', 'csv', 'currency', 'currency_code', 'currency_name', 'currency_symbol', 'date', 'date_between', 'date_between_dates', 'date_object', 'date_of_birth', 'date_this_century', 'date_this_decade', 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between', 'date_time_between_dates', 'date_time_this_century', 'date_time_this_decade', 'date_time_this_month', 'date_time_this_year', 'day_of_month', 'day_of_week', 'dga', 'domain_name', 'domain_word', 'dsv', 'ean', 'ean13', 'ean8', 'ein', 'email', 'factories', 'file_extension', 'file_name', 'file_path', 'firefox', 'first_name', 'first_name_female', 'first_name_male', 'format', 'free_email', 'free_email_domain', 'future_date', 'future_datetime', 'generator_attrs', 'get_formatter', 'get_providers', 'hex_color', 'hexify', 'hostname', 'http_method', 'iban', 'image_url', 'internet_explorer', 'invalid_ssn', 'ios_platform_token', 'ipv4', 'ipv4_network_class', 'ipv4_private', 'ipv4_public', 'ipv6', 'isbn10', 'isbn13', 'iso8601', 'items', 'itin', 'job', 'language_code', 'language_name', 'last_name', 'last_name_female', 'last_name_male', 'latitude', 'latlng', 'lexify', 'license_plate', 'linux_platform_token', 'linux_processor', 'local_latlng', 'locale', 'locales', 'localized_ean', 'localized_ean13', 'localized_ean8', 'location_on_land', 'longitude', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'military_apo', 'military_dpo', 'military_ship', 'military_state', 'mime_type', 'month', 'month_name', 'msisdn', 'name', 'name_female', 'name_male', 'null_boolean', 'numerify', 'opera', 'paragraph', 'paragraphs', 'parse', 'password', 'past_date', 'past_datetime', 'phone_number', 'port_number', 'postalcode', 'postalcode_in_state', 'postalcode_plus4', 'postcode', 'postcode_in_state', 'prefix', 'prefix_female', 'prefix_male', 'profile', 'provider', 'providers', 'psv', 'pybool', 'pydecimal', 'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyset', 'pystr', 'pystr_format', 'pystruct', 'pytimezone', 'pytuple', 'random', 'random_choices', 'random_digit', 'random_digit_not_null', 'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element', 'random_elements', 'random_int', 'random_letter', 'random_letters', 'random_lowercase_letter', 'random_number', 'random_sample', 'random_uppercase_letter', 'randomize_nb_elements', 'rgb_color', 'rgb_css_color', 'safari', 'safe_color_name', 'safe_email', 'safe_hex_color', 'secondary_address', 'seed', 'seed_instance', 'seed_locale', 'sentence', 'sentences', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'state', 'state_abbr', 'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'tar', 'text', 'texts', 'time', 'time_delta', 'time_object', 'time_series', 'timezone', 'tld', 'tsv', 'unix_device', 'unix_partition', 'unix_time', 'upc_a', 'upc_e', 'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent', 'user_name', 'uuid4', 'weights', 'windows_platform_token', 'word', 'words', 'year', 'zip', 'zipcode', 'zipcode_in_state', 'zipcode_plus4']

# USERS

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key


def undo_users():
    db.session.execute('TRUNCATE users CASCADE;')
    db.session.commit()
