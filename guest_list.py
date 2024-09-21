# 3-4. Guest List:
guests_list : list =["Faizan","Samia","Sadia"]
for guest in guests_list:
    print(f"Hey {guest.title()} I have a dinner tomorrow at 8 ")
# 3-5. Changing Guest List:
print(f"\t{guests_list[1]} can't come to party")
guests_list[1]="Duaa"
for guest in guests_list:
    print(f"Hey {guest.title()} I have a dinner tomorrow at 8 ")
# 3-6. More Guests:
print(f"\tWe have some more guests")
guests_list.insert(0,"Hiba")
guests_list.insert(3,"Hamna")
guests_list.append("Mair")
for guest in guests_list:
    print(f"Hey {guest.title()} I have a dinner tomorrow at 8 ")
#3-7. Shrinking Guest List:
print(f"\t Can only invite two people")
for guest in guests_list:
    if len (guests_list)>=2:
        name=guests_list.pop()
        print(f"Sorry {name} can't invite you to dinner")     
    # for guest in guests_list:    
        print(f"You're still invited {guest}")  
guests_list.clear()
print(guests_list)