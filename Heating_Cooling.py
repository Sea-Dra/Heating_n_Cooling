# Heating and Cooling (Functions and conditions)

# Normal Challenge

def heating_cooling(actual_temp, desired_temp):
    if actual_temp < desired_temp:
        print("Run Heat.")
    elif desired_temp < actual_temp:
        print("Run A/C.")
    else:
        print("Stand by.")


heating_cooling(66, 78)
heating_cooling(90, 60)
heating_cooling(67, 67)

actual_temp = input("Enter the current temperature: ")
desired_temp = input("Enter your desired temperature: ")

heating_cooling(actual_temp, desired_temp)


# Extended Challenge


def convert_temp(temp_celsius, target_unit):
    if target_unit == "C":
        print(f"{temp_celsius} C")
    elif target_unit == "F":
        temp_celsius = (temp_celsius * 1.8) + 32
        print(f"{temp_celsius} F")
    elif target_unit == "K":
        temp_celsius = temp_celsius + 273.15
        print(f"{temp_celsius} K")
    else:
        print("Your input is invalid")


convert_temp(44, "F")


# OR I can ask the user for the temp_celsius and target_unit

temp_celsius = int(input("Enter the temperature in Celsius: "))
target_unit = str.upper(input("Enter the letter of temp you'd like to convert to: "))

convert_temp(temp_celsius, target_unit)
