# Student ID: F319859
"""
This module generates rental records for video games, including game IDs, rental dates, return dates, and customer IDs. The rental dates are randomly generated within a specified range and stored in a text file.
"""
import random
from datetime import datetime, timedelta

def read_file(file_path):
    """
    Reads a text file and returns its data as a list of lists.

    Args:
    file_path (str): Path to the file to be read.

    Returns:
    list: A list of lists, each containing a line's contents.
    """
    data = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            data.append(line.strip().split(','))
    return data

def generate_rental_dates(start_date, end_date, num_records):
    """
    Generates random rental and return dates for games within a specified date range.

    Args:
    start_date (datetime): The start date of the period.
    end_date (datetime): The end date of the period.
    num_records (int): Number of records to generate.

    Returns:
    list: A list of tuples containing rental and return dates.
    """
    dates = []
    for _ in range(num_records):
        # Generate a random rental date within the specified range
        rental_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        # Generate a random return date, ensuring it is after the rental date
        return_date = rental_date + timedelta(days=random.randint(1, 30))  # Rental period between 1 to 30 days
        dates.append((rental_date.strftime("%d/%m/%Y"), return_date.strftime("%d/%m/%Y")))
    return dates

def parse_date(date_str):
    """
    Parses a date string into a datetime object.

    Args:
    date_str (str): Date string in the format 'dd/mm/YYYY'.

    Returns:
    datetime: The corresponding datetime object.
    """
    return datetime.strptime(date_str, "%d/%m/%Y")

# Read game and customer IDs from respective files
game_info = read_file('data/Game_Info.txt')
game_ids = [game[0] for game in game_info]

customer_info = read_file('data/Subscription_Info.txt')
customer_ids = [customer[0] for customer in customer_info]

start_date = datetime(2015, 1, 1)
end_date = datetime.now()
rental_records = []

# Generate rental records
for game_id in game_ids:
    dates = generate_rental_dates(start_date, end_date, random.randint(5, 15))
    for rental_date, return_date in dates:
        customer_id = random.choice(customer_ids)
        rental_records.append([game_id, rental_date, return_date, customer_id])

# Sort rental records by rental date
rental_records.sort(key=lambda x: parse_date(x[1]))

# Save sorted rental records to Rental.txt
with open('data/Rental.txt', 'w') as file:
    file.write("Game ID,Rental Date,Return Date,Rented Customer ID\n")
    for record in rental_records:
        file.write(','.join(record) + '\n')