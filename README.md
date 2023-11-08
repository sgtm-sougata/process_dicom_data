# DICOM Data Processing

This Python script processes DICOM (Digital Imaging and Communications in Medicine) data and extracts specific metadata information from the DICOM files. It creates a CSV file containing details like PatientID, SeriesDescription, RepetitionTime, EchoTime, FlipAngle, and InversionTime.

## Installation

1. **Requirements:**
   - Python 3.x
   - `pydicom` library
   - `pandas` library

2. **Installation of Required Libraries:**
   You can install the required libraries via pip:
   ```bash
   pip install pydicom pandas
   ```
## Usage
The main function in the script, process_dicom_data(root_directory), takes in the root directory of DICOM files and the desired output CSV file path.Modify the root_directory to set your own paths.

## Important Notes
  Ensure that the root directory contains DICOM files in its subdirectories.
  The script extracts specific DICOM metadata and saves it to a CSV file.
  Ensure the necessary permissions for file read and write operations.
  Contributing
  If you find any issues or would like to contribute to this project, please feel free to create a pull request or open an issue in the repository.

## License

  This project is licensed under MIT License. Please check the LICENSE file for details.
