try:
  fhand = open(input("Enter the filename:")
  for line in fhand:
      line = line.rstrip()
      print(line.upper())
except:
  print("Check the extension or maybe the file doesn't exist!")
   
