import os
import time
import csv
import openpyxl
import subprocess



def combine_csv_to_xlsx(csv_files, output_filename, selected_columns=None):
    wb = openpyxl.Workbook()

    for csv_file in csv_files:
        sheet_name = os.path.splitext(os.path.basename(csv_file))[0]  # Use CSV filename as sheet name
        ws = wb.create_sheet(title=sheet_name)

        with open(csv_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if selected_columns:
                    selected_row = [row[i] for i in selected_columns]
                else:
                    selected_row = row
                ws.append(selected_row)

    # Remove the default sheet created by openpyxl
    wb.remove(wb['Sheet'])

    # Save the combined workbook
    wb.save(output_filename)
    print(f"Combined CSV files saved to {output_filename}")



print("Generando reportes...\n")

try:
    subprocess.run(["C:\\ADReport\\HSAReport.bat"], check=True)
except subprocess.CalledProcessError:
    print("Error: The subprocess returned a non-zero exit status.")

time.sleep(660)


if __name__ == "__main__":
    csv_files_to_combine = ['UsersArgentina.csv', 'UsersChile.csv', 'UsersColombia.csv', 'UsersCostaRica.csv']
    output_xlsx_filename = 'UsersHSA.xlsx'
    columns_to_include = [0, 1, 3, 5, 8]  # Customize this list (0-based indices)
    combine_csv_to_xlsx(csv_files_to_combine, output_xlsx_filename, selected_columns=columns_to_include)