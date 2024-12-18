# Function to generate merit lists for each subject
def generate_merit_lists(input_file):
    try:
        # Read the data from the input file
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # Parse the header and student data
        header = lines[0].strip().split(',')
        students = [line.strip().split(',') for line in lines[1:]]
        
        # Define subject indices
        subject_indices = {
            "Physics": header.index("Physics Marks"),
            "Chemistry": header.index("Chemistry Marks"),
            "Mathematics": header.index("Mathematics Marks")
        }
        
        # Generate merit list for each subject
        for subject, index in subject_indices.items():
            # Sort students manually by marks in the current subject
            for i in range(len(students)):
                for j in range(i + 1, len(students)):
                    # Convert marks to integers for comparison
                    if int(students[i][index]) < int(students[j][index]):
                        # Swap if the current student has fewer marks
                        students[i], students[j] = students[j], students[i]
            
            # Write the sorted list to a new file
            with open(f"{subject}_Merit_List.txt", 'w') as merit_file:
                merit_file.write(f"Name,Roll Number,{subject} Marks\n")
                for student in students:
                    merit_file.write(f"{student[0]},{student[1]},{student[index]}\n")
        
        print("Merit lists generated successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the input file name
input_file_name = "students_data.txt"
generate_merit_lists(input_file_name)