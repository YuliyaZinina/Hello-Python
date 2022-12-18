# основные операции

def txt_import(file, phone_list):
    with open(file, 'r') as data:
        for line in data:
            if line != '\n':
                if '\n' in line:
                    phone_list.append(line[:-1])
                else:
                    phone_list.append(line)


def txt_export(file, phone_list):
    with open(file, 'w') as data:
        for i in range(0, len(phone_list)):
            if (i + 1) % 4 == 0:
                data.write(f'{phone_list[i]}\n\n')
            else:
                data.write(f'{phone_list[i]}\n')
