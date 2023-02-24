import os
import csv
#import modules

election_csv_path = os.path.join("Resources", "election_data.csv")
#create the path to the csv file

#create the list for candidate votes
candidate_votes = []

with open(election_csv_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #this creates the reader and denotes the comma delimiter
        csv_data = next(csv.reader(csvfile))
        #this skips header row
        
        #below if the list of candidates
        candidate_list = []

        #first, find and create a list of candidates and total votes list
        for row in csvreader:
                candidate_votes.append(row[2])
                
                #this will find and create the list of candidates
                if row[2] not in candidate_list:
                        #if the unique item is not in the list it will add it
                        candidate_list.append(row[2])
                        #makes a list of all the candidates
        
        #take the total number of candidate votes and find length, that is total votes
        total_votes = len(candidate_votes)

        #change it to an integer for math later
        total_votes = int(total_votes)

        #create print statements in terminal and a text file to put the information gathered so far
        print("Election Results")
        print("------------------------------")
        print(f"Total Votes: {total_votes}")
        print("------------------------------")
        
        #this opens a new text file
        with open("election_results.txt", "w") as text:
                text.write("Election Results")
                text.write('\n')
                text.write("------------------------------")
                text.write('\n')
                text.write(f"Total Votes: {total_votes}")
                text.write('\n')
                text.write("------------------------------")
                text.write('\n')
        
        #total number of candidates equals the length of the candidate list
        total_candidates = len(candidate_list)
        
        #loop through candidate list
        for c in range(len(candidate_list)):
                
                #count the number of times a candidate appears, this is the total votes
                count = candidate_votes.count(candidate_list[c])
                
                #change that to an integer
                count = int(count)
                
                #do the math to find the percent of votes
                percent = count / total_votes * 100

                #round the number to the nearest 3 decimals
                percent = round(percent, 3)

                #add the candidate name, percent votes and vote count to print statement
                print(f"{candidate_list[c]}: {percent}% ({count})")
                
                #append the txt file already created and add the same as print statement
                with open("election_results.txt", "a") as text:
                        text.write(f"{candidate_list[c]}: {percent}% ({count})")
                        text.write('\n')

                #now determine who was the winner by looking at candidate votes compared to other candidate votes
                last_count = candidate_votes.count(candidate_list[c-1])
                
                if count > last_count:
                        winner = candidate_list[c]

        #now add the winner to the print statement and txt file
        print("------------------------------")
        print(f"Winner: {winner}")
        print("------------------------------")

        with open("election_results.txt", "a") as text:
                text.write("------------------------------")
                text.write('\n')
                text.write(f"Winner: {winner}")
                text.write('\n')
                text.write("------------------------------")
       