import os
import pandas as pd
from tkinter import messagebox


def mark_attendance_in_excel(compiled_attendance_file, input_directory):
    # Check if the compiled attendance file already exists
    if os.path.isfile(compiled_attendance_file):
        # Read the existing compiled attendance file
        compiled_df = pd.read_excel(compiled_attendance_file)
    else:
        # Create an empty dataframe if the file doesn't exist
        compiled_df = pd.DataFrame(columns=['Name'])

    # Get all CSV files in the specified directory
    csv_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]

    # Create columns for total present count and percentage if not already present
    if 'Total_Present_Count' not in compiled_df.columns:
        compiled_df['Total_Present_Count'] = 0

    if 'Total_lectures' not in compiled_df.columns:
        compiled_df['Total_lectures'] = 0

    if 'Percentage' not in compiled_df.columns:
        compiled_df['Percentage'] = 0.0

    # Iterate through each CSV file and mark attendance in the compiled dataframe
    for file in csv_files:
        file_path = os.path.join(input_directory, file)
        df = pd.read_csv(file_path)

        # Filter rows with 'present' status
        present_rows = df[df['Status'] == 'present']

        # Extract names from the present rows
        present_names = set(present_rows['Name'])

        # Mark attendance in the compiled dataframe based on names
        compiled_df[f"Attendance_{file.split('.')[0]}"] = compiled_df['Name'].apply(
            lambda x: 'present' if x in present_names else 'absent')

        # Update total present count column
        compiled_df['Total_Present_Count'] += compiled_df[f"Attendance_{file.split('.')[0]}"].eq(
            'present').astype(int)

        compiled_df['Total_lectures'] = len(csv_files)

    # Calculate the percentage column
    compiled_df['Percentage'] = round((
        compiled_df['Total_Present_Count'] / len(csv_files)) * 100, 2)

    output_file = 'marked_Attendance.xlsx'
    compiled_df.to_excel(output_file, index=False)
    return output_file


# # Specify the path to the compiled attendance Excel file and the directory containing CSV files
# compiled_attendance_file = './Attendance_files/compiled_Attendance.xlsx'
# input_directory = './Attendance_files/'

# # Call the function to mark attendance in the Excel file
# mark_attendance_in_excel(compiled_attendance_file, input_directory)
