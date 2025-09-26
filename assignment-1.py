import array

# ...........Arrays: Volunteer Hours Log ..............
volunteer_hours = array.array('i', [5, 8, 6, 7, 9])
total_hours = sum(volunteer_hours)
average_hours = total_hours / len(volunteer_hours)
print(f"Total Hours: {total_hours}, Average: {average_hours:.2f}")

#...........Dictionaries: Volunteer Records ..............
volunteer_log = [
    {'unit': 'Health Unit A', 'hours': 5},
    {'unit': 'Health Unit B', 'hours': 8},
    {'unit': 'Health Unit C', 'hours': 6}
]
volunteer_log[1]['hours'] = 10  # Update
del volunteer_log[0]            # Delete
print("Updated Volunteer Log:", volunteer_log)

# ........................ CONDITIONS......................................
standard = 7
if average_hours > standard and total_hours > 20:
    print("Above Average")
else:
    print("Below Standard")

# ..........................LIST: ERROR TRACKING ..................................................
errors = ['Missing ID', 'Wrong Date']
print("Before:", errors)
errors.append('Invalid Time')
errors.remove('Wrong Date')
print("After:", errors)

# .........................Sets: Unique Volunteers ...............................
volunteers = {'Alice', 'Bob', 'Charlie', 'Alice'}
print("Unique Volunteers:", volunteers)
if average_hours > standard and len(volunteers) > 2:
    print("Above Standard")
else:
    print("Below Standard")

#........................ Tuples: Blood Donation Camps..................................
camps = (('Camp1', 20), ('Camp2', 15), ('Camp3', 25))
camp_totals = [camp[1] for camp in camps]
total_participants = sum(camp_totals)
average_participants = total_participants / len(camps)
max_participants = max(camp_totals)
print(f"Total: {total_participants}, Average: {average_participants:.2f}, Max: {max_participants}")
print("Above Standard" if average_participants > standard else "Below Standard")

# ......................Strings: OUTREACH MESSAGE..................................
message = "Community Health Outreach is vital. Outreach helps."
word = "Outreach"
count = message.count(word)
position = message.find(word)
updated_message = message.replace(word, "Support")
print(f"'{word}' occurs {count} times at position {position}")
print("Updated Message:", updated_message)

# --- Booleans: System Status ---
status = average_hours > standard and total_hours > 20
print("System Status:", "Above Standard" if status else "Below Standard")
