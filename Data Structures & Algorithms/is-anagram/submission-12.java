class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        Map<Character, Integer> sTable = new HashMap<>();
        Map<Character, Integer> tTable = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            sTable.put(s.charAt(i), sTable.getOrDefault(s.charAt(i), 1) + 1);
            tTable.put(t.charAt(i), tTable.getOrDefault(t.charAt(i), 1) + 1);
        }
        return sTable.equals(tTable);
    }
}
