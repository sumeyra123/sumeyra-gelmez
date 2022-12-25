# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 10:29:54 2022

@author: Sümeyra Nihal GELMEZ
"""

Class Bag:#depolama alanı tanımlama.
   def _init_(self):
       self._storage=list()
   def _len_(self):#liste uzunluğu int olarak 
           return len(self.storage)döndürür
   def _contains_(self,item):içerip içermediğini denetler boolean değer döndürür.
              retrun item in self._storage
   def add (self,item):#depolamaya ddeğişken ekler.
            self._storage.append(item) 
   def remove (self,index) #depolamadan değişken ekler
               self._storage.append(item)
               
               
   def y contain(self,aranan)#_contain_aynı işlevdeki farklı şekilde kullanımı
           karar=0
           for item in self._storage:
               if item ==aranan:
                   karar=1
                   break
                return karar !=0
    def _iter_(self):
         self.yedek=bagA1
         self.sayaç=0#depolama içerisindeki değişkenleri liste olarak çekiyoruz for döngüsü her
döndüğünde bir sonraki değişkeni çekiyoruz.

   def _next_(self):
     if self.sayac <len(self.yedek):
         item=self.yedek[self.sayaç]
         self.sayaç+=1
           return item
    else:
        raise StopIteration #for döngüsünü durduran exception
        
        
Bag1=Bag()
#oluşturduğumuz class içerisindeki ekleme metodunu kullanarak depoya(_storage)eleman ekleme
bag1.add(10)
bag1.add(20)
bag1.add(33)
bag1.add(89),
#oluşturduğumuz class içerisndeki remove metodunu kullanarak depodan(_storage eleman silme)

bag1.remove(0)
bag1remove(1)
#aynı işi yapan farklı yazım şekilleri

    print(33 in bag 1)
    print(bag1.yContain(33))
    print(0 in bag1)#0 depolamada yok bu yüzden false döndürecek
    print(bag1.ycontain(0))
#iter metodu for iler kullanıyoruz.
        for al in bag1:
            print(a)
*Myrange =iter(range(10))
print(next(myrange))
print(next(myrange))
=Arrays=


*tek boyutlu bir dizi için bir dizi ve yapısı ardından bunu 2 boyutlu bir dizi için bir dizi yapısı ve ardından bunu 
2 boyutlu bir diziyi ve ilgili matrıs yapısını uygulamak için kullanın.
**donanım düzeyinde,çoğu bilgısayar mimarisi ,tek boyutlu diziler oluşturmak için bir mekanizma sağlar.şekildeki gösterildiği gibi tek boyutlu bir dizi bitişik bellek boyutların
depolanan çoktu sıralı öğelerden oluşur ve  bireysel öğelere rastgele erişime  izin verir.
Array(size):Boyut öğelerinden oluşan tek boyutlu bir dizi oluştururher öğe başlangiçta yok olarak ayarlanır.Boyut 0 büyük olmalıdır.
Length():Dizideki öğelerin uzunluğuna veya sayısını döndürür.
getitem(index):Öğe konumunda dizide depolanan değeri döndürür.Dizin bağimsiz değişkeni geçerli aralık içinde olmalıdır.Alt simge öperatörü kullanılarak erişilir.
setitem(index,value):
clearing(value):
iterator():Dizinin öğelerini geçmek için kullanılabilecek bir yineleyic, oluşturu ve döndürür.
from array İmport Array 
import random
ValueList=Array[10000]
for i in range (len(Valuelist)):
        ValueList[i]=random.random()
for value in ValueList:
       print(value)
from Array İmport Array 
#sayaçlar için bir dizi oluşturan ve her öğeyi 0 
theCounters=Array(127)
theCounters.clear(0)
#•metin dosyalama okumak için açın ve her satırı dosyadan çıkarın ve satırdaki her karakter üzerinden yineleme yapın.T
TheFile=open("atextfile.txt,""r")
dosyadaki satır için satırdaki mektup için 
for line in theFile:
  for letter in line:
  theCounters[code]+=1
theFile.close()


The ctypes module:
Bu mödül,c dilinde mevcut olan çeşitli veri türlerine ve çok çeşitli c kitaplıklar tarafından sağlanan eksiksiz işlevselliğe erişim sağlar.
Ctypes modulu ,tıpkı python'un string,list,tuple ve sözlük koleksiyon türlerini uygulamak için kullanılanlar gibi donanım destekli diziler yaratma yeteneği sağlar '
ancak ctpes modülü pthon'da günlük kullanımiçin tasarlanmıştır'
import ctypes 
ArrayType=ctypes.py_object*5
slots=ArrayType()
print(slots[0])
for i in range (5):
slots[i]=None          
        diziden bir öğeyi çıkarmak için ,karşılık gelen öğeyi yok olarak ayarladık.
=Dizinin boyutu asla değişmez ,bu nedenle diziden bir öğeyi çıkarmak dizinin boyutu veya diğer öğelerle depolanan öğeler üzerinde hiçbir etkisi yoktur.Dizi ,ekleme veya ekleme gibi liste tipi işlemlerinden hiçbirini sağlamaz öğeleri patlama ,belirli bir öğeyi arama veya  öğeleri sıralama.
böyle bir işlem, bir dizi ile kullanmak için gerekli kodu kendiniz sağlamanız gerekir.
import ctypes

class Array:
    #creates an array with size elements
def _init_(self,size):
       assert size >0,"array size must be >0"
       self._size=size 
       #create the array structure using the ctypes modul
       Pyarraytype=ctypes.py.object*size
       self._elements=PyArrayType()
       #Inıtalize each element
       self.clear(None)
       #Returns the size of the array.
       def _len_(self):
           return self._size
       #gets the contents of the index element
       def _getitem_(self,index):
           assert index >=0 o and index <len(self) "Array subcript out of range"
           return self._elements[index]
       #puts the value in the array element at index position.
       def_setitem_(self,index,value):
           assert.index>=0 and index<len(self)
           self._elements[index]=value
 #Returns the array's iterator for traversing the elements.
def_iter_(self):
       return_ArrayIteartor(self.elements)

class_ArrayIterator:
    def_init_(self,the Array):
       self._arrayRef=theArray
       self._curNdx=0
def_iter_(self):
     return self 
def_next_(self):
      if self ._curndx< len(self._arrayRef):
           entry=self._arrayRef[self._curNdx]
           self._curNdx+=1
           return entry
       
        else:
            raise StopIteration.
        
  Searcging and Sorting
def selectionSort(aList):
      for i in range (Len(alist)):
          least=i
          for k in range (i+1,len(alist)):
              if a list[k]<a list[least]:
                  Least=k
                  swap(aList,Least)
def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp
selectionSort(my_list)
print(my_list)
                     LİNEAR SEARCH ALG.
def linearSearch(item,my_list):
       found=False
       position=0
       while position <len(my_list) and not found:
           if my_list [position]==item:
               found=True
        position=position+1
      return found 
  
    
  
def selectionSort(array):
       for i in range (len(array)-1,0,1):
           max_poisition=0
           for k in range (1,i+1):
               if array[k]>array[Max_position]:
                   max_position=k
          temp=array[i]
          array[i]=array[max_poisition]
          array[max_poisition]=temp
array=[14,66,193,137,3,4,50,19]
selectionSort(array) 
               ----BUBLE SORT----
+Bazen batan sıralama olarak adlandırılan kalarak,sıralanacak listede tekrar tekrar adım ilerleyen ,her bir bitişik öğe çiftini karşişlaştıran ve yanlış sıradaysa
bunları değiştiren basit bie sıralama algoritmasıdır.Listeden geçiş,takas gerekmeyince kadar tekrarlanır,bu da listenin sıralandiğini gösterir.Bu karşilaştırma türü olan algoritmasıdır
daha küçük öğelerin listenin en üstüne "kabarcık" girme şeklinden dolayı adlandırılmıştır.Algoritma basit olmasına rağmen,ekleme sıralamasıyla kıyasla bile çoğu problem için çok yavaş ve pratik değildir.Girdi genellikle sıralam düzenindeyse ancak bazen neredeyse konumdaki bazı sıradışşı öğelere sahip olabilirse pratik olabilir.
  def bubbleSort(nList):
      for passnum in range (len(nlist),-1,0,1)
          for  i in range(passnum):
              if nlist[i]>nlist[i+1]:
                  temp=nlist[i]
                  nlist[i]=nlist[i+1]
                  nlist[i+1]=temp
n list =[14,46,43,27,57,41,45,21,70]     
bubbleSort(nlist)
print(nlist)
def time_sort(list):
    runs,sorted_runs=[],[]
    lenght=len(list)
    new_run=[list[0]]
    sorted_array=[]
#ımplementation of insertion sort algorithm 
#ekleme sıralama algoritmasını kullanarak bir diziyi artan düzeyde sıralar.
def time_sort(list):
      runs,sorted_runs =[],[]           
              ımplementation of insertion sort algorithm.
              #ekleme sıralama algoritmasını kullanarak bir diziyi artan düzende sıralar.
              
              
              def insertionSort(theSeq):
                  n=len(theSeq)
                  #Sıralanan tek girişle olarak öğeyle başlar.
                     for i in range (1,n):
                         value=theSeqy[i]
                         pos=i
                         while pos > 0 and value<theSeq[pos-1]:
                             pos-=1
                     theSeq[pos]=value        
              
              
#merging two sorted lists#
merges two sorted lists to create and return a new sorted list.
def mergeSorted(listA,listB):
   newList=list()
a=0
b=0#merge the 2 lists together until are is empty.
while a<len(listA) and <listB[b]:
       newlist.append(ListA[b])
b+=1
#if list a contins more items ,append them to newlist.
     while a<len(ListA):
         newlist.append(listA[a])
         a+=1
         #or if ListB contains more items,append them to newlist.
         while b<len(ListB):
             newlist.append(listB[b])
             b+=1
         return newlist
     #How to create a linked list in python
#düğümler bağlantılı bir listenin yapı taşalrı olduğundan önce ,bir düğün oluşturacağız.
class ListNode:
    def_init_(self,data):
        self.data=data
a=listNode(11)
b=ListNode(52)
c=ListNode(18)
class ListNode:
      def_init_(self,data):
             self.data=data
             self.next=none
print(a.data)
print(a.next.data)
print(a.next.next.data)


Traversing a linked list 
    def traversal(head):
         curNode=head
         while curNode is not None:
             print curNode.data
             curNode=CurNode.next
Searching a linked list :
   def unorderedsearch(head,target):
       curNode=head
       while curNode is not None and curNode.data !=:
             curNode=curNode.next 
             return curNode is not None 
         
prepending a node to the linked list .
preNode=None 
car Node=head 
while curNode is not NOne and curNode.data!=target           
         preNode=curNode 
         curNode=curNode.next 
if curNode is not None: 
    if curNode is head:
            head=curNode.next 
            
            
    else:
             preNode.next=curNode.next 
#Implements the Bag adt using a singly linked list.
classBag:
    #constructs on empty bag.
def_init_(self):
      self._head=None 
      sels._size=0
#returns the number of items in the bag.
def_len_(self):
    retrun self._size 
#Determines if an item is contained in the bag.

def _contains_(self,target):
     curNode=self._head
     while curNode is not Nonre and curNode.item target !=
             curNode=curNode.next 
            return curNode is not None 
#adds a new item to the bag.
     def _add_(self,item):
           newNode=_BaglistNode(item)
           newNode.next=self._head 
           self._head=newNode 
           self._size+=1 
#removes an instance of the item from the bag.
def remove (self,item):
   predNode=None 
   curNode=self._head 
while curNode is not none and curNode.item !=item:
        predNode=curNode 
        curNode=curNode.next 
#The item has to be in the bag to remove it assert curNode is not none  "the item must be in the bag"
self._size-=1
if curNode is head :
        self._head=curNode.next 
else:
         preNode.next=curNode.next 
   return curNode.item 
#returns an iteration for traversing the list of the items.
     def _iter_(self):
         return_BagIterator(self._head)
#defines a private storage class for creating list nodes.
class_BagListNode(object):
        def_init_(self,item):
            self.item=item
            self.next=None
An iterator for the Bag class implemented using a linked list. 
#defines alinked list iterator for the bag adt.
class_BagIterator:
    def_init_(self,listHead):
        self._curNode=listHead
    def_iter_(self):
        return self 
    def next(self):
        if self._curNode is None:
            raise StopIteartion 
        else:
            item=self._curNode.item 
            self._curNode =self._curNode.next
                   retrun item 
#bir kuyruk referansı kullanarak bağlantılı bir listeye bir düğüm ekleme 
#Baş kuyruk işaretçileri verildiğinde ,bağlantılı bir listeye bir öğe ekler.

newNode=ListNode(item) 
if head is none :
         head=newNode 
else:
          tail.next=newNode 
          tail=newNode 
          
        
removing a node from a linked list using a tail reference.
#given the head and tail references ,removes a target from a linked list. 
   predNode=None 
   curNode=head 
while curNode is not none and curNode.data!=target:
            predNode=curNode 
            curNode=curNode.next 
if curNode is not None: 
       if curNode is head:
else: 
       predNode.next=curNode.next 
if curNode is tail:
           tail=predNode 
Searching a sorted linked list.
 def sortedSearch(head,target):
        curNode=head 
        while curNode is not None and curNode.data<target:
                 if  curNode.data==target:
                     return True 
                 else:
                     curNode=node.next 
                   return False
sıralanmiş bir listeye değer elkleme 
#baş işaretçisi varildiğinde ,sıralanmış bağlantılı bir listeye bir değer ekleyin
#yeni değer için eklem noktasını bulun.

predNode=None 
curNode=head 
while curNode is not None and value > curNode.data:
        predNode=curNode
        curNode=curNode.next 
#create the new node for the new value .
newNode=ListNode(value),
    #link the new node into the list 
if curNode is head:
       head=newNode 
else:
       predNode.next=newNode        
          
                        