cards = input().split()

should_terminate = False
first_team_sent_off_players = []
second_team_sent_off_players = []

for card in cards:
    if card in first_team_sent_off_players or card in second_team_sent_off_players:
        continue
    card_args = card.split("-")
    team_name = card_args[0]
    player_number = card_args[1]

    is_first_team = team_name == "A"
    is_second_team = team_name == "B"
    if is_first_team:
        first_team_sent_off_players.append(card)

    elif is_second_team:
        second_team_sent_off_players.append(card)

    if len(first_team_sent_off_players) > 4 or len(second_team_sent_off_players) > 4:
        should_terminate = True
        break

if should_terminate:
    print("Game was terminated")

print(f"Team A - {11 - len(first_team_sent_off_players)}; Team B - {11 - len(second_team_sent_off_players)}")
