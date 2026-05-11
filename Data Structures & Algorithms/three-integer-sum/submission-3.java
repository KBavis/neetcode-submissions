class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        int i = 0; 

        List<List<Integer>> res = new ArrayList<>();

        Arrays.sort(nums);

        while (i < nums.length) {

            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {

                int currSum = nums[i] + nums[j] + nums[k];
                
                if (currSum == 0) {

                    res.add(new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k])));

                    j += 1;
                    while (j < k && nums[j] == nums[j - 1]){
                        j += 1;
                    }

                    k -= 1;
                    while (k > j && nums[k] == nums[k + 1]){
                        k -= 1;
                    }
                } else if (currSum > 0){
                    k -= 1;
                } else {
                    j += 1;
                }
            }

            i += 1;
            while (i < nums.length && nums[i] == nums[i - 1]){
                i += 1;
            }
        }

        return res;
    }
}
