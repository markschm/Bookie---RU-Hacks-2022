import json
    
#writes desired json file, takes in dictionary to be written and file name
def writeJson(dict, file):
  with open(file, "w") as outfile:
    json.dump(dict, outfile)  

#reads json file: output file name
def readJson(file):
  with open(file) as json_file:
      return json.load(json_file)

#
def outputTasks(id):
  data = readJson("tasks.json")
  if data[id] == None or data[id] == "":
    return "No Tasks Active!"
  
  output = ""
  iterator = 1
  for item in data[id]:
    output += str(iterator)+". " + item + "\n"
    iterator+=1
  if (len(output) == 0):
    return "No Tasks Active!\nTo get started use '!tasks add (*insert task*)'"
  return output

def outputHistory(id):
  data = readJson("deleted_tasks.json")
  if data[id] == None or data[id] == "":
    return "No History Available!"
  
  output = ""
  iterator = 1
  for item in data[id]:
    output += str(iterator)+". " + item + "\n"
    iterator+=1
  if (len(output) == 0):
    return "No History Available!"
  return output

#outputs new dictionary
def addTasks(id,newTask):
  data = readJson("tasks.json")
  tasks = data[id]
  if (tasks != None):
    tasks.append(newTask)
  elif (type(tasks) == type(None)):
    tasks = [newTask]    
  elif (len(tasks)>0):
    tasks.append(newTask)
  else:
    tasks = [newTask]
  data[id] = tasks
  
  writeJson(data, "tasks.json")

def addTasksToDelete(data,id,newTask):
  tasks = data[id]
  if (tasks != None):
    tasks.append(newTask)
  else:
    tasks = [newTask]
  data[id] = tasks
  
  writeJson(data, "tasks.json")

   
def removeTask(id,taskNum):
  data = readJson("tasks.json")
  taskNum=taskNum-1
  if (len(data[id])-1 >= taskNum):
    #remove task
    removedTask = data[id][taskNum]
    if taskNum == 0:
      data[id] = []
    else:
      del data[id][taskNum]
    
    #append to history
    delTasks = readJson('deleted_tasks.json') 
    addTasksToDelete(delTasks,id,removedTask)
    writeJson(delTasks,'deleted_tasks.json')
    
  else:    
    return False
  writeJson(data, "tasks.json")
  return True

#
def terminateAllTasks(id):
  data = readJson("tasks.json")
  data[id] = []
  writeJson(data, "tasks.json")
  

#
def terminateHistory(id):
  delTasks = readJson('deleted_tasks.json')
  delTasks[id] = []
  writeJson(delTasks,'deleted_tasks.json')
  
#check if user has made a task before

def userExists(userID):
  data = readJson("tasks.json")
  del_data = readJson("deleted_tasks.json")
  if not(userID in data) or not(userID in del_data):
    data.update({str(userID):""})
    data[str(userID)]  = None
    writeJson(data, "tasks.json")
    del_data.update({str(userID):""})
    del_data[str(userID)]  = None
    writeJson(del_data, "deleted_tasks.json")