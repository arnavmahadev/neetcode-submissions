class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsDup = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            
            if (numsDup.containsKey(current)) {
                return new int[] {numsDup.get(current), i};
            }
            
            int difference = target - current;
            numsDup.put(difference, i);
        }
        return new int[2];
    }
}
