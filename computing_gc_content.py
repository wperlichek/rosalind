from typing import Dict, Tuple

def get_highest_gc_content() -> Tuple[str, float]:
    string_id_with_highest_gc_count : str = ""
    highest_gc_content : float = 0.0
    curr_g : int = 0
    curr_c : int = 0
    total_nucleotides : int = 0
    curr_string_name : str = ""
    with open("test_files/computing_gc_content.txt") as File:
        for line in File:
            line = line.strip()
            if line[0] == ">":
                if curr_string_name == "":
                    curr_string_name = line[1::]

                if curr_c > 0 or curr_g > 0 and total_nucleotides > 0:
                    count_gc = curr_c + curr_g
                    curr_gc_content = round(count_gc / total_nucleotides, 3)
                    if curr_gc_content > highest_gc_content:
                        string_id_with_highest_gc_count = curr_string_name
                        highest_gc_content = curr_gc_content
                
                curr_g = 0
                curr_c = 0
                total_nucleotides = 0
                curr_string_name = line[1::]
            else:
                for ch in line:
                    if ch == "G":
                        curr_g += 1
                    elif ch == "C":
                        curr_c += 1
                    total_nucleotides += 1

    if curr_c > 0 or curr_g > 0 and total_nucleotides > 0:
        count_gc = curr_c + curr_g
        curr_gc_content = round(count_gc / total_nucleotides, 4)
        if curr_gc_content > highest_gc_content:
            string_id_with_highest_gc_count = curr_string_name
            highest_gc_content = curr_gc_content   

    return (string_id_with_highest_gc_count, highest_gc_content * 100)

print(get_highest_gc_content())