## T1A3 Camilla De Pretto - Terminal Application
Terminal application submitted for Coder Academy diploma. 

The application is a a text-based terminal, born from my interest in mystery games and stories like Arthur C. Doyle's 'Sherlock Holmes', the name itself is a reference to the first book by the author. 

### Github online repository link
(link)

### Style guide convention used: 
[Google Python style guide] (https://google.github.io/styleguide/pyguide.html)

### How to use the app: 
This app needs Python3 installed to be used successfully. 

--> virtual environment

To run the app write `./src/run.sh` in the terminal. 


### Features: 
The main features of 'A Study in Red' are: 
+ Program - user inteaction\
 There's a continuos interaction between the program and the user throughout the entire use of the terminal application through a input-output relationship. \
 From the beginning the user will have to choose an username that will be returned as well as the role they will have in the game. \
 The user will try to catch the responsible of the crime starting from the main option menu, that is gonna appear after a brief introduction, where they can choose between investigating the crime scene, interviewing the suspects, use the notebook, make an accusation or quit the game. 

+ Character depth\
 For the text-based game to be successful, it was necessary to create suspects with a motive and an alibi. There are a total of five suspects, each own with their own alibi and motives. It's up to the user to try to catch the killer by examining the evidence and reasoning about the suspects' interviews. 

+  Notebook
 The notebook is a feature on its own for the fact that the user can add, remove, edit and view the notes they wrote just with a single input of the keyboard. \
 It's a useful tool to write down what the user think the killer is. 

### Implementation plan: 
Trello has been used to keep track of the application's development. I divided the tasks by each feature I wanted to be implemented. \
The deadline is set on 5 May, the day of the assignment's submission, and the list of features are checked as I complete writing the code for them. 

![Screenshot 1](./docs/Screenshot%201.png)
![Screenshot 2](./docs/Screenshot%202.png)
![Screenshot 3](./docs/Screenshot%203.png)
![Screenshot 4](./docs/Screenshot%204.png)
![Screenshot 5](./docs/Screenshot%205.png)
![Scrrenshot 6](./docs/Screenshot%206.png)


### Walkthrough: 
After running the code for starting the program the title will appear, and the user will be asked to input an username. 

--> screenshot

There is an introduction where it is said that the user is a detective assigned to a homicide case and has to catch the killer. 

The main menu consist of choosing from 5 options: 1. investigate the crime scene, 2. interview the suspects, 3. use the notebook, 4. make the final accusation and quit the game. 

--> screenshot 

If the user choose the first option, 'investigate the crime scene', in the terminal will appear a series of evidence and after that the user will be able to go back the menu by pressing enter. 

--> screenshot

When the user wants to interview the suspects by pressing '2' in the main option menu, a list of suspects will appear. The suspects of this game are: the wife, the son, the driver, the chef and the cleaning lady. Everyone has an alibi, and most has also a motive. 

--> screenshot 

The notebook function can be very useful to the user who wants to write down what they remember from the evidence and interviews.\ 
The 'add note' option will have the user to input thoughts freely. the 'remove note' will delete a note, the 'edit note' option will remove a note and change it with another one. Finally the 'view notes' can be used for reviewing what has been written so far. \
The last option is to go back to the main menu. 

--> screenshot

If the user press '4' it will take them to the final stage of the game... catching the killer!\ 
The programm will ask the user to input the suspect they think could be the responsible of the crime. \
If that won't be the case and the user inputs a incorrect name, they will have the chance to try again. 

--> screenshot 

The last and final option from the main menu is to quit the game. 
--> screenshot


