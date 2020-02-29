# Import dependencies
import os
import csv

# Define CSV document path
election_csv = os.path.join("Resources", "election_data.csv")

# Define election results function
def election_results():
    
    # Open CSV file in read mode
    with open(election_csv, 'r') as csvfile:

        # Split the data on commas
        election = csv.reader(csvfile, delimiter = ",")

        # Skip the header
        header = next(election)
        
        # Create lists to host the data elements
        voter_id = []
        county = []
        candidate = []
        unique_candidates = []
        unique_candidates_votes = []

        # From the CSV, assign elements to the lists
        for row in election:
            voter_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])

        # Find total number of votes
        total_votes = len(voter_id)

    # Create text file to show election results
    file = open("election_results.txt","w")
    
    # Create output strings
    output_intro = (
        "Election Results\n"
        '---------------------------\n'
        f'Total Votes: {total_votes}\n'
        '---------------------------'
        )

    # Print results intro and total votes to terminal
    print(output_intro)
    
    # Export results intro and total votes to text file
    file.write(output_intro)

    # Get unique candidates
    for i in candidate:
        if i not in unique_candidates:
            unique_candidates.append(i)

    # Get number of votes and proportion per candidate
    for i in unique_candidates:
        count = candidate.count(i)
        unique_candidates_votes.append(count)
        vote_percentage = (((count/total_votes)*100))
        index = unique_candidates.index(i)
        
        # Create output strings
        output_results = f'\n{unique_candidates[index]}: {vote_percentage:.3f}% ({count})\n'
        
        # Print results analysis to terminal
        print(output_results)
        
        # Export results analysis to text file
        file.write(output_results)

    # Get candidate with highest votes
    winner_votes = max(unique_candidates_votes)
    winner_index = unique_candidates_votes.index(winner_votes)

    # Create output strings
    output_end = (    
            '---------------------------\n'
        f'Winner: {unique_candidates[winner_index]}'
        )
    
    # Print winner to terminal
    print(output_end)
    
    # Export winner to text file
    file.write(output_end)
        
election_results()