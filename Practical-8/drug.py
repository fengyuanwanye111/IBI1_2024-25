# Pseudocode
# Function: Calculate paracetamol dosage
# Input: weight (kg), strength ("120 mg/5 ml" or "250 mg/5 ml")
# Output: Required volume (ml)
# Steps:
# 1. Check if weight is between 10-100 kg
#    If not, raise error
# 2. Check if strength is valid ("120 mg/5 ml" or "250 mg/5 ml")
#    If invalid, raise error
# 3. Calculate required dose: weight × 15 mg/kg
# 4. Calculate volume based on strength:
#    If strength is "120 mg/5 ml", volume = (dose / 120) × 5
#    If strength is "250 mg/5 ml", volume = (dose / 250) × 5
# 5. Return volume (rounded to 2 decimal places)
# 6. Provide example call

def calculate_paracetamol_dosage(weight, strength):
    """
    Calculate the required paracetamol dosage for children
    Parameters:
        weight (float): Weight in kg, must be between 10-100 kg
        strength (str): Paracetamol strength, must be "120 mg/5 ml" or "250 mg/5 ml"
    Returns:
        float: Required paracetamol volume in ml
    """
    # Check 1: Weight range
    if not (10 <= weight <= 100):
        raise ValueError("Error: Weight must be between 10-100 kg!")

    # Check 2: Valid strength
    valid_strengths = ["120 mg/5 ml", "250 mg/5 ml"]
    if strength not in valid_strengths:
        raise ValueError("Error: Strength must be '120 mg/5 ml' or '250 mg/5 ml'!")

    # Calculate required dose: Recommended dose is 15 mg/kg
    required_dose = weight * 15  # Total paracetamol needed in mg

    # Calculate volume based on strength
    if strength == "120 mg/5 ml":
        # 120 mg corresponds to 5 ml, so 1 mg corresponds to 5/120 ml
        volume = (required_dose / 120) * 5
    else:  # strength == "250 mg/5 ml"
        # 250 mg corresponds to 5 ml, so 1 mg corresponds to 5/250 ml
        volume = (required_dose / 250) * 5

    return round(volume, 2)  # Round to 2 decimal places

# Example call
if __name__ == "__main__":
    try:
        # Example 1: Weight 20 kg, strength 120 mg/5 ml
        volume = calculate_paracetamol_dosage(20, "120 mg/5 ml")
        print(f"Weight 20 kg, strength 120 mg/5 ml, requires {volume} ml paracetamol.")

        # Example 2: Test error case (weight out of range)
        volume = calculate_paracetamol_dosage(5, "120 mg/5 ml")
    except ValueError as e:
        print(e)