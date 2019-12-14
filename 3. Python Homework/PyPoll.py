import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = []
Khan = 0
Correy = 0
Li = 0
O_Tooley = 0

with open(csvpath, newline="") as Hmwk3Buget:
    csvreader = csv.reader(Hmwk3Buget, delimiter=",")
    next(csvreader) 

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == "Khan":
            Khan = Khan + 1
        if row[2] == "Correy":
            Correy = Correy + 1
        if row[2] == "Li":
            Li = Li + 1
        if row[2] == "O'Tooley":
            O_Tooley = O_Tooley + 1
    print(total_votes)
    print(candidates)
    print(Khan, Khan/total_votes*100)
    print(Correy, Correy/total_votes*100)
    print(Li, Li/total_votes*100)
    print(O_Tooley, O_Tooley/total_votes*100)

    
output_path = os.path.join("Resources", "ElectionOutput.csv")

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Candidates", "Votes Received", "Percentage"])
    csvwriter.writerow(["Khan", Khan, Khan/total_votes*100])
    csvwriter.writerow(["Correy", Correy, Correy/total_votes*100])
    csvwriter.writerow(["Li", Li, Li/total_votes*100])
    csvwriter.writerow(["O'Tooley", O_Tooley, O_Tooley/total_votes*100])
    csvwriter.writerow(["THe winner is Khan"])
