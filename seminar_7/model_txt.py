# основные операции

def txt_import(file, phone_list):
    with open(file, 'r') as data:
        phone_list.append([])
        for line in data:
            if line != '\n':
                if '\n' in line:
                    phone_list[len(phone_list)-1].append(line[:-1])
                else:
                    phone_list[len(phone_list)-1].append(line)
            elif line == '\n':
                phone_list.append([])


def txt_export(file, phone_list):
    with open(file, 'w') as data:
        for i in range(0, len(phone_list)):
            for j in phone_list[i]:
                data.write(f'{j}\n')
            if i < len(phone_list)-1:
                data.write('\n')
