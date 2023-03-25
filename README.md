# Word Guess Game
### Inspiration
### Basic Information
## Features
## Testing
### Accessibility
## Validator Testing
No errors or problems are showing in Gitpod terminal.
- ![this is an image](./assets/images/validation-screenshot.png)
### Bugs or Errors
- I found a bug in score calculation which i tried my best to solve but i couldnt and the display
  of the name and score on gspread wasn't in the right order. So my Mentor helped me to solve these issues and improving my code. 
- I forgot to validate user input and got advise from my mentor to add it as well :) 

## Language and Technologies
- [Python3](https://python.org)

## Frameworks and Libraries
- Random is used to display words from lists randomly.
- Datetime is used to display date and time to the user.
- Googlesheets (gspread) is used to create Leaderboard / Scoreboard.
- Github template provided by Codeinstitute.
- Gitpod to create and write our code.
- Github is used to store the project.
- Heroku is used to deploy and run the project.

## Deployement
I followed the steps written below to deploy my project to [Heroku](https://heroku.com/), based on the [Code Institute](https://codeinstitute.net/) instructions:

- First created account on Heroku by flollowing the instructions given from Code Institute.

- pip3 freeze > requirements.txt to install our dependencies to Heroku.
- Commit changes push the changes to Github:
  git commit -m "Add requirements for deployment”

In HEROKU after creating the account:

- "Create new App".

- Give the App a unique name and enter region.

- Click on "Create App".

- Click on "Settings" on your new App Dashboard.

- Scroll down to Config Vars to add creds.json files and KEY: PORT and VALUE: 8000 for the 
  deployment.

- Press Add-button.

- Scroll down to Buildpacks and press the icon for Python, click Save Changes, then press the icon  
  for Nodejs and save changes. These Buildpacks need to be same as in the order below:

  -  Python 
  -  NodeJS

- Go to Deploy section tab and scroll down to Deployment Method.I connect to Github pages and then
  could search for my Github Repository "guessword-game" and then click connect.

- Scroll down to Automatic and Manual Deploys sections. I clicked on Manual Deployment.

- Then in the Manual Deploy section, press Deploy Branch.

- After the project has been deployed successfully I clicked the View-button to see the program run 
  in the terminal.

Credits
## Credits
- [youtube](https://youtube.com/) for videos related to word guess game.
- My mentor helped me to fix bug in the score calculation and adding scores on google 
  spreadsheets.
- [google](https://google.com/) for searching how to import and display date and time
  and data to create different lists of words. 
- [stackoverflow](https://stackoverflow.com/) to learn how to validate user input data.
## Content
- Code institute for the READ.md layout.
- [Stackoverflow](https://stackoverflow.com/) for input validation and date and time display.
- [youtube](https://youtube.com/) to add scores in game.
- [google](https://google.com/) to create lists of emotions, animal, birds and country names.
