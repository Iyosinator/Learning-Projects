# Step 1: Read the input file
with open('input.txt', 'r') as file:
  contents = file.read()

# Step 2: Convert the input into a dictionary
original_dict = eval(contents)

# Step 3: Invert the dictionary
inverted_dict = {}

for key, value in original_dict.items():
  if value in inverted_dict:
    inverted_dict[value].append(key)
  else:
    inverted_dict[value] = [key]

# Step 4: Write the inverted dictionary to the output file
with open('output.txt', 'w') as file:
  for key, value in inverted_dict.items():
    file.write(f"{key}: {', '.join(value)}\n")

# Step 5: Close the files (not necessary with the 'with' statement)
file.close()