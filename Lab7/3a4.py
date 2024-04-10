def front_back(str):
  res = str
  if(len(str)>1):
    res = str[-1] + str[1:-1] + str[0]
  return res

front_back(input())