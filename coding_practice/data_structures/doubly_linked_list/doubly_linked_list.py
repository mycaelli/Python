class Node:
    def __init__ (self, data=None, next=None, prev=None) :
        self.data = data
        self.next = next
        self.prev = prev
    
class Doubly_linked_list:
    def __init__ (self) :
        self.head = None
        self.tail = None
        
    def get_length(self) :
        count = 0
        itr = self.head
        
        while itr :
            count += 1
            itr = itr.next
                 
        return count
    
    def insert_at_beggining (self, data) :
        node = Node(data, self.head)
              
        node.next = self.head
        
        #empty list
        if self.head is None :
            self.tail = node
        
        else :
            self.head.prev = node
        
        self.head = node
        
    
    def print_forward (self) :
        if self.head is None :
            print("Empty list")
        
        itr = self.head
        dlstr = ""
        while itr :
            dlstr += str(itr.data) + "-->"
            itr = itr.next
        
        print(dlstr)
        
    
    def print_backward(self) :
        if self.head is None : 
            print("Empty list")
        
        itr = self.tail 
        dlstr = ""
        while itr :
            dlstr += str(itr.data) + "-->"
            itr = itr.prev
        
        print(dlstr)
        
    
    def insert_at_end (self, data) :
        if self.head is None :
            self.head = Node(data, None, None)
            return

        itr = self.head 
        while itr.next :
            itr = itr.next
            
        itr.next = Node(data, None, itr)
        self.tail = itr.next
        
    
    def insert_values (self, data_list) :
        if self.head is not None :
            self.head = None
        
        for data in data_list :
            self.insert_at_end(data)
    
    
    def remove_at(self, index) :
        """ 
            removes node at given index
            input: int(index)
            return: - 
        """
        
        if index < 0 or index >= self.get_length() :
            raise Exception("Invalid index")
        
        if index == 0 :
            self.head.next.prev = None
            self.head = self.head.next
            return
           # self.head.prev = None
        
        if index == self.get_length() - 1 :
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return 
        
        count = 0
        itr = self.head
        while itr :
            if count == index - 1 :
                itr.next.next.prev = itr
                itr.next = itr.next.next
                #itr.next.next.prev = itr
                break
            count += 1
            itr = itr.next
            
    def insert_at(self, index, data):
        """
        inserts node at given index
        input: int(index), anyType(data)
        return: -
        """
        
        if index < 0 or index >= self.get_length() :
            raise Exception ("Invalid Index")
 
        #O(1)
        if index == 0 :
            self.insert_at_beggining(data)
            return
        
        #O(1)
        if index == self.get_length() - 1 :
            self.insert_at_end(data)
            return
        
        #O(n)
        count = 0
        itr = self.head
        while itr :
            if count == index - 1 :
                node = Node(data, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
        
    
    def check_value(self, data):
        """
        checks if the data exists in the list 
        input: anytype(data)
        return: boolean
        O(n)
        """
        itr = self.head
        while itr :
            if itr.data == data :
                return True 
            itr = itr.next
        
        return False
    
    def inser_after_value(self, data_after, data_to_insert):
        """
        inserts a node after the one that contains data_after value
        input: AnyType(data_after, data_to_insert)
        return: -
        O(n)
        """
        #O(1)
        if self.head == None :
            return 
        
        #O(1)
        if self.tail.data == data_after :
            node = Node(data_to_insert, None, self.tail)
            self.tail.next = node
            self.tail = node
            return
        
        #O(n)
        if self.check_value(data_after) : 
            itr = self.head
            while itr :
                if itr.data == data_after :
                    Node()
                    node = Node(data_to_insert, itr.next, itr)
                    itr.next.prev = node
                    itr.next = node
                    break
                itr = itr.next
    
    
    def remove_by_value(self, data):
        """
            removes the node that contains data
            input: data
            return: -
        """
        
        #O(1)
        if self.head is None :
            return
        
        if self.check_value(data) :
            #O(1)
            if self.head.data == data :
                self.head.next.prev = None 
                self.head = self.head.next
                return 

            #O(1)
            if self.tail.data == data :
                self.tail.prev.next = None
                self.tail = self.tail.prev
                return
        
            #O(n)
            itr = self.head
            while itr :
                if itr.next.data == data :          
                    itr.next.next.prev = itr
                    itr.next = itr.next.next
                    return
                itr = itr.next
        
        
        

if __name__ == "__main__" :
    dl = Doubly_linked_list()
    dl.insert_at_beggining(1)
    #dl.print_forward()
    dl.insert_at_beggining(2)
    dl.insert_at_beggining(3)
    '''
    dl.print_forward()
    dl.insert_at_end(32)
    dl.print_forward()
    dl.insert_values(["tuts", "hejdc", "hj"])
    dl.insert_at_end(32)
    dl.print_forward()
    dl.get_length()
    dl.print_forward()
    dl.remove_at(0)
    dl.print_forward()
    dl.remove_at(2)
    dl.print_forward()
    '''
    dl.insert_values([1,2,3,4,5,6,7,8,9])
    dl.print_forward()
    #dl.print_backward()
    dl.remove_by_value(5)
    dl.print_forward()
    dl.remove_by_value(8)
    dl.print_forward()
    dl.remove_by_value(2)
    dl.print_forward()