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

# Implementation
- I opted for a game loop which would print each scenario, the rooms would be organised into a collection of arrays, containing the room number, room text, optional text for keys etc. and an array of exits. This array would contain a zero if that direction was unavailable, or if this exit was available, it would contain the connecting rooms number. This allowed me to orgainize and edit the rooms and connections in an intuitive way
# Bugs
- There was a bug found with the lock on level 12, it seemed I had confused some of the logic with room 5, so it was a simple fix to rearrange the logic