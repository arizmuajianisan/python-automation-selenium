import os
import pandas as pd


def merge_csv_files(input_dir, output_file):
    """
    Merges all CSV files in the specified directory into a single CSV file.

    :param input_dir: Directory containing the CSV files.
    :param output_file: Path to the output CSV file.
    """
    # List all CSV files in the directory
    csv_files = [f for f in os.listdir(input_dir) if f.endswith(".csv")]

    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Initialize a list to hold DataFrames
    df_list = []

    for i, file in enumerate(csv_files):
        file_path = os.path.join(input_dir, file)
        # print(f"Processing {file_path}")
        print(f"Processing {file}")

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Check if the DataFrame has more than one row (excluding header)
        if df.shape[0] > 1:
            df_list.append(df)
        elif df.shape[0] == 1:
            # If the DataFrame has only one row, include it without the header
            df_list.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    merged_df = pd.concat(df_list, ignore_index=True)

    # Write the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)
    print(f"Merged CSV saved to {output_file}")


# Example usage
if __name__ == "__main__":
    input_directory = os.path.join("./extracted_files")
    output_csv = os.path.join("./result/merged_output.csv")

    merge_csv_files(input_directory, output_csv)
