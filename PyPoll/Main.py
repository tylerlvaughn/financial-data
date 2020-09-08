import os
import csv

#Path to Collect Data from the Resources Folder
poll_csv = os.path.join('Resources', 'election_data.csv')

#Open CSV and Read the File
with open(poll_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    print(f"Header: {header}")

    #Declare Varables
    count = 0
    winner_votes = 0
    most_votes = ["",0]
    candidates = []
    candidate_votes = {}

    #Total Votes for Each Candidate
    for row in csvreader:    

        count = count + 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        #Determine Winner
        if (count > winner_votes):
            most_votes[1] = candidate_votes
            most_votes[0] = row[2]

    #Print Total Results
    print ("Election Results")
    print ("---------------------------------------")
    print ("Total Votes: " + str(count))
    print ("---------------------------------------")
    #Print Individual Results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/count)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/count)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
    candidate_votes

    winner = sorted(candidate_votes.items(),)

    #Winner Results
    print("-------------------------")
    print("Winner: " + str(winner[1]))
    print("-------------------------")

    #Results to Text File

    
    file = open("output.txt","w")

    file.write("Election Results" + "\n")

    file.write("------------------------------------------------" + "\n")

    file.write("Total Votes: " + str(count) + "\n")

    file.write("------------------------------------------------" + "\n")

    file.write(candidate + " " + str(round(((candidate_votes[candidate]/count)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")

    file.write(str(winner) + "\n")

    file.write("------------------------------------------------" + "\n")

    file.write("Winner: " + str(winner[1]) + "\n")

    file.close()







        

