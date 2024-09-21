# Guest List Manager

This project is a **Guest List Manager** written in Python. It simulates managing a guest list for a dinner party, allowing for adding, replacing, and removing guests, and even handling the unfortunate need to reduce the number of invites.

## Features

1. **Initial Invitations**: Sends dinner invitations to an initial list of guests.
2. **Change Guest**: Handles the case where one guest cannot attend and replaces them with another.
3. **Add More Guests**: Adds additional guests to the beginning, middle, and end of the list.
4. **Shrink Guest List**: Simulates the scenario where only two guests can be invited, removing guests from the list and notifying them.
5. **Clear Guest List**: After handling all invitations, the guest list is cleared.

## How It Works

- Initially, the program invites a list of guests.
- The guest list is dynamically updated when a guest can't attend, and new guests are added.
- In the end, the guest list is reduced to only two people, with the remaining guests being informed that they're still invited.
- The program concludes by clearing the guest list.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/guest-list-manager.git
   cd guest-list-manager
   ```

2. Run the Python script:

   ```bash
   python guest_list.py
   ```

## Example

```bash
Hey Faizan, I have a dinner tomorrow at 8.
Hey Samia, I have a dinner tomorrow at 8.
Hey Sadia, I have a dinner tomorrow at 8.

Samia can't come to the party.
Hey Faizan, I have a dinner tomorrow at 8.
Hey Duaa, I have a dinner tomorrow at 8.
Hey Sadia, I have a dinner tomorrow at 8.

We have some more guests!
Hey Hiba, I have a dinner tomorrow at 8.
Hey Faizan, I have a dinner tomorrow at 8.
Hey Duaa, I have a dinner tomorrow at 8.
Hey Hamna, I have a dinner tomorrow at 8.
Hey Sadia, I have a dinner tomorrow at 8.
Hey Mair, I have a dinner tomorrow at 8.

Unfortunately, I can only invite two people.
Sorry Mair, I can't invite you to dinner.
Sorry Sadia, I can't invite you to dinner.
Sorry Hamna, I can't invite you to dinner.
Sorry Duaa, I can't invite you to dinner.

You're still invited, Hiba.
You're still invited, Faizan.

Final guest list: []
```

## License

This project is licensed under the MIT License.
