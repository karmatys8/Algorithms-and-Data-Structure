class QuickMedian:
  def __init__(self, array) -> None:
    self.array = array
    self.heap_sort()
    
    ln = len(self.array)
    self.smaller = array[0: (ln-1)//2]
    self.median = array[(ln-1)//2: ln//2 +1]
    self.bigger = array[ln//2 +1: ln]
    
    self.build_heap(self.smaller, True)
    self.build_heap(self.bigger, False)
  
  
  def heapify(self, array, i, ln, greater):
    max_i = i
    
    l = 2*i + 1
    r = l + 1
    
    if l < ln  and  (greater == (array[l] > array[max_i])):
      max_i = l
    if r < ln  and  (greater == (array[r] > array[max_i])):
      max_i = r
      
    if max_i != i:
      array[i], array[max_i] = array[max_i], array[i]
      self.heapify(array, max_i, ln, greater)
      
  
  def heap_insert(self, array, v, greater):
    i = len(array)
    array.append(v)
    
    while i > 0  and  (greater == (array[i] > array[(i-1)//2])):
      array[i], array[(i-1)//2] = array[(i-1)//2], array[i]
      
      i//=2
    
    if greater == (array[1] > array[0]):
      array[1], array[0] = array[0], array[1]
  
  
  def build_heap(self, array, greater):
    ln = len(array)
    for i in range(ln//2-1, -1, -1):
      self.heapify(array, i, ln, greater)
  
  
  def heap_sort(self):
    self.build_heap(self.array, True)
    
    for i in range(len(self.array)-1, 0, -1):
      self.array[i], self.array[0] = self.array[0], self.array[i]
      self.heapify(self.array, 0, i, True)
  
  
  def insert(self, v):
    if len(self.median) == 1:
      if self.median[0] == v:
        self.median.append(v)
        
      elif v > self.median[0]:
        self.median.append(self.bigger[0])
        self.bigger[0] = v
        self.heapify(self.bigger, 0, len(self.bigger), False)
        
      else:
        self.median.append(self.smaller[0])
        self.smaller[0] = v
        self.heapify(self.smaller, 0, len(self.smaller), True)
        
    else:
      if self.median[0] + self.median[1] == 2 * v:
        self.heap_insert(self.smaller, self.median[0], True)
        self.heap_insert(self.bigger, self.median[1], False)
        
        self.median = [v]
        
      elif self.median[0] + self.median[1] > 2 * v:
        self.heap_insert(self.smaller, v, True)
        self.heap_insert(self.bigger, self.median[1], False)
        
        self.median.pop()
        
      else:
        self.heap_insert(self.smaller, self.smaller[0], True)
        self.heap_insert(self.bigger, v, False)
        
        self.median.pop(0)
        
  
  
  def extract_median(self):
    if len(self.median) == 0:
      return "ERROR: Array is empty"
    
    v = self.median[0]
    try:
      v += self.median[1]
      v /= 2
    except:
      pass
    
    try:
      self.median[0] = self.smaller[0]
      self.median[1] = self.bigger[0]
    except:
      self.median = []
    
    if len(self.smaller) > 1:
      self.smaller[0] = self.smaller.pop()
      self.heapify(self.smaller, 0, len(self.smaller), True)
    else:
      self.smaller = []
    
    if len(self.bigger) > 1:
      self.bigger[0] = self.bigger.pop()
      self.heapify(self.bigger, 0, len(self.bigger), False)
    else:
      self.smaller = []
    
    return v
