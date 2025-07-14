q1 = input("1. What is your favorite time of day? (a) Morning (b) Afternoon (c) Night: ").lower()

q2 = input("2. Pick a vacation spot: (a) Mountains (b) Beach (c) City: ").lower()

q3 = input("3. Which animal do you like most? (a) Dog (b) Cat (c) Owl: ").lower()
if q1 == 'a' and q2 == 'a' and q3 == 'a':
    result = "You're an Adventurer 🌄 — brave, energetic, and love the great outdoors!"
elif q1 == 'c' and q2 == 'b' and q3 == 'b':
    result = "You're a Dreamer 🌙 — creative, calm, and love your space!"
elif q1 == 'b' and q2 == 'c' and q3 == 'c':
    result = "You're a Thinker 🧠 — curious, observant, and love exploring ideas!"
else:
    result = "You're a Mix 🌈 — unique, balanced, and full of surprises!"

print("\nYour Personality Result:")
print(result)
