# Final-Project
CS110 Final Project

**Goal:**
Use  what you have learned this semester to design, implement and demonstrate a Python program that shows that you can apply the basic principles of programming to a project of a larger scale than the assignments done so far. Each of you will work with  one other individual from the class to develop and implement the project. Note:  you don't have to go to the same lab session, but you should be evenly matched gradewise!

**Project Organization:**
* Your program must have a graphical user interface
* Your program must be designed so that the class that comprises the GUI user interface **is separate from** the code that implements the application logic, i.e. plays the game, accesses the database, etc.
* The code that implements the *application logic* **must be encapsulated in two or more classes.** The code that implements the user interface must be an Object-Oriented GUI class, and must create objects of one or more classes  (and have those objects will call their methods as needed).

**Some Project Ideas:**
* Write a program that simulates the playing of a game such as Hangman, Connect4, The Tic-Tac-Toe, etc. 
* Write a program that allows a user to play a game of Nim (either against the computer or against another user).  
There are many variations of this game.  Here is one version:  
	* The game starts with between 25 and 50 tokens  in a pile.  
	* Players alternately remove tokens from the pile. 
	* A player can take at most half of  the tokens but must take at least one token.
	* The player who takes the last token loses.
	* You can add to the difficulty level of your project by adding a feature which allows the user to choose whether the computer plays in dumb or in smart mode.  
	* In dumb mode the computer randomly picks a legal number of tokens (between 1 and n/2) to remove.
	* In smart mode the computer removes a number of tokens that makes the size of the pile a power of 2 minus 1 (i.e. 3, 7, 15, 31, etc.).
	* Since it is not possible to make such a pick when the current size of the pile is one less than a power of two, in this case the computer makes a random legal move.
* Write a program that plays a card game of your choosing. Suggestion: use an object containing a list of Card objects created from a Card class to represent one or more decks/piles of cards.
* Explore some additional features of SQLite by creating a table and writing a program that allows a user to connect to and query that table.
* Use the world database to create a geography quiz that might be used by elementary school children.
* Propose your own project.

**How to Work Together:**
* Once you and your partner have decided on a project that interests both of you, and which you believe can be implemented by both of you to completion (be realistic!), do the following:
	* Discuss the goal of your project and work up a preliminary analysis
	* At a minimum, draw up a top-level design of your project, and a top-level set of tasks that must be implemented to fulfill your design
	* Decide upon a mutually agreeable public interface for the major program units of your project
	* Divide up the tasks as follows:
		* You must work independently on at least one program unit each, and fulfill the public interface
		* You must work collaboratively on at least one program unit each
		* You can divide up the remaining program units as you see fit, but each unit must start with a comment specifying which one of you was responsible for designing and coding it, or be labeled collaborative
	* Program units
		* In a large project made up of several small cooperating classes, each of you could pick a class to design and code separately
		* In a small project made up of only a couple of classes, each of you could pick one or more methods of your application logic class to design and code separately
		* It is not recommended that one individual code all of the GUI and the other code all of the logic
		* You must document both individual and collaborative responsibility
	* You may unit test your code individually, but integration testing should be performed together
	* Integration testing is the perfect opportunity to teach each other the program units that were developed independently:
Make sure that you can answer questions about any part of your project!

**Grading Criteria:**
* Difficulty Level (10%)
	* Size of undertaking and use of material not covered in class (must have two)
* Design (30%)
	- Use of classes to decompose the problem and structure the code 
	- You MUST define and use two or more application logic classes
	- You must have a GUI class that encapsulates your user interface
	- You must be able to breakdown your project into discrete tasks that can be allocated separately to each of the people in your 'team'
* Quality of code (25%)  
	- Readability, internal documentation, coding style, clarity of logic and use of Python, 
   	- You must adhere to the class coding conventions
* User Interface (15%)
	- Ease of use, layout and clarity of GUI 
	- Handling of user input errors                          
	- Written or "online" User's Guide
* Demo (20%)
	- Quality and run-through of Acceptance Test Procedure 
	- Ability to explain the project and answer questions about it 
	- Each individual must demonstrate and explain their individual contribution
	
