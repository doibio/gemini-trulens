if len(sys.argv) < 3:
    print("Usage: p split-edirect.py input_file output_directory")
    sys.exit(1)
    
source_file_path = sys.argv[1]
output_file_path = sys.argv[2]

file_counter = 1
new_file = None

with open(source_file_path, 'r') as file:
    for line in file:
        if line.startswith("PMID:"):
            if new_file is not None:
                new_file.close()

            new_file_path = f'{output_file_path}{file_counter}.txt'
            new_file = open(new_file_path, 'w')
            file_counter += 1

        if new_file is not None:
            new_file.write(line)

if new_file is not None:
    new_file.close()
