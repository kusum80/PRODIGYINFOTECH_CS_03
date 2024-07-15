def check_password_strength(password):
    """
    This function checks the strength of a password based on various criteria.

    Args:
        password: The password string to be evaluated.

    Returns:
        A tuple containing a score (int) and a strength message (str).r
    """

    # Define criteria and weights
    criteria = {
        "length": 10,      # Maximum points for length
        "uppercase": 1,
        "lowercase": 1,
        "number": 1,
        "special": 1,
    }

    # Initialize score and flags for character classes
    score = 0
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    # Check length
    length_score = min(criteria["length"], len(password))
    score += length_score

    # Check character classes
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_number = True
        elif not char.isalnum():  # Special character
            has_special = True

    # Add points for each character class found
    if has_uppercase:
        score += criteria["uppercase"]
    if has_lowercase:
        score += criteria["lowercase"]
    if has_number:
        score += criteria["number"]
    if has_special:
        score += criteria["special"]

    # Define strength messages based on score
    strength_messages = {
        (0, 9): "Very Weak (Needs improvement)",
        (10, 12): "Weak (Consider adding more complexity)",
        (13, 14): "Strong (Good password)",
    }

    # Determine strength message based on score
    for score_range, message in strength_messages.items():
        if score_range[0] <= score <= score_range[1]:
            return score, message

    # Default return in case of unexpected score
    return score, "Unknown Strength"

def main():
    while True:
        # Get user input
        password = input("Enter your password: ")

        # Check password strength
        score, message = check_password_strength(password)

        # Print results
        print(f"Password Strength: {score} ({message})")

        # If the password is at least moderate, break the loop
        if score >= 13:
            print("Password is strong enough.")
            break
        else:
            print("Please try again with a stronger password.")

# Run the main function
main()
