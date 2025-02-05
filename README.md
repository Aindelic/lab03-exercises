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