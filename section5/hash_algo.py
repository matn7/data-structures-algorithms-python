class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:       
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found with that email address"

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
# print(hash_table)
# hash_table.set_val('majka@example.com', 'some value')
# hash_table.set_val('puszek@example.com', 'some other value')
# hash_table.set_val('evgeny@example.com',{'first_name':'Evgeny','last_name':'CoderElite'})
# hash_table.set_val('tyrion@example.com',{'first_name':'Tyrion','last_name':'BadAdvice'})
# print(hash_table)
# hash_table.set_val('majka@example.com', 'some value exited')
# print(hash_table.get_val('tyrion@example.com'))

with open("data.txt") as f:
    for line in f:
        key, value = line.split(":")
        hash_table.set_val(key, value)
    
print(hash_table.get_val('majka@example.com'))
print(hash_table.get_val('panda@example.com'))
