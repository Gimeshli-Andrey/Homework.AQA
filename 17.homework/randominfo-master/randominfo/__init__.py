from __future__ import unicode_literals
import sys
import glob
import csv
import pytz
import shutil
from os import listdir, getcwd, access, W_OK
from os.path import abspath, join, dirname, split, exists, isfile, isdir
from random import randint, choice, sample, randrange
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from math import ceil
from typing import Optional, Union, Dict, List, Any

__title__ = 'randominfo'
__version__ = '2.0.2'
__author__ = 'Bhuvan Gandhi'
__license__ = 'MIT'

__all__ = [
	'Person',
	'get_id',
	'get_first_name',
	'get_last_name',
	'get_gender',
	'get_country',
	'get_full_name',
	'get_otp',
	'get_formatted_datetime',
	'get_email',
	'get_phone_number',
	'random_password',
	'get_today',
	'get_date',
	'get_birthdate',
	'get_address',
	'get_hobbies'
]

START_RANGE = datetime(1970, 1, 1, 0, 0, 0, 0, pytz.UTC)
END_RANGE = datetime.today()


def full_path(filename: str) -> str:
	return abspath(join(dirname(__file__), filename))


def get_id(
		length: int = 6,
		seq_number: Optional[int] = None,
		step: int = 1,
		prefix: Optional[str] = None,
		postfix: Optional[str] = None
) -> str:
	if seq_number is not None and not isinstance(seq_number, int):
		raise TypeError("Sequence number must be an integer.")
	if not isinstance(step, int):
		raise TypeError("Step must be an integer.")

	if seq_number is None:
		generated_id = ''.join(str(randint(0, 9)) for _ in range(length))
	else:
		generated_id = str(seq_number + step)

	if prefix:
		generated_id = f"{prefix}{generated_id}"
	if postfix:
		generated_id = f"{generated_id}{postfix}"

	return generated_id


def get_first_name(gender: Optional[str] = None) -> str:
    with open(full_path('data.csv'), 'r', encoding='utf-8') as f:
        first_name_file = csv.reader(f)
        filtered_data = []

        if gender is None:
            filtered_data = [data[0] for data in first_name_file if data[0]]
        else:
            gender = gender.lower()
            if gender not in ("male", "female"):
                raise ValueError("Gender must be 'male' or 'female'.")
            filtered_data = [
                data[0] for data in first_name_file
                if data[0] and data[2] == gender
            ]

        if not filtered_data:
            raise ValueError("No names found matching criteria")

        return choice(filtered_data)



def get_last_name() -> str:
	"""Get random last name."""
	with open(full_path('data.csv'), 'r', encoding='utf-8') as f:
		last_name_file = csv.reader(f)
		filtered_data = [data[1] for data in last_name_file if data[1]]
		return choice(filtered_data)


def get_gender(first_name: str) -> str:
	with open(full_path('data.csv'), 'r', encoding='utf-8') as f:
		first_name_file = csv.reader(f)
		for data in first_name_file:
			if data[0] and data[0] == first_name:
				return data[2]
	return ""


def get_country(first_name: Optional[str] = None) -> str:
	with open(full_path('data.csv'), 'r', encoding='utf-8') as f:
		country_file = csv.reader(f)
		if first_name:
			for data in country_file:
				if data[0] and data[0] == first_name:
					return data[3]
			print("Specified user data is not available. Generating random country.")

		filtered_data = [data[12] for data in country_file if data[12]]
		return choice(filtered_data)


def get_full_name(gender: Optional[str] = None) -> str:
	return f"{get_first_name(gender)} {get_last_name()}"


def get_otp(
		length: int = 6,
		digit: bool = True,
		alpha: bool = True,
		lowercase: bool = True,
		uppercase: bool = True
) -> str:
	if not (digit or alpha):
		raise ValueError("At least one of 'digit' or 'alpha' must be True.")

	chars = ""
	if digit:
		chars += "0123456789"
	if alpha:
		if lowercase:
			chars += "abcdefghijklmnopqrstuvwxyz"
		if uppercase:
			chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	if not chars:
		raise ValueError("No character set selected")

	return ''.join(choice(chars) for _ in range(length))


def get_formatted_datetime(
		out_format: str,
		str_date: str,
		str_format: str = "%d-%m-%Y %H:%M:%S"
) -> str:
	return datetime.strptime(str_date, str_format).strftime(out_format)


def get_email(prsn: Optional['Person'] = None) -> str:
	domains = [
		"gmail", "yahoo", "hotmail", "express", "yandex", "nexus",
		"online", "omega", "institute", "finance", "company",
		"corporation", "community"
	]
	extensions = [
		'com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au',
		'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site', 'xyz',
		'zero', 'tech'
	]

	if prsn is None:
		prsn = Person()

	domain = f'@{choice(domains)}'
	extension = choice(extensions)

	email_type = randint(0, 2)
	if email_type == 0:
		email = f"{prsn.first_name}{get_formatted_datetime('%Y', prsn.birthdate, '%d %b, %Y')}"
	elif email_type == 1:
		email = f"{prsn.last_name}{get_formatted_datetime('%d', prsn.birthdate, '%d %b, %Y')}"
	else:
		email = f"{prsn.first_name}{get_formatted_datetime('%y', prsn.birthdate, '%d %b, %Y')}"

	return f"{email.lower()}{domain}.{extension}"


