#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[3] != 'Jefferson':
#    print(counties[2])
#
#What is the temperature?
#temperature = int(input("What is the temperature outside?"))
#
#if temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")

#What is the score?
#score = int(input("What is your test score?"))

#Determine the grade.
#if score >= 90:
#    print('Your grade is an A.')
#elif score >= 80:
#    print('Your grade is a B.')
#elif score >=70:
#    print('Your grade is a C.')
#elif score >= 60:
#    print('Your grade is a D.')
#else:
#    print('Your grade is an F')

#counties = ["Arapahoe","Denver","Jefferson"]
#if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe  is in the list of counties ad El Paso is not in the list of counties")

#for i in range(len(counties)):
#    print(counties[i])

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters:,} registered voters.")


#fstring printing
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print(f"I received {my_votes / total_votes * 100}% of the total votes")

#fstring dictionaries
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters")

#Multi line Fstrings
#candidate_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#message_to_candidate =(
#    f"You received {candidate_votes:,} number of votes."
#    f"The total number of votes in the election was {total_votes:,}."
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

voting_data = [1: {"county":"Arapahoe", "registered_voters": 422829}, 
               2: {"county":"Denver", "registered_voters": 463353}, 
               3: {"county":"Jefferson", "registered_voters": 432438}]
               
print(f"{voting_data[1]['county']} county has {voting_data[1]['registered_voters']:,} registered voters")


#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    print(county_dict["county"])