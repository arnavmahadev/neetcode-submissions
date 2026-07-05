class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dups = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int curr = nums[i];
            int diff = target - curr;

            if (dups.containsKey(curr)) {
                return new int[]{dups.get(curr), i};
            }

            dups.put(diff, i);
        }

        return new int[2];
    }
}
