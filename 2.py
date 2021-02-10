old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [old_list[i] for i in range(1, len(old_list)) if old_list[i] > old_list[i - 1]]
print(new_list)
