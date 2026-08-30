gender = input("Enter biological gender (female/male): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Low hemoglobin")
    elif hemoglobin > 155:
        print("High hemoglobin")
    else:
        print("Normal hemoglobin")
elif gender == "male":
    if hemoglobin < 134:
        print("Low hemoglobin")
    elif hemoglobin > 167:
        print("High hemoglobin")
    else:
        print("Normal hemoglobin")
else:
    print("Invalid gender")