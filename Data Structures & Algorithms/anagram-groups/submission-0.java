class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groups = new HashMap<>();
        
        for (String str : strs) {
            int[] freq = new int[26];
            for (char c : str.toCharArray()) {
                freq[c - 'a']++;
            }
            String key = Arrays.toString(freq);
            groups.putIfAbsent(key, new ArrayList<>());
            groups.get(key).add(str);
        }

        return new ArrayList<>(groups.values());
    }
}
