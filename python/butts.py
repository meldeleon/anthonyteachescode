def my_pop(my_list, index):
  return_item = my_list[index]
  del my_list[index]
  return return_item
def my_insert(my_list, index, value):
  list_1 = my_list[:index]
  list_2 = my_list[index:]
  list_1.append(value)
  my_list.clear()
  my_list.extend(list_1)
  my_list.extend(list_2)

def better_insert(my_list, index, value):
  my_list[index:index] = [value]
