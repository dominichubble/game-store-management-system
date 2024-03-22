# Student ID: F319859
"""
Module: gameRent.py
Description: Manages the game renting process. Validates customer IDs and game IDs, checks subscription status and game availability, and updates the rental records. Returns a message indicating the outcome of the rental attempt.
"""
import database
import subscriptionManager
from datetime import datetime

def rentGame(customerId, gameId):
    """
    Handles the process of renting a game to a customer based on their subscription status and game availability.

    Args:
    customerId (str): The ID of the customer trying to rent a game.
    gameId (str): The ID of the game the customer is trying to rent.

    Returns:
    str: A message indicating the outcome of the rental attempt.
    """
    # Load subscription data to check customer's subscription status
    subscriptions = subscriptionManager.load_subscriptions('data/Subscription_Info.txt')

    # Verify if the customer's subscription is active
    if not subscriptionManager.check_subscription(customerId, subscriptions):
        return "Customer subscription is not active."

    # Determine rental limit based on customer's subscription type
    customerSubscription = subscriptions.get(customerId, {})
    subscriptionType = customerSubscription.get('type', 'Basic')  # Default to 'Basic' if type is not found
    rentalLimit = subscriptionManager.get_rental_limit(subscriptionType)

    # Retrieve current game rental information
    _, rentalData = database.readRentalInfo()

    # Check if customer already has maximum allowed rentals
    currentRentals = sum(1 for rental in rentalData if rental[3] == customerId and not rental[2])
    if currentRentals >= rentalLimit:
        return f"Customer has reached their rental limit of {rentalLimit} games."

    # Check if the requested game is available for rent
    _, gameData = database.readGameInfo()
    gameAvailable = any(game[0] == gameId and all(rental[0] != gameId or rental[2] for rental in rentalData) for game in gameData)
    if not gameAvailable:
        return "Game is not available for rent."

    # Process the game rental
    rentalRecord = [gameId, datetime.now().strftime("%d/%m/%Y"), "", customerId]
    rentalData.append(rentalRecord)
    database.writeRentalInfo(rentalData)
    return "Game rented successfully."

if __name__ == "__main__":
    # Test the rent game function
    print("Testing game rent:")
    print(rentGame("coai", "cod01"))  # Use valid IDs as per your data
