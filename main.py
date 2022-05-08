import discord
import os
import help
import todo
from pomodoro import Pomodoro
from motivational_quotes import get_quote
from grade_calculator import Grade_Calculator
from lifestyle import Lifestyle_Reminder
from perpetual import Perpetual


client = discord.Client()
pd = Pomodoro()
gc = Grade_Calculator()
ls = Lifestyle_Reminder()


@client.event
async def on_ready(): # when the bot is on
  print("Running...")

@client.event
async def on_message(message): # eveytime message is sent to the chat
  if message.content.startswith("!"):
    user_input = message.content.split(" ")

    if user_input[0] == "!help":
      help_string = ""
      if len(user_input) == 1:
        help_string = help.get_help_message()
      elif user_input[1] == "pmd" or user_input[1] == "pomodoro":
        help_string = help.get_pmd_help()
      elif user_input[1] == "todo":
        help_string = help.get_todo_help()
      elif user_input[1] == "gradecalculator":
        help_string = help.get_grade_calculator()
      elif user_input[1] == "lifestyle":
        help_string = help.get_lifestyle_help()
      else:
        help_string = "To get more specific help type !help followed by the command name"

      embed = discord.Embed( 
        title = "Help",
        description = help_string,
        colour = 15158332
      )
      await message.channel.send(embed=embed)

    elif message.content.startswith("!todo"):      
      msg = message.content.strip("!todo")
      USER_ID = str(message.author.id)
      todo.userExists(USER_ID)
      if msg.startswith(" tasks"):   
        embed = discord.Embed(
          title = "TO-DO",
          description = todo.outputTasks(USER_ID),
          colour = 9936031
        )
        
        await message.channel.send(embed=embed)
      elif msg.startswith(" add"):      
        msg = message.content.strip(" add")
        msg = str(message.content.replace("!todo add ",""))
        if msg == "":          
          embed = discord.Embed(
            title = "TO-DO",
            description = "Please Insert A Valid Task!",
            colour = 15158332
          )      
        else:
          todo.addTasks(USER_ID, msg)
          embed = discord.Embed(
            title = "TO-DO",
            description = "Task Added!",
            colour = 5763719
          )   
        await message.channel.send(embed=embed) 
      elif msg.startswith(" remove"):   
        num = str(message.content.replace("!todo remove ",""))
        if int(num) > 0:
          num = int(num)
          if (todo.removeTask(USER_ID,num)):
            embed = discord.Embed(
              title = "TO-DO",
              description = "Task Removed!",
              colour = 5763719
            )      
          else:
            embed = discord.Embed(
              title = "TO-DO",
              description = "Please Insert A Valid Number Index!",
              colour = 15158332
            )      
          await message.channel.send(embed=embed)     
        else:
          await message.channel.send("Please Insert A Valid Number!")        
      elif msg.startswith(" terminate history"):   
        todo.terminateHistory(USER_ID)      
        embed = discord.Embed(
          title = "TO-DO",
          description = "History Successfully Terminated!",
          colour = 5763719
        )      
        await message.channel.send(embed=embed)
      
      elif msg.startswith(" terminate"):   
        todo.terminateAllTasks(USER_ID)
        embed = discord.Embed(
          title = "TO-DO",
          description = "All Tasks Successfully Terminated!",
          colour = 5763719
        )      
        await message.channel.send(embed=embed)   
      elif msg.startswith(" history"):   
        embed = discord.Embed(
          title = "TO-DO",
          description = todo.outputHistory(USER_ID),
          colour = 9936031
        )
        
        await message.channel.send(embed=embed)

    
    elif user_input[0] == "!pmd":
      await pd.change_state(message.channel)

    
    elif user_input[0] == "!quote":
      embed = discord.Embed(
        title = "Motivational Quote",
        description = get_quote(),
        colour = 15844367
      )
      await message.channel.send(embed=embed)

    
    elif user_input[0] == "!gradecalculator":
      embed = discord.Embed(
        title = "Grade Calculator",
        description = gc.current_grade(user_input[1:]),
        colour = 15158332
      )
      await message.channel.send(embed=embed)

    
    elif user_input[0] == "!lifestyle":
      await ls.change_state(message.channel)

    
    else:
      embed = discord.Embed(
        title = "Invalid Input",
        description = "Try !help to find the list of commands",
        colour = 15158332
      )
      await message.channel.send(embed=embed)


Perpetual()
client.run(os.environ['Bookie-Secret'])