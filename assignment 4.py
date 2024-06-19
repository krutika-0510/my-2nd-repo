#Assignment 4
#Creating first feedback file
with open("C:\\Users\\Mahesh\\Desktop\\Python\\Feedback1.txt",'w') as file:    #paste the path where you want to create the files with the file name
   file.write("Customer's Feedback in 1st File:")
   file.write("\n Krutika: 3 - Average Service, needs improvement.")
   file.write("\n Pranjal: 4 - Good Service, but could improve.")
   file.write("\n Aaditi: 3 - Average Service, needs improvement.")

#Creating second feedback file
with open("C:\\Users\\Mahesh\\Desktop\\Python\\Feedback2.txt",'w') as file:    #paste the path where you want to create the files with the file name
   file.write("Customer's Feedback in 2nd File:")
   file.write("\n Rudra: 5 - Very Good Service!")
   file.write("\n Tanishq: 2 - Poor Service, must improve.")
   file.write("\n Parth: 5 - Very Good Service!")

#Creating third feedback file
with open("C:\\Users\\Mahesh\\Desktop\\Python\\Feedback3.txt",'w') as file:    #paste the path where you want to create the files with the file name
   file.write("Customer's Feedback in third file:")
   file.write("\n Mahesh: 5 - Efficient Service!")
   file.write("\n Nirmohi: 4 - Good Service!!.")
   file.write("\n Roshani: 4 - Good Service!!.")
   file.write("\n Shweta: 2 - Very Poor Service, needs more improvement.")

import os
# Function to read feedback files
def readfdbfiles(filenames):
    feedbacks = []
    for filename in filenames:
        try:
            with open(os.path.join("C:\\Users\\Mahesh\\Desktop\\Python", filename), 'r') as file:
                feedbacks.extend(file.readlines())
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        except Exception as e:
            print(f"An error occurred while reading {filename}: {e}")
    return feedbacks

# Function to process feedback data
def processfdbdata(feedbacks):
    processedfeedbacks = []
    totalratings = 0
    for feedback in feedbacks:
        try:
            customername, rest = feedback.split(': ', 1)
            rating, comment = rest.split(' - ', 1)
            rating = int(rating)
            # Validate rating (optional)
            if rating < 1 or rating > 5:
                raise ValueError(f"Invalid rating value: {rating}")
            processedfeedbacks.append((customername, rating, comment))
            totalratings += rating
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: Invalid format in feedback entry: {feedback.strip()}")
    
    average_rating = totalratings / len(processedfeedbacks) if processedfeedbacks else 0
    return processedfeedbacks, average_rating

# Function to write summary file
def writesummaryfile(filename, processedfeedbacks, average_rating):
    try:
        with open(os.path.join("C:\\Users\\Mahesh\\Desktop\\Python", filename), 'w') as file:
            file.write(f"Total Feedback Entries: {len(processedfeedbacks)}\n")
            file.write(f"Average Rating: {average_rating:.2f}\n")
            file.write("\nFeedbacks:\n")
            for feedback in processedfeedbacks:
                file.write(f"{feedback[0]}: {feedback[1]} - {feedback[2]}\n")
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")

# Main logic
if __name__ == "_main_":
    inputfiles = ['Feedback1.txt', 'Feedback2.txt', 'Feedback3.txt']
    feedbacks = readfdbfiles(inputfiles)
    processedfeedbacks, average_rating = processfdbdata(feedbacks)
    writesummaryfile('FeedbacksSummary.txt', processedfeedbacks, average_rating)