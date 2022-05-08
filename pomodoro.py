import asyncio

class Pomodoro:

  def __init__(self):
    self.is_on = False
    self.breaks_taken = 0
    self.curr_channel = None
    self.is_working = False

  
  async def change_state(self, curr_channel):
    self.curr_channel = curr_channel

    if self.is_on:
      await self.end()
    else:
      await self.start()

  
  async def start(self):
    await self.curr_channel.send("Pomodoro Timer is now On.")
    self.is_on = True
    await self.work()

  
  async def end(self):
    await self.curr_channel.send("Pomodoro Timer is now Off.")
    self.is_on = False
    self.breaks_taken = 0
    self.is_working = False

  
  async def work(self):
    if self.is_on:
      await self.message_user()
      self.is_working = True
      await asyncio.sleep(25 * 60) #25 minutes
      await self.take_break()

  
  async def take_break(self):
    if self.breaks_taken > 20:
      await self.curr_channel.send("Timer max length exceeded")
      await self.curr_channel.send("To use the pomodoro timer again use the command")
      self.end()

    elif self.is_on:
      await self.message_user()
      self.is_working = False
      await asyncio.sleep(5 * 60) #5 minutes 
      await self.work()

  
  async def message_user(self):
    if self.is_working:
      await self.curr_channel.send("Time for a Break!")
      await self.curr_channel.send("Go walk around or stretch your eyes")
      
    else:
      await self.curr_channel.send("Time to get back to Work!")
      