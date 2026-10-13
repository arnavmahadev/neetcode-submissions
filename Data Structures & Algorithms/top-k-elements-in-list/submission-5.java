class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> numFreq = new HashMap<>();
        List<List<Integer>> buckets = new ArrayList<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i <= nums.length; i++) {
            buckets.add(new ArrayList<>());
        }

        for (int num : nums) {
            numFreq.put(num, numFreq.getOrDefault(num, 0) + 1);
        }


        for (Map.Entry<Integer, Integer> entry : numFreq.entrySet()) {
            int num = entry.getKey();
            int val = entry.getValue();

            buckets.get(val).add(num);
        }

        for (int freq = buckets.size() - 1; freq >= 0 && result.size() < k; freq--) {
            for (int num : buckets.get(freq)) {
                result.add(num);
            if (result.size() == k) break;
            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray();

    }
}
