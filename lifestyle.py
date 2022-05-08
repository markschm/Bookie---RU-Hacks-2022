import asyncio

class Lifestyle_Reminder:

  def __init__(self):
    self.is_on = False
    self.curr_channel = None
    self.standup_number = 0

    
# when called, will turn on if not on already, otherwise will turn off
  async def change_state(self, curr_channel):
    self.curr_channel = curr_channel

    if self.is_on:
      await self.end()
    else:
      await self.start()

  
  async def start(self):
    await self.curr_channel.send("Lifestyle Reminder is now On.")
    self.is_on = True
    await self.reminders()

  
  async def end(self):
    await self.curr_channel.send("Lifestyle Reminder is now Off.")
    self.is_on = False

  
  async def reminders(self):
    while self.is_on:
      await self.stand_up() # every 30 minutes
      await self.drink() # every 45 minutes
      
      if self.standup_number % 6 == 0:
        await self.touch_grass() # every while

  
  async def stand_up(self):
    self.standup_number += 1
    await asyncio.sleep(30 * 60) # 30 minutes
    if self.is_on:
      await self.curr_channel.send("Time to stand up! Stand up and move a little for a minute.")

  
  async def drink(self):
    await asyncio.sleep(15 * 60)
    if self.is_on:
      await self.curr_channel.send("Thirsty? Time to drink some water! Go get some water and stay hydrated.")

  
  async def touch_grass(self):
    if self.is_on:
      await self.curr_channel.send("It's been awhile. Let's not be an incel. Get up, walk away from your computer, go outside to touch some grass and appreciate nature for once.")
