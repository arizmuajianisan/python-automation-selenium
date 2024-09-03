import os
import logging
import pandas as pd
import pantab as pt


def export_to_hyper(csv_path, hyper_dir="./hyper_dir", filename="pcb_molding.hyper"):
    """
    Reads a CSV file from a specified path and exports the data to a Hyper file in the specified folder.

    :param csv_path: The path to the CSV file to read.
    :param hyper_dir: The folder where the Hyper file will be saved.
    :param filename: The name of the Hyper file.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_path)
        print(df.columns)
        print(f"Read CSV from {csv_path}")

        # Ensure the folder exists
        if not os.path.exists(hyper_dir):
            os.makedirs(hyper_dir)
            print(f"Created directory: {hyper_dir}")

        # Construct the full file path
        file_path = os.path.join(hyper_dir, filename)

        # Export the DataFrame to a Hyper file
        pt.frame_to_hyper(df, file_path, table="pcb_molding")
        print(f"Data successfully exported to {file_path}")

    except Exception as e:
        logging.error(f"Failed to export data: {e}.")
        raise

if __name__ == "__main__":
    # Example usage:
    csv_path = "./result/merged_output.csv"
    hyper_dir = "./hyper_dir"
    export_to_hyper(csv_path, hyper_dir)