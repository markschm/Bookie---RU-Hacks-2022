# Bookie---RU-Hacks-2022<br/>
<p align="center">
  <a href="https://github.com//">
    <img src="https://media.discordapp.net/attachments/875958297272926221/972783475058958336/bookie.png?width=671&height=671" alt="Logo" width="80" height="80">
  </a>

  <h2 align="center">Bookie Bot</h2>
  <h3 align="center">RU-Hacks-2022</h3>

  <p align="center">
    Lets get productive on Discord with Bookie Bot!
    <br/>
    <br/>
    <a href="https://discord.com/api/oauth2/authorize?client_id=972629701048819722&permissions=8&scope=bot">Invite To Your Server!</a>
    <br/>
    <a href="https://replit.com/@MarkSchmid1/Bookie-The-Discord-Bot#main.py">Available On Repl</a>  
    <br/>
    <a href="https://devpost.com/software/test-mdjo6c#updates">Like us on DevPost</a>
  </p>
</p>


## What it does
Our Discord bot, Bookie Bot, has many productivity functions built inside of it, such as:
**To-Do List**
**Pomodoro Technique Timer**
**Grade Calculator**
**Motivational Quote Generator**
**Lifestyle Reminder**
**Help Function**

## Inspiration
When Covid-19 first hit, everyone was forced to move to online learning, where many had trouble with productivity, focus, and procrastination. We personally faced these problems as well, and considering that many people including ourselves still have online learning, we decided to create a Discord bot that would help with that.

## How we built it
We built the whole project on repl.it in order to efficiently collaborate remotely. We used Flask as our framework and to host our local server to keep it running indefinitely. We also used Python as our main programming language. We split Bookie Bot's functions into its own separate classes and had a main function that would call each function when called by the user. 

## Challenges we ran into
We initially wanted to have a scientific calculator similar to Wolfram Alpha's online calculator, and so we tried importing its APIs but had great difficulty dissecting and decoding the JSON file it outputted. After several hours of trial and error, we decided to cut our losses and move on.
Another challenge we ran into was the implementation of the asynchronous timer functions such as the Pomodoro Timer and Lifestyle Reminder, where we would need these functions to time themselves in the background, whilst still being able to call other functions in Bookie Bot. After a couple of hours, we eventually solved the logic behind the asynchronous functions and managed to successfully implement it.

## Accomplishments that we're proud of
As mentioned above, we are very proud of our ability to overcome the logic behind the asynchronous timer functions, where we managed to have the functions run in the background. Another thing we are proud of is the successful use of a local Flask server to host our bot, in order to have it run indefinitely.

## What we learned
As our first-ever hackathon, we learned a great deal. We learned a lot about how Discord bots are made, how to connect them to servers using tokens, how to host bots on local Flask servers, asynchronous functions, how to create Discord bot functions, and how to import and decode external APIs, and how to debug Discord APIs.

## What's next for Bookie Bot
As we have online summer school, all of us will continue to use Bookie Bot for our online productivity. We are also connecting it to our friends' servers to show off what we have made. As our first-ever hackathon project, Bookie Bot has served as a great learning opportunity and will act as a stepping stone to bigger and better projects for us in the future.

## Built With
**Python, Flask, JSON, DiscordAPI, Repl**

## Contributors 
* [Bruce](https://github.com/Bruce4PF)
* [Mark](https://github.com/markschm)
* [Alex](https://github.com/alexfatu)
* [Jacky](https://github.com/JackyLiu13)

## Getting Started

To get started <a href="https://discord.com/api/oauth2/authorize?client_id=972629701048819722&permissions=8&scope=bot">Click Me</a> to invite Bookie to your server!

## Usage
* **!todo** - Personal todo list <br/>
* **!pmd** - Pomodoro Timer <br/>
* **!quote** - Get a motivational quote <br/>
* **!gradecalculator** - Calculate current grade in a class <br/>
* **!lifestyle** - Healthy studying reminders <br/>
--------------------------- <br/>
**use !help (command name) to get help with a specific function**



## License

Distributed under the MIT License. See [LICENSE](https://github.com///blob/main/LICENSE.md) for more information.

## Authors

* **Alex** - *Comp Sci Student* - [Alex](https://github.com/alexfatu) - **
* **Bruce** - *Comp Sci Student* - [Bruce](https://github.com/Bruce4PF) - **
* **Jacky** - *Comp Sci Student* - [Jacky](https://github.com/JackyLiu13) - **
* **Mark** - *Comp Sci Student* - [Mark](https://github.com/markschm) - **

