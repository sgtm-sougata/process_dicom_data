import os
import pydicom
import pandas as pd

def process_dicom_data(root_directory):
    data = []

    for path, dir, filenames in os.walk(root_directory):
        for filename in filenames:
            filepath = os.path.join(path, filename)
            ds = pydicom.dcmread(filepath)

            PatientID = ds.PatientID
            SeriesDescription = ds.SeriesDescription
            RepetitionTime = ds.get("RepetitionTime", "NA")
            EchoTime = ds.get("EchoTime", "NA")
            FlipAngle = ds.get("FlipAngle", "NA")
            InversionTime = ds.get("InversionTime", "NA")

            # Writing data to list
            data.append([PatientID, SeriesDescription, RepetitionTime, EchoTime, FlipAngle, InversionTime])

    df = pd.DataFrame(data, columns=["PatientID", "SeriesDescription", "RepetitionTime", "EchoTime", "FlipAngle", "InversionTime"])
    df = df.drop_duplicates()
    df.to_csv("process_dicom_data.csv", index=False)

# Example usage
root_dir = os.path.join(os.getcwd(), "data")
process_dicom_data(root_dir)
