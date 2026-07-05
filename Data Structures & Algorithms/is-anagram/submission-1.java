class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sTable = new HashMap<Character, Integer>();
        HashMap<Character, Integer> tTable = new HashMap<Character, Integer>();

        for (char c : s.toCharArray()) {
            sTable.put(c, sTable.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            tTable.put(c, tTable.getOrDefault(c, 0) + 1);
        }

        return sTable.equals(tTable);
    }
}
