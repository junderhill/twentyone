from twentyone import TwentyOneGame

print("Twenty One")

game = TwentyOneGame()

while not game.is_game_over():
    print(game.current_hand)

    hit = input('Hit?')
    if hit == "y":
        game.hit_me()
    else:
        break

if game.is_game_over():
    print(game.current_hand)
    print('Unlucky!!')
else:
    print(game.current_score)

