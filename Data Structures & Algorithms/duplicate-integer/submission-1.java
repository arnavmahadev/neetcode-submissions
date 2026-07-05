class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numsDup = new HashSet<Integer>();
        for (int num : nums) {
            if (numsDup.contains(num)){
                return true;
            }
            numsDup.add(num);
        }
        return false;
    }
}