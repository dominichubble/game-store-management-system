# Student ID: F319859
"""
Module: gameReturn.py
Description: Handles the return of rented video games. It updates the rental database to reflect game returns and prompts the store manager to enter feedback about the customer's experience, which is then stored in an external feedback database.
"""
import database
import feedbackManager
from datetime import datetime

def returnGame(gameId, rating, comments):
    """
    Handles the process of returning a rented game and recording feedback.

    Args:
    gameId (str): The ID of the game being returned.
    rating (int): The rating given to the game.
    comments (str): Any comments about the game.

    Returns:
    str: A message indicating the outcome of the return process.
    """
    # Retrieve current game rental information
    rentalHeaders, rentalData = database.readRentalInfo()

    # Locate the rental record for the specified game
    rentalRecord = next((rental for rental in rentalData if rental[0] == gameId and not rental[2]), None)
    if not rentalRecord:
        return "Error: Game ID is invalid or the game is already available."

    # Mark the game as returned by updating the return date
    rentalRecord[2] = datetime.now().strftime("%d/%m/%Y")
    database.writeRentalInfo(rentalData)

    # Record the customer's feedback in the external feedback database
    feedbackManager.add_feedback(gameId, int(rating), comments, 'data/Game_Feedback.txt')

    return "Game returned successfully and feedback recorded."

if __name__ == "__main__":
    # Test the return game function
    print("Testing game return:")
    print(returnGame("cod01", 5, "Great experience"))  # Use a valid game ID
