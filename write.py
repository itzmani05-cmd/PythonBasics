import csv
with open('protagonist.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN","Name","Job"])
    writer.writerow(["1","Manikandan","Learning"])
    writer.writerow(["2","Maharaja","Playing"])

import csv
row_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)