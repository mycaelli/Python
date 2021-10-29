class Node: 
    def __init__(self, data=None, next=None):
        #Node represents an element in the list
        #data -> values of the list 
        #next -> pointer to the next element
        self.data = data
        self.next = next

class LinkedList: 
    def __init__(self):
        self.head = None
    
    def insert_at_beggining(self, data):
        #the node is the first element
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        #checks if the list is empty
        if self.head is None:
            print("Empty linked list")
        
        #llstr -> to print the elements in the list
        itr = self.head 
        llstr = ''
        while itr : 
            llstr += str(itr.data) + "-->"
            itr = itr.next
        
        print(llstr)
        #print("head: " + self.head.data)
    
    def insert_at_end(self, data):
        #if list is empty creates a node that points to none 
        if self.head is None :
            self.head = Node(data, None)
            return

        itr = self.head
        #while there is value in 'next' it is not in the end
        while itr.next :
            itr = itr.next
        
        #itr now has the last value
        #the last node (itr) will point to the new node being created 
        itr.next = Node(data, None)
    
    def insert_values(self, data_list):
        #input: list o values 
        #output: new linked list with the values 
        
        #deletes all the current values (garbage collector)
        if self.head is not None :
            self.head = None
        
        for data in data_list:
            self.insert_at_end(data)
        
    def get_length(self):
        #returns the length of the list
        count = 0
        itr = self.head
        
        while itr :
            count += 1
            itr = itr.next
        
        return count

    def remove_at(self, index):
        #remove node at index
        if index < 0 or index >= self.get_length() :
            raise Exception("Invalid index")
        

        #first position 
        if index == 0 :
            self.head = self.head.next #head will become the second node
            return
        
        count = 0
        itr = self.head
        while itr :
            #when itr gets to the node before the one that will be removed
            if count == index - 1 :
                #itr will point to the element that the node being removed points
                itr.next == itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        #invalid index
        if index < 0 or index >= self.get_length() :
            raise Exception("Invalid index")
        
        #insert at first pos O(1)
        if index == 0 : 
            self.insert_at_beggining(data)
            return
        
        #insert at index position 
        count = 0
        itr = self.head    
        while itr :
            if count == index - 1 :
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next 
            count += 1
    
    #checks if a value is on the list
    def check_value(self, data):        
        itr = self.head
        
        while itr :
            if data == itr.data :
                return True
            itr = itr.next
            
        return False
    
    
    #if list is not None inserts a node after the 'data_after' node
    def insert_after_value(self, data_after, data_to_insert):
        
        if self.head is None :
            return
        
        if self.check_value(data_after) :
            itr = self.head 
            while itr :
                if itr.data == data_after :
                    itr.next = Node(data_to_insert, itr.next)
                    break
                itr = itr.next
    
    #if list is not None removes the node by its value
    def remove_by_value(self, data):
        
        if self.head is None :
            return
        
        if self.check_value(data) :
            #removes first element
            if self.head.data == data :
                self.head = self.head.next
                return
            
            #removes other positions
            itr = self.head
            while itr :
                if itr.next.data == data:
                    itr.next = itr.next.next
                    return
                itr = itr.next
                    
        
#main function??
if __name__ == '__main__' :
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("banana","apple") # insert apple after mango
    ll.print()
