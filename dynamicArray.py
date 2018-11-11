

#nothing() allocates a list of none values-written because i couldnt find a default function to do so.

class dynamicArray:
    def __init__(self, data):
        self.data = data
        self.length = len(data)
    def nothing(length):
        l = []
        for i in range(length):
            l.append(None)
        return l
    def append(self, value):
        if self.length == len(self.data):
            tempdata = self.data
            self.data = nothing(2*self.length)
            for i in range(self.length):
                self.data[i] = tempdata[i]
            self.data[self.length] = value
            self.length += 1
        else:
            self.data[self.length] = value
            self.length+=1

    def delete_last_element(self):
        val = self.data[self.length-1]
        self.data[self.length-1] = None 
        return val
    def dumbappend(self, value):
        if (self.length) == len(self.data):
            tempdata = self.data
            self.data = nothing(self.length+1)
            for i in range(self.length):
                self.data[i] = tempdata[i])
            self.data[self.length] = value
            self.length += 1
        else:
            self.data[self.length] = value
            self.length+=1

#testing

a = dynamicArray([1,2,3])

a.append(4)
print a.data
a.delete_last_element()
print a.data

lc
#testing program
