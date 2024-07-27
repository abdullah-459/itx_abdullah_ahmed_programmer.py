#Name: Abdullah Ahmed
# abdullah.official@gmail.com
#Roll number:24
def get_blood_pressure_instructions(bp):
    if 80 <= bp < 100:
        return "Take some fresh juice and rest."
    elif 100 <= bp < 120:
        return "It's Excellent."
    elif 120 <= bp < 140:
        return "It's a bit high. Take a long breath."
    elif 140 <= bp < 160:
        return "Take some rest and drink plenty of water."
    elif 160 <= bp < 180:
        return "Consult a doctor and take medicine."
    elif 180 <= bp <= 210:
        return "Immediately visit the nearest clinic or hospital and take the supervision of a Doctor."
    else:
        return "Blood pressure out of range. Please enter a valid blood pressure value."

def main():
    try:
        bp = int(input("Enter your blood pressure: "))
        instructions = get_blood_pressure_instructions(bp)
        print(instructions)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
