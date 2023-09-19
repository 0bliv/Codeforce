s = input()
if s and s != '{}':
   value = s.strip("{}").split(",")
   value = [element.strip() for element in value]
   Myset = set(value)
else:
   Myset = set()
print(len(Myset))
