def count_point_mutations(dna_str: str = "", dna_str_2: str = "") -> int:
    point_mutations = len(dna_str) - len(dna_str_2)
    str_range = len(dna_str) if len(dna_str) < len(dna_str_2) else len(dna_str_2)
    for idx in range(str_range):
        if dna_str[idx] != dna_str_2[idx]:
            point_mutations += 1
    return point_mutations


with open("test_files/counting_point_mutations.txt") as file:
    first_str = file.readline().strip()
    second_str = file.readline().strip()
    print(str(count_point_mutations(first_str, second_str)))
