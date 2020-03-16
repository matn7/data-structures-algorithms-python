records = [('majka@example.com', 'Hello World'),
        ('puszek@example.com', 'Hello puszek'),
        ('seba@example.com', 'Hello Seba')]

for index, record in enumerate(records):
    key, value = record
    if key == "puszek@example.com":
        break

print(records[index])       