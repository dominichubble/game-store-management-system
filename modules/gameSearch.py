# Student ID: F319859
"""
Module: gameSearch.py
Description: Provides functions to search for video games in the inventory based on various criteria such as title, genre, or platform. Each function returns a list of games that match the search criteria.
"""
import database

def searchByTitle(title):
    """
    Searches for games by title.

    Args:
    title (str): The title to search for.

    Returns:
    list: A list of games that match the specified title.
    """
    gameHeader, gameData = database.readGameInfo()

    try:
        titleIndex = gameHeader.index('Title')
    except ValueError:
        print("Error: 'Title' column not found in game data.")
        return []

    matchingGames = [game for game in gameData if game[titleIndex].lower() == title.lower()]
    return matchingGames

def searchByGenre(genre):
    """
    Searches for games by genre.

    Args:
    genre (str): The genre to search for.

    Returns:
    list: A list of games that match the specified genre.
    """
    gameHeader, gameData = database.readGameInfo()

    try:
        genreIndex = gameHeader.index('Genre')
    except ValueError:
        print("Error: 'Genre' column not found in game data.")
        return []

    matchingGames = [game for game in gameData if game[genreIndex].lower() == genre.lower()]
    return matchingGames

def searchByPlatform(platform):
    """
    Searches for games by platform.

    Args:
    platform (str): The platform to search for.

    Returns:
    list: A list of games that match the specified platform.
    """
    gameHeader, gameData = database.readGameInfo()

    try:
        platformIndex = gameHeader.index('Platform')
    except ValueError:
        print("Error: 'Platform' column not found in game data.")
        return []

    matchingGames = [game for game in gameData if game[platformIndex].lower() == platform.lower()]
    return matchingGames

if __name__ == "__main__":
    # Test the search functions
    print("Testing search by Title:")
    print(searchByTitle("COD"))

    print("\nTesting search by Genre:")
    print(searchByGenre("Action"))

    print("\nTesting search by Platform:")
    print(searchByPlatform("PlayStation"))
