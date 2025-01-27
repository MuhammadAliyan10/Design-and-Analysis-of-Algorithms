class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hashTable(self, key):
        hashValue = 0
        for char in key:
            hashValue = (hashValue * 31 + ord(char)) % self.size
        return hashValue
    
    def insert(self, key, value):
        index = self.hashTable(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    def search(self, key):
        index = self.hashTable(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key):
        index = self.hashTable(key)
        for i , pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False
    
    def sortByKeys(self):
        allItems = []
        for bucket in self.table:
            allItems.extend(bucket)
        return sorted(allItems, key=lambda x: x[0])
    
    def sortByValues(self):
        allItems = []
        for bucket in self.table:
            allItems.extend(bucket)
        return sorted(allItems, key=lambda x: x[1])
    

if __name__ == "__main__":
    hashTable = HashTable(size=10)
    hashTable.insert("apple", 50)
    hashTable.insert("banana", 30)
    hashTable.insert("cherry", 20)
    hashTable.insert("date", 40)

    print(f"Search 'banana': {hashTable.search('banana')}")
    print(f"Search 'mango': {hashTable.search('mango')}")

    print("Sorted by key:", hashTable.sortByKeys())
    print("Sorted by value:", hashTable.sortByValues())
