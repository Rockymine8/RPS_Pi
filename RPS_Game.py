import RPi.GPIO as GPIO
#button setup

#player 1
GPIO.setup(4, GPIO.IN)#R
GPIO.setup(5, GPIO.IN)#P
GPIO.setup(6, GPIO.IN)#S

button_state_4 = GPIO.input(4)
print("Button 4 state:", button_state_4)

button_state_5 = GPIO.input(5)
print("Button 5 state:", button_state_5)

button_state_6 = GPIO.input(6)
print("Button 6 state:", button_state_6)

if button_state_4 == GPIO.HIGH:
    player1_choice = 'rock'
elif button_state_5 == GPIO.HIGH:
    player1_choice = 'paper'
elif button_state_6 == GPIO.HIGH:
    player1_choice = 'scissors'
else:
    player1_choice = None

#player 2
GPIO.setup(9, GPIO.IN)#R
GPIO.setup(10, GPIO.IN)#P
GPIO.setup(11, GPIO.IN)#S

button_state_9 = GPIO.input(9)
print("Button 9 state:", button_state_9)

button_state_10 = GPIO.input(10)
print("Button 10 state:", button_state_10)

button_state_11 = GPIO.input(11)
print("Button 11 state:", button_state_11)

if button_state_9 == GPIO.HIGH:
    player2_choice = 'rock'
elif button_state_10 == GPIO.HIGH:
    player2_choice = 'paper'
elif button_state_11 == GPIO.HIGH:
    player2_choice = 'scissors'
else:
    player2_choice = None




if player1_choice == player2_choice:
    print("Tie!")
elif player1_choice == 'rock' and player2_choice == 'scissors':
    print("Player 1 win!")
elif player1_choice == 'paper' and player2_choice == 'rock':
    print("Player 1 win!")
elif player1_choice == 'scissors' and player2_choice == 'paper':
    print("Player 1 win!")
else:
    print("Player 2 wins!")
    
