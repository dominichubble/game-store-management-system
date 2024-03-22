# Student ID: F319859
"""
Module: inventoryPruning.py
Description: Identifies video game titles for potential removal from the inventory based on rental frequency. Offers visualisations to aid decision-making and actively removes selected games from the inventory database.
"""
import database
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import Counter

def get_rental_frequency():
    """
    Retrieves and counts the frequency of rentals for each game.

    Returns:
    dict: A dictionary with game IDs as keys and their rental counts as values.
    """
    # Retrieve rental data and calculate rental frequency for each game
    _, rentalData = database.readRentalInfo()
    rentalCounts = Counter(rental[0] for rental in rentalData)
    return rentalCounts

def plot_rental_frequency(rentalCounts):
    """
    Plots the rental frequency of games.

    Args:
    rentalCounts (dict): A dictionary containing rental frequencies of games.
    """
    # Prepare data for plotting
    games, counts = zip(*rentalCounts.items())
    plt.figure(figsize=(10, 6))
    ax = plt.subplot(111)
    ax.bar(games, counts)

    # Format y-axis to display only whole numbers
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # Set plot labels and title
    plt.xlabel('Game ID')
    plt.ylabel('Number of Rentals')
    plt.title('Rental Frequency of Games')
    plt.xticks(rotation=90)
    plt.show()

def pruneGames():
    """
    Suggests games for removal from the inventory based on their rental frequencies.

    Returns:
    list: A list of game IDs suggested for removal.
    """
    rentalCounts = get_rental_frequency()

    # Check which games are still in the inventory
    _, gameData = database.readGameInfo()
    gamesInInventory = {game[0] for game in gameData}

    # Consider only games that are still in inventory
    filteredRentalCounts = {game_id: count for game_id, count in rentalCounts.items() if game_id in gamesInInventory}
    plot_rental_frequency(filteredRentalCounts)

    # Calculate mean rental frequency and determine removal threshold
    if filteredRentalCounts:
        meanRentalFrequency = sum(filteredRentalCounts.values()) / len(filteredRentalCounts)
        removalThreshold = meanRentalFrequency * 0.5  # 50% below the mean
    else:
        print("No rental data available for pruning.")
        return []

    # Identify games for potential removal
    suggestedGamesForRemoval = [game_id for game_id, count in filteredRentalCounts.items() if count < removalThreshold]
    return suggestedGamesForRemoval

def removeSelectedGames(gamesToRemove):
    """
    Removes selected games from the inventory.

    Args:
    gamesToRemove (list): A list of game IDs to be removed.

    Returns:
    str: A message indicating the outcome of the removal process.
    """
    if not gamesToRemove:
        return "No games were selected for removal."

    # Remove specified games from the inventory
    gameHeaders, gameData = database.readGameInfo()
    gameData = [game for game in gameData if game[0] not in gamesToRemove]
    database.writeGameInfo(gameData)

    return f"Removed the following games from the inventory: {', '.join(gamesToRemove)}"

if __name__ == "__main__":
    # Test the pruning functionality
    print("Testing pruning games:")
    suggestedGames = pruneGames()
    print("Suggested games for removal:", suggestedGames)

    print("\nTesting removal of selected games:")
    print(removeSelectedGames(suggestedGames[:2]))  # Remove first two suggested games as a test
