🏏 CLI Hand Cricket Game – User Guide
This is a simple command-line based Hand Cricket game built with Python where you play against an AI.

🎮 How to Play
1. Start the Game
When you run the script, the game will welcome you and ask:

"hmm... odd or even 😏??"

Type either:

odd

even

This will be your toss choice.

2. Toss Time
You will then be asked to:

"enter the tose number:"

Input a number between 0 and 6 (inclusive).
The AI will also randomly choose a number. If the sum is even or odd (based on your original choice), the winner of the toss is decided.

3. Choose Batting or Bowling (if you win toss)
If you win the toss, you get to choose:

"your turn enter batting🏏 or balling⚾"

Type:

batting – You will bat first

balling – You will bowl first

If the AI wins the toss, it will choose for you randomly.

4. Gameplay Rules
🔁 Turns:
In each turn, both you and the AI select a number between 0 and 6.

If both numbers match, the batting player is OUT.

If numbers are different, the batter scores runs equal to their chosen number.

💡 Example:
You chose 4 and AI chose 2 → You score 4 runs
You chose 3 and AI chose 3 → You're OUT

5. Innings
The first player bats and scores runs until they are out.

The second player then tries to chase the target and win.

Whoever scores more runs wins!

🧠 AI Behavior
The AI makes random choices for:

Toss number

Runs while batting or bowling

Toss winner’s decision (if AI wins)

🏁 Winning
After both innings are over:

If your score is higher → You Win 🏆

If AI's score is higher → You Lose 😏

If scores are equal → It's a Draw 🤝

⚠️ Input Guidelines
Always enter numbers between 0 and 6

For toss and gameplay, only valid inputs are accepted (program will re-prompt on error)

