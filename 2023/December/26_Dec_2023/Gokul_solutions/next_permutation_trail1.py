def get_biggest_possible(nums):
  rev_sorted = sorted(nums, reverse=True)
  return rev_sorted

def get_next_permutation(nums):
  uniqu= sorted(list(set(nums)))
  sorted_nums = sorted(nums)
  for i in range(len(nums)):
    if nums(len(nums)-1-i)==sorted_nums(len(nums)-1-i):
      
def nextPermutations(nums):
  print("biggest possible: ", get_biggest_possible(nums))
  if nums == get_biggest_possible(nums):
    return sorted(nums)
  # the above covers the case where we get the biggest number in the permutation
  # and we need to return the smallest permutation

  else:


  return nums

print(nextPermutations([1,2,3]))