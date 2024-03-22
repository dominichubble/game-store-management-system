# Student ID: F319859
"""
Module: database.py
Description: Provides common database functionalities such as reading and writing to text files that store game information and rental transactions. It serves as a central module used by other parts of the system for database interactions.
"""
# File paths for game information and rental data
gameInfoFile = 'data/Game_Info.txt'
rentalFile = 'data/Rental.txt'

# Headers for game information and rental data files
gameInfoHeaders = ["ID", "Platform", "Genre", "Title", "Publisher", "Purchase Date"]
rentalHeaders = ["Game ID", "Rental Date", "Return Date", "Rented Customer ID"]

def readFile(filePath):
    """
    Reads data from a specified text file and returns it as a list of lists.
    
    Args:
    filePath (str): The path of the file to be read.

    Returns:
    tuple: A tuple containing the headers and the data from the file.
    """
    data = []
    try:
        with open(filePath, 'r') as file:
            headers = file.readline().strip().split(',')
            for line in file:
                data.append(line.strip().split(','))
        return headers, data
    except FileNotFoundError:
        print(f"Error: The file {filePath} was not found.")
        return [], []

def writeFile(filePath, data):
    """
    Writes the given data to a specified text file.

    Args:
    filePath (str): The path of the file where data is to be written.
    data (list): The data to be written to the file.
    """
    headers = gameInfoHeaders if filePath == gameInfoFile else rentalHeaders
    try:
        with open(filePath, 'w') as file:
            file.write(','.join(headers) + '\n')
            for record in data:
                file.write(','.join(record) + '\n')
    except Exception as e:
        print(f"Error: Unable to write to {filePath}. Details: {e}")

def readGameInfo():
    """
    Reads the Game_Info.txt file.

    Returns:
    tuple: A tuple containing headers and game information data.
    """
    return readFile(gameInfoFile)

def readRentalInfo():
    """
    Reads the Rental.txt file.

    Returns:
    tuple: A tuple containing headers and rental data.
    """
    return readFile(rentalFile)

def writeGameInfo(data):
    """
    Writes data to the Game_Info.txt file.

    Args:
    data (list): The data to be written to the Game_Info.txt file.
    """
    writeFile(gameInfoFile, data)

def writeRentalInfo(data):
    """
    Writes data to the Rental.txt file.

    Args:
    data (list): The data to be written to the Rental.txt file.
    """
    writeFile(rentalFile, data)
