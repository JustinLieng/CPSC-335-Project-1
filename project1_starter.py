import ast

def convertTimeToMinutes(time):
  hours, minutes = time.split(":")
  return int(hours) * 60 + int(minutes)

# Combines the two people's dailyActive. This gets the greater time of the 0th index of
# both AND gets the lower time of the 1st index of both.
def combineDailyActive(person1_dailyActive, person2_dailyActive, dailyActive):
  p1Lower = convertTimeToMinutes(person1_dailyActive[0])
  p2Lower = convertTimeToMinutes(person2_dailyActive[0])
  p1Upper = convertTimeToMinutes(person1_dailyActive[1])
  p2Upper = convertTimeToMinutes(person2_dailyActive[1])
  if (p1Lower > p2Lower):
    dailyActive.append(person1_dailyActive[0])
  elif (p2Lower > p1Lower):
    dailyActive.append(person2_dailyActive[0])
  elif (p1Lower == p2Lower):
    dailyActive.append(person1_dailyActive[0])

  if (p1Upper < p2Upper):
    dailyActive.append(person1_dailyActive[1])
  elif (p2Upper < p1Upper):
    dailyActive.append(person2_dailyActive[1])
  elif (p1Upper == p2Upper):
    dailyActive.append(person1_dailyActive[1])

def scheduleMeeting(person1_schedule, person2_schedule, dailyActive,
                    meeting_duration, available_times):
  earliest = convertTimeToMinutes(dailyActive[0])
  latest = convertTimeToMinutes(dailyActive[1])
  # Combines both schedules into one big schedule. Still trying to figure out how to sort this.
  schedule_string = person1_schedule + person2_schedule
  
  # Each iteration grabs the [i][0] time of the current object, and the [i+1][1] time of the next object.
  end_time = earliest
  end_time_string = dailyActive[0]
  start_time = convertTimeToMinutes(schedule_string[0][0])
  start_time_string = schedule_string[0][0]

  time_difference = start_time - end_time
  if time_difference >= meeting_duration:
    available_times.append([end_time_string, start_time_string])

  for i in range(len(schedule_string)):
    end_time = convertTimeToMinutes(schedule_string[i][1])
    end_time_string = schedule_string[i][1]

    # if i is on the last iteration, then start_time = latest
    if i >= len(schedule_string) - 1:
      start_time = latest
      start_time_string = dailyActive[1]
    else:
      start_time = convertTimeToMinutes(schedule_string[i + 1][0])
      start_time_string = schedule_string[i + 1][0]

    time_difference = start_time - end_time

    if time_difference >= meeting_duration:
      available_times.append([end_time_string, start_time_string])

# Declare variables first before initializing them to each line in input.txt
var1 = []
var2 = []
var3 = []
var4 = []
var5 = 0
dailyActive = []
available_times = []

# Open the input.txt file
with open(
    "input.txt") as file:  # Initialize each line in input.txt to var1-var5
  x = 1
  testCaseCount = 1
  
  # Clear the output.txt file
  with open("output.txt", 'w') as outputFile:
    outputFile.write("== Available Times ==\n")
    
  for line in file:
    if line == "\n":
      x = 1
      continue
    exec(f'var{x} = line')
    
    if x % 5 == 0:
      # Copy var1-var5 to descriptive variable names.
      # The ast functions are to convert from string to a list.
      person1_schedule = ast.literal_eval(str(var1))
      person1_dailyActive = ast.literal_eval(str(var2))
      person2_schedule = ast.literal_eval(str(var3))
      person2_dailyActive = ast.literal_eval(str(var4))
      meeting_duration = ast.literal_eval(str(var5))
      combineDailyActive(person1_dailyActive, person2_dailyActive, dailyActive)
      scheduleMeeting(person1_schedule, person2_schedule, dailyActive,
                      meeting_duration, available_times)
      
      # Append the available_times to the output.txt file
      with open("output.txt", 'a') as outputFile:
        outputFile.write("Test Case: {}\n".format(testCaseCount) + str(available_times) + "\n")

      # Empty out the variables we created in order to overwrite them with new schedules and data.
      var1 = []
      var2 = []
      var3 = []
      var4 = []
      var5 = 0
      dailyActive = []
      available_times = []
      person1_schedule = ast.literal_eval(str(var1))
      person1_dailyActive = ast.literal_eval(str(var2))
      person2_schedule = ast.literal_eval(str(var3))
      person2_dailyActive = ast.literal_eval(str(var4))
      meeting_duration = ast.literal_eval(str(var5))
      testCaseCount += 1
      x = 1
      continue
    x += 1