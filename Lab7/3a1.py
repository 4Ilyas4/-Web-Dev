def sleep_in(weekday, vacation):
  res = weekday and vacation
  if(weekday and vacation==False):
    res = False
  elif(weekday==False and vacation):
    res = True
  if(weekday==False and vacation==False):
    res = True
  return res