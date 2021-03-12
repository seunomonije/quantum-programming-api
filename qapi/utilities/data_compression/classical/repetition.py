import os
import pickle

#  NOTES:
#  CREATE A MAP that INDEXES EACH CHARCTER'S POSITION, store the map, then rearrange the file

class IndexFrequencyPair():
  def __init__(self, frequency, index):
    self.frequency = frequency
    self.indexes = []

class RepetitionCompression():
  def __init__(self, file_path):
    self.file_path = file_path

  def compress(self):
    indexDict = {}
    filename, file_extension = os.path.splitext(self.file_path)
    output_path = filename + '.bin'

    with open(self.file_path, 'r+') as file, open(output_path, 'wb') as output:
      text = file.read().rstrip()

      for i in range(len(text) - 1):
        currentLetter = text[i]
        indexDict[currentLetter] = IndexFrequencyPair(0, [])

      for i in range(len(text) -1):
        currentLetter = text[i]
        indexDict[currentLetter].frequency += 1
        indexDict[currentLetter].indexes.append(i)

      pickle.dump(indexDict, output)

    # print(text)
    # print(len(text))
    # print(text.index('i'))
  
def main():
  path = './repetition.txt'
  R = RepetitionCompression(path)
  R.compress()

  
  return

if __name__ == '__main__':
  main()