def random_password(
		length: int = 8,
		special_chars: bool = True,
		digits: bool = True
) -> str:
	if length < 1:
		raise ValueError("Password length must be positive")

	spec_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
	alpha = "QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq"
	chars = []

	if special_chars:
		spec_char_len = randint(1, ceil(length / 4))
		chars.extend(choice(spec_chars) for _ in range(spec_char_len))

	if digits:
		dig_char_len = randint(1, ceil(length / 3))
		chars.extend(str(randint(0, 9)) for _ in range(dig_char_len))

	remaining_len = length - len(chars)
	chars.extend(choice(alpha) for _ in range(remaining_len))

	return ''.join(sample(chars, len(chars)))


def get_phone_number(country_code: bool = True) -> str:
	phone_parts = []

	if country_code:
		country_codes = [91, 144, 141, 1, 44, 86, 52, 61, 32, 20, 33, 62, 81, 31, 7]
		phone_parts.append(f"+{choice(country_codes)}")

	first_digit = str(randint(6, 9))
	rest_digits = ''.join(str(randint(0, 9)) for _ in range(9))

	phone_parts.append(first_digit + rest_digits)

	return ' '.join(phone_parts)


def get_today(format_str: str = "%d-%m-%Y %H:%M:%S") -> str:
	return datetime.today().strftime(format_str)


def get_date(
		tstamp: Optional[int] = None,
		format_str: str = "%d %b, %Y"
) -> str:
	if tstamp is None:
		start_ts = START_RANGE.timestamp()
		end_ts = END_RANGE.timestamp()
		tstamp = randrange(int(start_ts), int(end_ts))
	elif not isinstance(tstamp, int):
		raise ValueError("Timestamp must be an integer")

	return datetime.utcfromtimestamp(tstamp).strftime(format_str)


def get_birthdate(
		start_age: Optional[int] = None,
		end_age: Optional[int] = None,
		format_str: str = "%d %b, %Y"
) -> str:
	if start_age is not None and not isinstance(start_age, int):
		raise ValueError("Starting age must be an integer")
	if end_age is not None and not isinstance(end_age, int):
		raise ValueError("Ending age must be an integer")

	if start_age is not None and end_age is not None:
		if start_age >= end_age:
			raise ValueError("Starting age must be less than ending age")
		start_range = datetime(datetime.now().year - start_age, 12, 31, 23, 59, 59, 0, pytz.UTC)
		end_range = datetime(datetime.now().year - end_age, 1, 1, 0, 0, 0, 0, pytz.UTC)
	elif start_age is not None or end_age is not None:
		age_year = start_age if start_age is not None else end_age
		start_range = datetime(datetime.now().year - age_year, 12, 31, 23, 59, 59, 0, pytz.UTC)
		end_range = datetime(datetime.now().year - age_year, 1, 1, 0, 0, 0, 0, pytz.UTC)
	else:
		start_range = END_RANGE
		end_range = START_RANGE

	start_ts = start_range.timestamp()
	end_ts = end_range.timestamp()
	return datetime.fromtimestamp(randrange(int(end_ts), int(start_ts))).strftime(format_str)


def get_address() -> Dict[str, str]:
	addr_params = ['street', 'landmark', 'area', 'city', 'state', 'country', 'pincode']
	full_addr = []

	with open(full_path('data.csv'), 'r', encoding='utf-8') as f:
		for i in range(5, 12):
			addr_file = csv.reader(f)
			all_addrs = [addr[i] for addr in addr_file if len(addr) > i and addr[i]]
			if all_addrs:
				full_addr.append(choice(all_addrs))

	return dict(zip(addr_params, full_addr))


def get_hobbies() -> List[str]:
	"""Generate random list of hobbies."""
	with open(full_path('data.csv'), 'r', encoding='utf-8') as f:
		hobbies_file = csv.reader(f)
		all_hobbies = [data[4] for data in hobbies_file if data[4]]
		return [choice(all_hobbies) for _ in range(randint(2, 6))]


class Person:

	def __init__(self, gender: Optional[str] = None):
		self.first_name = get_first_name(gender)
		self.last_name = get_last_name()
		self.full_name = f"{self.first_name} {self.last_name}"
		self.birthdate = get_birthdate()
		self.phone = get_phone_number()
		self.email = get_email(self)
		self.gender = get_gender(self.first_name)
		self.country = get_country(self.first_name)
		self.paswd = random_password()
		self.hobbies = get_hobbies()
		self.address = get_address()
		self.custom_attr: Dict[str, Any] = {}

	def set_attr(self, attr_name: str, value: Any = None) -> None:
		if not attr_name.isalnum():
			raise ValueError("Attribute name must contain only letters and numbers")
		if not attr_name[0].isalpha():
			raise ValueError("Attribute name must start with a letter")

		self.custom_attr[attr_name] = value
		print(f"Attribute '{attr_name}' added.")

	def get_attr(self, attr_name: str) -> Any:
		if not attr_name.isalnum():
			raise ValueError("Attribute name must contain only letters and numbers")
		if not attr_name[0].isalpha():
			raise ValueError("Attribute name must start with a letter")

		try:
			return self.custom_attr[attr_name]
		except KeyError:
			raise AttributeError("Specified attribute does not exist")

	def get_details(self) -> Dict[str, Any]:
		return {
			"first_name": self.first_name,
			"last_name": self.last_name,
			"full_name": self.full_name,
			"birthdate": self.birthdate,
			"gender": self.gender,
			"email": self.email,
			"phone": self.phone,
			"paswd": self.paswd,
			"country": self.country,
			"hobbies": self.hobbies,
			"address": self.address,
			"other_attr": self.custom_attr
		}
'''
REFERENCE:
http://www.first-names-meanings.com/country-indian-names.html
https://www.familyeducation.com/baby-names/browse-origin/surname/indian
https://thispersondoesnotexist.com/
https://en.wikipedia.org/wiki/List_of_hobbies
'''