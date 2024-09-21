# 3-4. Guest List:
guests_list = ["Faizan", "Samia", "Sadia"]
for guest in guests_list:
    print(f"Hey {guest.title()}, I have a dinner tomorrow at 8.")

# 3-5. Changing Guest List:
print(f"\n{guests_list[1]} can't come to the party.")
guests_list[1] = "Duaa"
for guest in guests_list:
    print(f"Hey {guest.title()}, I have a dinner tomorrow at 8.")

# 3-6. More Guests:
print("\nWe have some more guests!")
guests_list.insert(0, "Hiba")   # Add guest at the beginning
guests_list.insert(3, "Hamna")  # Add guest at the middle
guests_list.append("Mair")      # Add guest at the end
for guest in guests_list:
    print(f"Hey {guest.title()}, I have a dinner tomorrow at 8.")

# 3-7. Shrinking Guest List:
print("\nUnfortunately, I can only invite two people.")

# Remove guests until only 2 remain
while len(guests_list) > 2:
    name = guests_list.pop()
    print(f"Sorry {name.title()}, I can't invite you to dinner.")

# Inform the remaining guests that they are still invited
for guest in guests_list:
    print(f"You're still invited, {guest.title()}.")

# Clear the guest list
guests_list.clear()
print("\nFinal guest list:", guests_list)
