package StringArray;

import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {
        int[] nums = {2, 8, 11, 21};
        int target = 10;

        TwoSum twoSum = new TwoSum();
        int[] solutionFor = twoSum.solveFor(nums, target);
        int[] solutionMap = twoSum.solveMap(nums, target);

        System.out.println(solutionFor[0] + " " + solutionFor[1]);
        for(int i:solutionMap){
            System.out.print(i + " ");
        }

    }

    public int[] solveFor(int[] nums, int target){
        int[] result = new int[2];

        for (int i = 0; i < nums.length - 1; i++){
            for (int j = 1; j < nums.length; j++){
                if (nums[i] + nums[j] == target){
                    result[0] = i;
                    result[1] = j;

                    return result;
                }
            }
        }

        return result;
    }

    public int[] solveMap(int[] nums, int target){
        int[] result = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i<nums.length; i++){
            if (map.containsKey(nums[i])){
                result[0] = map.get(nums[i]);
                result[1] = i;

                return result;
            }
            else{
                map.put(target - nums[i], i);
            }
        }

        return result;
    }

}
