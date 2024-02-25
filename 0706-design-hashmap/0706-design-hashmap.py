class MyHashMap:

    def __init__(self):
        self.mydict={}

    def put(self, key: int, value: int) -> None:
        self.mydict[key]=value

    def get(self, key: int) -> int:
        if key in self.mydict:
            return self.mydict[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.mydict[key]=-1

