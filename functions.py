def convertTimeToMinutes(time):
  hours, minutes = time.split(":")
  return int(hours) * 60 + int(minutes)