**What to bring to your Demo:**
* Partially filled out gradesheet (all gray areas must be filled out prior to your demo), one per 'team'
	* Stop by and pick up a copy of the gradesheet in my office on Wednesday if you're going to do an early bird
	* You can printout your own ONLY if you are able to set your margins to narrow
* Printout of ALL source code
	* All classes should be contained in separate files (and therefore printed out on separate pages)
		* The only allowable exceptions to this are be 'error' classes (like the BadArgument one we wrote), or those used strictly to create small 'helper' objects for other classes
	* All classes MUST be properly documented according to the documentation scheme covered this semester
	* All code must adhere to proper style conventions as covered this semester (good names, proper case, no magic numbers, proper structure, etc.)
* Printout of your external or online User's Guide consisting of
	* Cover sheet (Colorful pics/photos are encouraged)
	* A narrative explaining the purpose of the program
	* A dictionary-style summary of program controls (name/picture of control along with explanation)
	* Screen shots of your GUI illustrating program usage
	* Explanation of error or warning messages
* Printout of your Acceptance Test Procedure: Note the example one provided!
	* This is how you will demonstrate your program and show that all the features work 'as advertised'
		* It must be thorough and efficient
		* It must show how ALL of your program features work and that they work correctly
		* It must include steps that deal with how the program prevents or handles user error
		* Note how the sample ATP illustrates all of the features of the GuiCounter program, and how each step is arranged to set up the next test efficiently without undue repetition
	* You MUST write your ATP in the same tabular fashion illustrated in the sample provided
		* Columns must be same as shown:  
			* Step:  step number
			* Pay attention to description of next two columns!
				* Procedure:  exact procedure for tester to follow
				* Expected Results:  description of results to be expected - must be EXACT
				* Examples: 
					* Procedure:  ~~Enter a value into the entry box | Expected Results:  value is displayed: ~~ Incorrect, not exact
					* Procedure:  Go to Set Counter entry box, enter 10 and press <Enter>  |  Expected Results:  Display changes to Count = 10:  Correct, exact procedure and exact result
				* Actual Results:  LEAVE BLANK - will be filled in with appearance of results that actually occur during your demo
				* ✔ or AI: LEAVE BLANK - checkoff if actual results match expected results, 'Action Item' written up if results don't match during your demo
* Video Cable Adapter: if you can't use the video cable provided (this applies mainly to Mac users, but may apply to others:  when in doubt, try it out beforehand!)
	
**Words to the Wise:**
We keep a repository of previous projects.  All project code will be run through Moss (a program that detects the same or similar programs). If you hand in the same project as or a similar project to one from a previous semester OR found on the internet, you will receive a grade of 0, and will have to deal with this and other consequences of cheating.

**Important Dates and DUE DATES:**
* Monday, 4/8: On your Lecture attendance sheet:  list your name, your project partner's name, and your tentative project idea(s)
* Friday, 4/12: On your Lecture attendance sheet:  list your name and confirm your project partner's name and your project topic
* Week of May 6/8/10: Upload your project code electronically on the evening (May 9) before your lab if you intend to do an early bird including your User's Guide and Acceptance Test Procedure
	* Note:  Students wanting to do an Early bird without a previous upload will be allowed only at our discretion (i.e., Don't plan on it!)
	* Early Bird Final Project demonstrations (+ 10 points if completed early) OR sign up for demo during exam week
		* You must have all of your materials uploaded electronically beforehand as detailed above
		* You must BRING ALL OF YOUR REQUIRED PRINTOUTS such as your documented source code, ATP, User's Guide and Grading Sheet
		* First come, first served:  sign-in as soon as you arrive in lab, no special lab time if you're demoing
		* When it's your turn to demo, if any electronic or hardcopy materials are missing or incomplete, you will not be permitted to demo!
	* If you're NOT doing an Early Bird
		* Sign up for a time during exam week (TBD)
* Exam week in lab:  Final Project demonstrations (if you didn't take advantage of the Early Bird)
	* You must upload your code, User's Guide, and Acceptance Test Procedure before the time you are to demo
	* You must BRING ALL OF YOUR REQUIRED PRINTOUTS such as your documented source code, ATP, User's Guide and Grading Sheet
	* When it's your turn to demo, if any electronic or hardcopy materials are missing or incomplete, you will not be permitted to demo!
	* You must be in the lab at least 10 minutes before your assigned time
