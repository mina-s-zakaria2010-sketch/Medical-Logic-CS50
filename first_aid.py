# First Aid Logic System - CS50 Inspired
# Based on Research by: Mina Sherif (2026)

def emergency_protocol():
    print("--- First Aid Decision Tree System ---")
    print("Developed based on Alexandrian Community Research [Mina Sherif]\n")
    
    print("Emergency Type: 1. Bleeding  2. Fainting  3. Burns")
    choice = input("Enter number of emergency: ")

    if choice == "1":
        # Based on 79.5% awareness result 
        print("[LOGIC]: Apply direct pressure with a clean cloth. Call 123.")
    elif choice == "2":
        # Based on 56.4% awareness result [cite: 22, 60]
        print("[LOGIC]: Lay on back, lift legs. DO NOT spray water. Call 123.")
    elif choice == "3":
        # Based on 70% awareness result [cite: 21, 63]
        print("[LOGIC]: Cool running water for 10 mins. Call 123.")
    else:
        print("[RUNTIME ERROR]: Logical error. Unknown emergency. Call 123 IMMEDIATELY.")

if __name__ == "__main__":
    emergency_protocol()