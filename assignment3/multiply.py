import MapReduce
import sys
import itertools

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
L, N = 5, 5

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents  
    matrix = record[0]
    for i in range(0, L):
      if matrix == 'a':
        key = (record[1], i)
        value = (record[2], record[3])
        mr.emit_intermediate(key, value)
      else:
        key = (i, record[2])
        value = (record[1], record[3])
        mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    result = 0
    for i in range(0, L):
      pair = []
      for index, v in list_of_values:
        if index == i:
          pair.append(v)
      if len(pair) > 1:
        result += reduce(lambda x, y: x*y, pair)
    mr.emit((key[0], key[1], result))
    
      #for v in list_of_values:
      #  if v[0] == i:
      #    pair.append(v[1])
      #print pair
      #if len(pair) == 2:
      #  result += pair[0] * pair[1]
    #mr.emit((key[0], key[1], result))
        



    # key: word
    # value: list of occurrence counts
    
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
