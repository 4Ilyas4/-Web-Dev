def not_string(str):
  res = ""
  if(str[0:3].find("not")==-1):
    res = "not " + str
  elif(str.find("not")==0):
    res = str
  return res
    
