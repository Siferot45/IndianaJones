
def find_password(n):
    # ���������� ��� �������� ������
    result = ""

    # ������� ���� �� ������� �����
    for i in range(1, n):
        # ���������� ���� �� ������� �����, ������� � i+1, ����� �������� ������������
        for j in range(i + 1, n):
            # �������� ���������
            if n % (i + j) == 0:  
                # ��������� ���� � ������ ����������
                result += str(i) + str(j)

    return result


for num in range(3, 21):
    password = find_password(num)
    print(f" Number {num} - password {password}")
