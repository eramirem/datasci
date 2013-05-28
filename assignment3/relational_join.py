import MapReduce
import sys
import itertools

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(bag):
    # key: document identifier
    # value: document contents
    key = bag[1]
    mr.emit_intermediate(key, bag)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print list_of_values
    output_list = [] 
    for v in itertools.product(list_of_values[0:1], list_of_values[1:]):
      output_list = v[0] + v[1]
      mr.emit(output_list)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
