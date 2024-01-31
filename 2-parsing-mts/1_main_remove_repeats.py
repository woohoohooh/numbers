region = 'yugra'

def remove_duplicates(input_file, output_file):
    unique_lines = set()

    with open(input_file, 'r', encoding='utf8') as input_f:
        input_f.readline()  # Пропускаем первую строку, если это заголовок

        for line in input_f:
            line = line.strip()
            if line:  # Пропускаем пустые строки
                unique_lines.add(line)

    with open(output_file, 'w', encoding='utf8') as output_f:
        for unique_line in unique_lines:
            output_f.write(f'{unique_line}\n')

    print(f"Уникальные строки из {input_file} записаны в {output_file}")

remove_duplicates(f'{region}_new.txt', f'{region}_clear.txt')

with open(f'{region}_good.txt', 'w', encoding='utf8') as f:
    f.write('')