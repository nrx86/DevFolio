# series=[35,45,36,21,30,1,2]
# min=series[0]
# max=series[0]
# for i in series:
#     if i<min:
#         min=i
#     if i>max:
#         max=i

# print(min)
# print(max)  


# series=[35,45,36,21,30,1,2]
# max = series[0]
# second_max = series[0]
# for i in series:
#     if i>max:
#         second_max=max
#         max=i
#     elif i>second_max and i!=max:
#         second_max=i
# print("The second largest number is:", second_max)

votes = {}

while True:
    candidate = input()

    if candidate == "END":
        break

    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1

if len(votes) == 0:
    print("No votes cast")
else:
    for candidate in votes:
        print(candidate +":",votes[candidate])

    winner = ""
    highest = 0

    for candidate in votes:
        if votes[candidate] > highest:
            highest = votes[candidate]
            winner = candidate

    print("Winner:", winner)

