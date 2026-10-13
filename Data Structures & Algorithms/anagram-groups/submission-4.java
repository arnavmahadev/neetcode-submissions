class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagramMap = new HashMap<>();

        for (String str : strs) {
            int[] charFreq = new int[26];
            for (char c : str.toCharArray()) {
                charFreq[c - 'a'] += 1;
            }
            String key = Arrays.toString(charFreq);
            if (anagramMap.containsKey(key)) {
                anagramMap.get(key).add(str);
            } else {
                anagramMap.put(key, new ArrayList<>());
                anagramMap.get(key).add(str);
            }
        }

        return new ArrayList<>(anagramMap.values());
    }
}
