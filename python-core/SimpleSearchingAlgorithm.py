# LinearSearch:
class LinerSearch:
    def __init__(self,list):
        self.list = list
    def getIndex(self,search):
        list = self.list
        for i in range(0,len(list)):
            if list[i] == search:
                return i
        return 'Search element not found'
li = [1,4,63,46,45,78]
finder = LinerSearch(li)
print(finder.getIndex(100))
