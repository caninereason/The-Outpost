# Site Overview
The outpost is a simple text adventure game made in python. The player must navigate their way around and abandoned outpost and find a way to escape. There are many rooms to explore, and if the player is diligent and clever, the game should take no more than 10 minutes to complete.

## Goal
I was fascinated by the "choose your own adventure" books as a child, and wished to create a science fiction themed version. I had been thinking of this theme for a long time and this project seemed like the ideal place to bring this story to life.

## Technologies used
- [Heroku](https://heroku.com) to deploy the website.
- [Python](https://www.python.org/) for the main game.
- [GitHub](https://github.com/) as a remote repository.
- [Visual Studio Code](https://code.visualstudio.com/) as a local IDE & repository.

## Target Audience
- Lovers of science fiction
- People who enjoy text adventure games and interactive novels
- Those who enjoy a challenging adventure game

## Future Features
- I have had the idea for this project for a long time and feel it could make a compelling narative. The arrangement of each rooms array is organised so future additions and editing rooms would be quite simple.In the future I would like to further develop the storyline, adding more rooms, pickups, graphics and scenarios. However the text adventure game style is not to everyone's liking and I may change this to incorporate better graphics, UI and playability. 

# Design
- I began by drawing a map of all the rooms, and using this map I proceeded to populate each room with it's appropiate number, description, exits and pickups.
This made it easy to organise and iterate through each rooms dialogue and  options. I then added a few interactive elements such as a lazer, a key to pickup and a book the player could examine which would teleport them to a random room. Given the scope of this project I found these to be a sufficient number of interactable objects.

![alt text](readme_docs/map.png)
# Implementation
- I opted for a game loop which would print each scenario, the rooms being organised into a collection of arrays, containing the room number, room text, optional text for keys etc. and an array of exits. This array would contain a zero if that direction was unavailable, or if this exit was available, it would contain the connecting rooms number. This allowed me to orgainize and edit the rooms and connections in an intuitive way. I also gave the rooms an 'extra' variable, which if populated would allow the user to interact with something or change the initial description based on which direction they might come from. This was implemented sparsley but does work as a good option should I want to add objects in the future. 

# Bugs
- There was a bug found with the lock on level 12, it seemed I had confused some of the logic with room 5, so it was a simple fix to rearrange the logic to fix the error.
- There were other small bugs, such as text not updating after a pickup , or room sequences not ordered correctly. After much testing these were wasy to fix.

# Deployment 

## Deployment to Heroku
1. Navigate to [Heroku](https://dashboard.heroku.com/apps)
2. Find 'New' and select 'Create a new app'
3. Name your application and create app.
4. Go to to 'Settings'
5. Under Buildpacks click the add buildpacks button. Select Python and save changes and then node.js and save changes.
6. Navigate to the 'Deploy' section. 
7. Connect to GitHub, search for your repo and confirm. 
8. Choose branch to deploy.
9. There was an error in heroku deploying after the 28th of November, the fix was as follows
- from the dashboard in Heroku, click configure dynos
- you should see an unconfigured node index.js, you can edit this with the pen on the right.
- while editing click the slider to turn on then click on confirm, the dyno is now configured.

## How to Fork
1. Login to [GitHub](https://github.com/).
2. Locate the repository 
3. Click on the 'Fork' button in the upper left.
4. Your should now have a forked version of the repository.

### Version Control
- I used git as the version control software. With the use of the commands git add . , git commit -m "", and git push , I was able to add, save and push code to the github repository.


