F319859 
Nov 13, 2023 --> Dec 12, 2023

Hello and welcome to my Video Game Rental Management System. As the creator of this system, I'm thrilled to present a comprehensive solution that I've meticulously developed to streamline the management of video game rentals for store managers. This README outlines key features and essential instructions.

1. Inventory Pruning:

One of the system's standout features is the Inventory Pruning functionality. I've designed it to actively remove less popular video game titles from the inventory, based on their rental frequency.
This process utilises a dynamic threshold, calculated as 50% below the mean rental frequency, ensuring an adaptable and fair criterion for pruning games.
The system only considers games currently listed in Game_Info.txt, thus avoiding the redundancy of removing already pruned games.

2. Special Instructions:

Ensure all necessary data files (Game_Info.txt, Rental.txt, etc.) are correctly placed in their respective directories.
When operating the system, particularly via the Jupyter Notebook interface (menu.ipynb), verify that the 'modules' directory is correctly included in the Python path.
Familiarise yourself with the pruning feature's threshold-based logic for a full understanding of how it enhances inventory management.

3. System Highlights:

Robust Search Functionality: The system allows users to effortlessly search for games based on title, genre, or platform.
Streamlined Rental and Return Processes: Automated subscription checks during rentals and feedback collection upon returns are integral to the system.
User-Friendly GUI: I've devoted significant effort to ensuring the graphical interface is intuitive and simple to navigate.
Proactive Inventory Management: The adaptive nature of the Inventory Pruning functionality, which I am particularly proud of, not only suggests but also actively removes less popular games from the inventory.

4. Additional Notes:

This system is built using standard Python libraries, which aids in its compatibility and ease of maintenance.
If issues arise related to file paths or module imports, please consult the provided folder structure for guidance.
Closing Remarks:
Developing this system has been an immensely rewarding experience, marrying my technical abilities with practical application. The actual pruning of games, as part of the Inventory Management, is a testament to my commitment to creating innovative and effective management solutions.

Thank you for using or assessing my Video Game Rental Management System. Should you have any queries or require further assistance, please do not hesitate to contact me.