# Pseudocode
# Class: Patient record management
# Steps:
# 1. Define a class named patients
#    Attributes:
#      - patient_name: Patient name
#      - age: Age
#      - latest_admission: Date of latest admission
#      - medical_history: Medical history
# 2. Define a method print_details in the class
#    Method function: Print all attributes in a single line
# 3. Provide example call

class Patients:
    """
    Class for managing patient records
    Attributes:
        patient_name (str): Patient name
        age (int): Age
        latest_admission (str): Date of latest admission
        medical_history (str): Medical history
    """
    def __init__(self, patient_name, age, latest_admission, medical_history):
        """
        Initialize a patient object
        Parameters:
            patient_name (str): Patient name
            age (int): Age
            latest_admission (str): Date of latest admission
            medical_history (str): Medical history
        """
        self.patient_name = patient_name
        self.age = age
        self.latest_admission = latest_admission
        self.medical_history = medical_history

    def print_details(self):
        """
        Print patient details in a single line
        """
        print(f"Patient name: {self.patient_name}, Age: {self.age}, Latest admission: {self.latest_admission}, Medical history: {self.medical_history}")

# Example call
if __name__ == "__main__":
    # Create a patient object
    patient = Patients("John Doe", 30, "2024-10-01", "Hypertension")
    # Call the print_details method
    patient.print_details()