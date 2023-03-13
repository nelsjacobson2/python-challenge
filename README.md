# python-challenge

Election Results Analysis
This code analyzes the election data given in election_data.csv file and outputs the following results:

Total number of votes cast.
List of candidates who received votes.
Percentage of votes and total number of votes each candidate received.
The winner of the election.
The code uses the pandas library to read the CSV file and store it in a pandas DataFrame. It then calculates the total number of votes cast by finding the length of the DataFrame.

Next, it creates a list of all the candidates who received votes by selecting the unique values from the "Candidate" column of the DataFrame.

It then calculates the percentage of votes and the total number of votes each candidate received by using the value_counts() function and dividing it by the total number of votes cast.

The code then determines the winner of the election by selecting the candidate with the most votes.

Finally, the results are printed to the console and saved to a text file named election_analysis.txt located in the Analysis folder of the project directory.

How to Run
To run this code, you need to have Python 3.x installed on your system.

Download the election_data.csv file and save it to your local machine.
Open the terminal and navigate to the directory where you saved the code.
Run the following command: python election_analysis.py
