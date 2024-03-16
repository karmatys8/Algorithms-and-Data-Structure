'''
Task: Implement data structure from which you can extract min, max in log.
      Insert should also be in log.
'''



import copy

class QuickMinAndMax:
  def __init__(self, array):
    self.minHeap = copy.copy(array)
    
    for i in range(len(array)):
      self.minHeap[i] = (self.minHeap[i], -1)
      
    self.maxHeap = copy.deepcopy(self.minHeap)
    
    self.build_heap(self.minHeap, self.maxHeap, False)
    self.build_heap(self.maxHeap, self.minHeap, True)
    
    for i in range(len(array)):
      for j in range(len(array)):
        if self.minHeap[j][1] == -1  and  self.maxHeap[i][0] == self.minHeap[j][0]:
          self.maxHeap[i], self.minHeap[j] = (self.maxHeap[i][0], j), (self.minHeap[j][0], i)
          break
      
  
  def heapify(self, array, sup_array, i, ln, greater):
    max_i = i
    
    l = 2*i + 1
    r = l + 1
    
    if l < ln  and  (greater == (array[l][0] > array[max_i][0])):
      max_i = l
    if r < ln  and  (greater == (array[r][0] > array[max_i][0])):
      max_i = r
        
    if max_i != i:
      print(array[i], sup_array[array[i][1]], array[max_i], sup_array[array[max_i][1]])
      array[i], sup_array[array[i][1]], array[max_i], sup_array[array[max_i][1]] = array[max_i], (sup_array[array[i][1]][0], max_i), array[i], (sup_array[array[max_i][1]][0], i)
      self.heapify(array, sup_array, max_i, ln, greater) #issue is that I also have to change indexes in 2nd array
      
  
  def heap_insert(self, array, v, greater):
    i = len(array)
    array.append((v, -1))
    
    while i > 0  and  (greater == (array[i][0] > array[(i-1)//2][0])):
      array[i], array[(i-1)//2] = array[(i-1)//2], array[i]
      
      i//=2
    
    if greater == (array[1][0] > array[0]):
      array[1], array[0] = array[0], array[1]
      i = 0
      
    return i
  
  
  def build_heap(self, array, sup_array, greater):
    ln = len(array)
    for i in range(ln//2-1, -1, -1):
      self.heapify(array, sup_array, i, ln, greater)
      
  
  def extract(self, greatest):
    if greatest:
      array1 = self.maxHeap
      array2 = self.minHeap
    else:
      array1 = self.minHeap
      array2 = self.maxHeap
    
    
    res = array1[0]
    array1[0] = array1[-1]
    array1.pop()
    self.heapify(array1, array2, 0, len(array1), greatest)
    
    array2[res[1]] = array2[-1]
    array2.pop()
    self.heapify(array2, array1, res[1], len(array2), not greatest)
    
    return res[0]
  
  
  def insert(self, v):
    in_max = self.heap_insert(self.maxHeap, v, True)
    in_min = self.heap_insert(self.minHeap, v, False)
    
    self.maxHeap[in_max], self.minHeap[in_min] = (self.maxHeap[in_max], in_min), (self.minHeap[in_min], in_max)
