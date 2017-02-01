def main():
    team = input("Enter a team name:")
    
    f = open('WorldSeriesWinners.txt', 'r')
    data = f.read().splitlines()
    f.close()
    
    won = 0
    for i in range(0, len(data) - 1):
        if data[i] == team:
            won += 1
    
    print("They have won", won, "time(s)")
