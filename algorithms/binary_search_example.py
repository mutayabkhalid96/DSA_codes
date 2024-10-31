from binary_search import binary_recursive

def search_indices(number_list, findnumber):
  index = binary_recursive(number_list, findnumber)
  indices = [index]
  i = index - 1
  while i >= 0:
    if findnumber == number_list[i]:
      indices.append(i)
    else:
      break
    i = i - 1

  i = index + 1
  while i < len(number_list):
    if findnumber == number_list[i]:
      indices.append(i)
    else:
      break
    i = i + 1

  return sorted(indices)