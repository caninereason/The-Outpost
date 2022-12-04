# Site Overview
The outpost is a simple text adventure game made in python. The player must navigate their way around and abandoned outpost and find a way to escape.

## Goal
I was fascinated by the "choose your own adventure" books as a child, and wished to create a science fiction themed version. I had been thinking of this theme for a long time and this project seemed like the ideal place to bring this story to life.

## Technologies used
- [Heroku](https://heroku.com) to deploy the website.
- [Python](https://www.python.org/) for the main game-play.
- [GitHub](https://github.com/) as a remote repository.
- [Visual Studio Code](https://code.visualstudio.com/) as a local IDE & repository.

## Target Audience
- lovers of science fiction
- people who enjoy text adventure games and interactive novels

## Future Features
- I have had the idea for this project for a long time and feel it could make a compelling narative.In the future I would like to further develop the storyline, adding more rooms, pickups, graphics and scenarios. However the text adventure game style is not to everyone's liking and I may change this to incorporate better graphics, UI and playability.

# Implementation
- I opted for a game loop which would print each scenario, the rooms would be organised into a collection of arrays, containing the room number, room text, optional text for keys etc. and an array of exits. This array would contain a zero if that direction was unavailable, or if this exit was available, it would contain the connecting rooms number. This allowed me to orgainize and edit the rooms and connections in an intuitive way.

# Design
- I began by drawing a map of all the rooms, and using this map I proceeded to populate each room with it's appropiate number, description, exits and pickups.
This made it easy to organise and iterate through each rooms dialogue and  options.

# Bugs
- There was a bug found with the lock on level 12, it seemed I had confused some of the logic with room 5, so it was a simple fix to rearrange the logic to fix the error.
# Deployment 

### Version Control
- I used git as the version control software. With the use of the commands git add . , git commit -m "", and git push , I was able to add, save and push code to the github repository.