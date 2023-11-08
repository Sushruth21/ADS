class minHeap:
    def __init__(self,lst=[]):
        self.data=lst
        self._buildHeap_()

    def isEmpty(self):
        return len(self.data)==0
    
    def getCount(self):
        return len(self.data)
    
    def _parent_(self,idx):
        return (idx-1)//2
    
    def _lchild(Self,idx):
        return (2*idx+1)
    
    def _rchild(self,idx):
        return (2*idx+2)
    
    def _swap_(self,i,j):
        self.data[i],self.data[j]=self.data[j],self.data[i]

    def _buildHeap_(self):
        length=len(self.data)
        start=(length-2)//2
        for idx in range(start,-1,-1):
            self._downHeap_(idx,length)

    def _downHeap_(self,idx,length):
        if(self._lchild(idx)<length):
            left=self._lchild(idx)
            bigChild=left
            if(self._rchild(idx)<length):
                right=self._rchild(idx)
                if(self.data[right]<self.data[left]):
                    bigChild=right
            if self.data[bigChild]<self.data[idx]:
                self._swap_(bigChild,idx)
                self._downHeap_(bigChild,length)

    def addElement(self,key):
        self.data.append(key)
        self._upHeap_(len(self.data)-1)
    
    def _upHeap_(self,j):
        parent=self._parent_(j)
        if(j>0 and self.data[j]<self.data[parent]):
            self._swap_(j,parent)
            self._upHeap_(parent)

    def getMinElement(self):
        return(self.data[0])
 
    def delete(self):
        self._swap_(0,len(self.data)-1)
        ele=self.data.pop()
        self._downHeap_(0,len(self.data)-1)
        return ele
    
    #testing the heap order property
    def testMAxHeap(self):
        if not self.isEmpty():
            for idx in range(len(self.data)-1,0,-1):
                assert(self.data[idx]>=self.data[self._parent_(idx)])

    #heap sort
    def heapSort(self):
        if not self.isEmpty():
            for i in range(len(self.data)-1,0,-1):
                self._swap_(0,i)
                self._downHeap_(0,i)
            return self.data


heap=minHeap()
heap.addElement(65)
heap.addElement(25)
heap.addElement(30)
heap.addElement(75)
heap.addElement(95)
heap.addElement(23)
heap.addElement(82)
heap.testMAxHeap()
assert(heap.getCount()==7)
assert(heap.getMinElement()==23)
assert(heap.delete()==23)
assert(heap.getMinElement()==25)
assert(heap.delete()==25)
assert(heap.getMinElement()==30)
assert(heap.heapSort()==([95,82,75, 65,30]))