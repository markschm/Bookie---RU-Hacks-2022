def get_help_message():
  help_string = """
  !todo - Personal todo list
  !pmd - Pomodoro Timer
  !quote - Get a motivational quote
  !gradecalculator - Calculate current grade in a class
  !lifestyle - Healthy studying reminders 
  ---------------------------
  use !help (command name) to get help with a specific function
  """
  
  return help_string


def get_pmd_help():
  help_string = """
  Pomodoro Timer Help:
    - Toggle Pomodoro Timer - !pmd
    - Sets a timer for 25 minutes of work then 5 minutes of break
  """
  return help_string

  
def get_todo_help():
  help_string = """
  Todo List Help:
    - To print the current todo list - !todo tasks
    - To print your history - !todo history
    - To add a task to the list - !todo add (task description/name)
    - To remove/complete a task - !todo remove (task number)
    - To remove all tasks - !todo terminate
    - To remove history - !todo terminate history
  """

  return help_string


def get_grade_calculator():
  help_string = """
  Grade Calculator Help:
    - To calculate your grade use !gradecalculator
    - Then after the command type your grades and weight separated by spaces
    - ex. -> !gradecalculator 90 20 82 15
  """
  return help_string


def get_lifestyle_help():
  help_string = """
  Lifestyle Reminder Help:
    - Turn on lifestyle reminder - !lifestyle
    - Reminds you to stand up, take breaks, touch grass, drink water etc.
  """
  return help_string
