# Student ID: F319859
"""
This module generates a set of video game information records, including game IDs, platforms, genres, titles, publishers, and purchase dates. The data is randomly generated and written to a text file.
"""
import random
from datetime import datetime, timedelta

def generateIncrementalDates(startDate, numRecords, minDays=1, maxDays=30):
    """
    Generates a sequence of dates, incrementing each date randomly within a specified range.

    Args:
    startDate (datetime): The starting date for the sequence.
    numRecords (int): Number of dates to generate.
    minDays (int): Minimum days to increment.
    maxDays (int): Maximum days to increment.

    Yields:
    datetime: A sequence of incremented dates.
    """
    currentDate = startDate
    for _ in range(numRecords):
        yield currentDate
        currentDate += timedelta(days=random.randint(minDays, maxDays))

def generateGameInfo(numRecords):
    """
    Generates a list of game information records.

    Args:
    numRecords (int): Number of game records to generate.

    Returns:
    list: A list of lists, each containing game information.
    """
    # Define a list of game details
    games = [
        {'title': 'COD', 'platforms': ['PlayStation', 'Xbox', 'PC'], 'genre': 'Action', 'publisher': 'Activision'},
        {'title': 'FIFA', 'platforms': ['PlayStation', 'Xbox', 'Nintendo Switch'], 'genre': 'Sports', 'publisher': 'EA Sports'},
        {'title': 'Minecraft', 'platforms': ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch'], 'genre': 'Sandbox', 'publisher': 'Mojang'},
        {'title': 'Overwatch', 'platforms': ['PC', 'PlayStation', 'Xbox'], 'genre': 'Shooter', 'publisher': 'Blizzard Entertainment'},
        {'title': 'Fortnite', 'platforms': ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch', 'Mobile'], 'genre': 'Battle Royale', 'publisher': 'Epic Games'},
        {'title': 'Dark Souls', 'platforms': ['PC', 'PlayStation', 'Xbox'], 'genre': 'RPG', 'publisher': 'FromSoftware'},
        {'title': 'Assassin\'s Creed', 'platforms': ['PC', 'PlayStation', 'Xbox'], 'genre': 'Adventure', 'publisher': 'Ubisoft'},
        {'title': 'Halo', 'platforms': ['Xbox'], 'genre': 'Shooter', 'publisher': 'Microsoft Studios'},
        {'title': 'Elden Ring', 'platforms': ['PC', 'PlayStation', 'Xbox'], 'genre': 'RPG', 'publisher': 'FromSoftware'},
        {'title': 'Doom', 'platforms': ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch'], 'genre': 'Shooter', 'publisher': 'Bethesda Softworks'},
    ]
    gameCounters = {game['title']: 0 for game in games}
    purchaseDates = list(generateIncrementalDates(datetime(2015, 1, 1), numRecords * len(games), 1, 90))

    gameInfoData = []
    dateIndex = 0

    # Generate game information data
    while len(gameInfoData) < numRecords:
        for game in games:
            gameCounters[game['title']] += 1
            gameId = f"{game['title'][:4].lower()}{gameCounters[game['title']]:02d}"
            platform = random.choice(game['platforms'])
            genre = game['genre']
            title = game['title']
            publisher = game['publisher']
            purchaseDate = purchaseDates[dateIndex].strftime("%d/%m/%Y")
            gameInfoData.append([gameId, platform, genre, title, publisher, purchaseDate])
            dateIndex += 1

            if len(gameInfoData) == numRecords:
                break

    return gameInfoData


# Generate game information and rental data
gameInfo = generateGameInfo(20)

# Save generated data to files
with open('data/Game_Info.txt', 'w') as file:
    file.write("ID,Platform,Genre,Title,Publisher,Purchase Date\n")
    for record in gameInfo:
        file.write(",".join(record) + "\n")
