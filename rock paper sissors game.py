import random

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win this round!"
        else:
            self.computer_score += 1
            return "Computer wins this round!"

    def play_game(self):
        while True:
            user_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to stop playing: ").lower()
            if user_choice == "quit":
                break
            elif user_choice not in ["rock", "paper", "scissors"]:
                print("Invalid choice. Please enter rock, paper, or scissors.")
                continue

            computer_choice = self.get_computer_choice()
            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}\n")

            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            print(f"Score - You: {self.user_score}, Computer: {self.computer_score}\n")

        print("Game over. Final score:")
        print(f"You: {self.user_score}, Computer: {self.computer_score}")
        if self.user_score > self.computer_score:
            print("You win the game! Congratulations!")
        elif self.user_score < self.computer_score:
            print("Computer wins the game! Better luck next time!")
        else:
            print("It's a tie game!")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()