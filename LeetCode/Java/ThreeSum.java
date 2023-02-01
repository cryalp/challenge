import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        if (nums.length < 3 || nums.length > 3000) {
            return new ArrayList<List<Integer>>();
        }

        var threeSumList = new HashSet<List<Integer>>();
        var notZeroMap = new HashMap<Integer, Integer>();
        var dupedList = new HashSet<Integer>();

        for (var counter1 = 0; counter1 < nums.length - 2; counter1++) {
            if (!dupedList.add(nums[counter1])) {
                continue;
            }

            for (var counter2 = counter1 + 1; counter2 < nums.length; counter2++) {
                var index1 = nums[counter1];
                var index2 = nums[counter2];

                var sum = 0 - index1 - index2;
                if (notZeroMap.containsKey(sum) && counter1 == notZeroMap.get(sum)) {
                    var threeSum = new ArrayList<Integer>();
                    threeSum.add(index1);
                    threeSum.add(index2);
                    threeSum.add(sum);

                    Collections.sort(threeSum);
                    threeSumList.add(threeSum);
                }
                notZeroMap.put(nums[counter2], counter1);
            }
        }

        return new ArrayList<>(threeSumList);
    }
}
