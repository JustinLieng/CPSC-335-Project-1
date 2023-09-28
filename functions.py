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