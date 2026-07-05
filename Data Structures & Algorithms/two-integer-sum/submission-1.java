class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsDup = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];

            if (numsDup.containsKey(current)) {
                return new int[] {numsDup.get(current), i};
            }

            int diff = target - current;
            numsDup.put(diff, i);
        }
        return new int[2];
    }
}
