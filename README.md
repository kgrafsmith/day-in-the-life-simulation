**READ ME:** Day In The Life at Smith College  
By Fiona Bloom, Kendra Graf, and Jackie Wiechmann

**Files required:**

1. MAIN:   
   1. The entry point of the program.  
   2. Runs the game by calling wake\_up() from WAKE\_UP.py.  
   3. Handles the overall flow and ensures all modules load correctly.  
2. WAKE\_UP:  
   1. Contains the function wake\_up(), which begins the game.  
   2. Greets the player using their stored name and presents breakfast options.  
   3. Directs the player to the next module based on their choice (i.e. PATH\_BLUE, PATH\_PINK, etc.).  
3. PATH\_BLUE, PATH\_PINK, PATH\_GREEN:  
   1. Each file contains a function controlling the next step after breakfast.  
   2. Presents the player with multiple choices for what to do next.  
   3. Uses loops to ensure the player enters a valid input.  
   4. Directs the player to new events or ultimately to the game ending.  
4. GAME\_OVER:  
   1. Contains the game\_over() function.  
   2. Prints a final message summarizing the player’s day.  
   3. Calls create\_collage() from COLLAGE.py to generate a visual summary of the player's choices.  
5. GLOBAL\_VARS:  
   1. Stores global variables used across files (i.e. player name, choices).  
   2. Allows different modules to access shared information.  
6. COLLAGE:  
   1. Uses the graphics library to open a window and draw a collage showing what the player did.  
   2. Displays images in a grid (top-left, top-right, bottom-left, bottom-right) corresponding to the choices made throughout the game.  
   3. Called only when the player reaches the end.

**How to Run & Interact With the Project (User Guide)**

1. **Running the Game**  
   1. Ensure all project files are in the same folder:  
      1. MAIN.py, GLOBAL\_VARS.py, path modules, WAKE\_UP.py, GAME\_OVER.py, COLLAGE.py, and the images.  
      2. Open the folder in Thonny.  
      3. Run the file MAIN.py.  
2. **Starting the Game**  
   1. When the game begins, you’ll be greeted and asked for your name, major, and house (if applicable).  
   2. The game then presents choices like breakfast options, class choices, work shifts, or skipping activities.  
3. **Making Choices**  
   1. Each menu gives numbered options:

   1\. Option One  

   2\. Option Two  

   3\. Option Three

   2. Type the number of your choice and press Enter.  
   3. If you type something invalid, the game asks again until you choose correctly.  
4. **Story Progression**  
   1. Your choices determine:  
      1. Where you go on campus  
      2. Who you interact with  
      3. What events happen  
      4. Which images appear in your final collage  
   2. Each branch leads to different outcomes, but all eventually reach the ending.  
5. **The Ending**  
   1. When you finish your day, the game runs game\_over().  
   2. A message prints summarizing your adventure.  
   3. The collage window pops up, showing images representing your choices:  
      1. Top-left \= first decision  
      2. Top-right \= second event  
      3. Bottom-left \= third event  
      4. Bottom-right \= final result  
6. **Exiting the Game**  
   1. Simply close the graphics window.  
   2. The program then ends normally.