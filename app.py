def main():
  contents = ""
  try:
     with open('./input/inputfile.txt', 'r') as inputfile:
        contents = inputfile.read()
  except IOError:
     print('Input file not found')

  try:
     with open('./output/outputfile.txt', 'w+') as outputfile:
        outputfile.write(contents)
        for item in range(0,5):
           outputfile.write('\nText is copied from input/file.txt and \
              pasted to a new file output/file.txt along with these 5 new lines.')
     print('A new file is created successfully in ./output directory')

  except:
     print('Output file cannot be written')


if __name__ == '__main__':
   main()