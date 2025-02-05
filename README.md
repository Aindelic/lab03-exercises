### java find all duplicates
```
import java.util.ArrayList;
import java.util.List;

public class DuplicateFinder {
    public static List<Integer> findDuplicates(int[] nums) {
        List<Integer> duplicates = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    if (!duplicates.contains(nums[i])) {
                        duplicates.add(nums[i]);
                    }
                    break;
                }
            }
        }

        return duplicates;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 2, 4, 5, 6, 6, 7};
        System.out.println(findDuplicates(nums)); // Output: [2, 6]
    }
}

```

### Different Approaches
```
Nested Loop:
    You start with an empty list, and use the outer loop to iterate through each number in the list, then the inner loop is used to compare each number to the chosen one, if a match is found, you check to see of its in the new list and if not you add it. This method can be slow for large lists as it has a big time complexity and has some redundant checks for duplicate numbers in the new list, however it is simple and easy to implement.  

```

```
Dictionary solution:
    This way uses an empty dictionary to store how many times a number appears, you iterate through the list and update the dictionary with numbers and count, then you loop through the dictionary and return all numbers with count values more than 1. this has a much better time complexity, as you only iterate through the list once, but dictionaries are harder to understand and implement. 

```