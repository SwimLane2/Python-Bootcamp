# Below code calculates the percentage of a part relative to a whole.
def calculate_percentage(part, whole):    
    if whole == 0:
        return 0
    return (part / whole) * 100
# Example usage
#part = 50
#whole = 200
#percentage = calculate_percentage(part, whole)
#print(f"{part} is {percentage}% of {whole}")    
print("Welcome to the Percentage Calculator!")
part = float(input("Enter the part value: \n"))
whole = float(input("Enter the whole value: \n"))
percentage = calculate_percentage(part, whole)
print(f"{part} is {percentage}% of {whole}")
