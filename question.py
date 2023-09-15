data = [
    ("P1", "VSCode", 100, "MID"),
    ("P23", "Eclipse", 234, "MID"),
    ("P93", "Chrome", 189, "High"),
    ("P42", "JDK", 9, "High"),
    ("P9", "CMD", 7, "High"),
    ("P87", "NotePad", 23, "Low")
]

# Define a custom sorting key function
def sorting_key(item):
    priority_order = {"Low": 0, "MID": 1, "High": 2}
    return (priority_order[item[3]], item[2])  # Sorting by priority and start time

# Sort the data using the custom key function
sorted_data = sorted(data, key=sorting_key)

# Print the sorted data
print("P_ID\tProcess\tStart Time (ms)\tPriority")
for item in sorted_data:
    print(f"{item[0]}\t{item[1]}\t{item[2]}\t\t{item[3]}")