class Solution {
    public int prefixCount(String[] words, String pref) {
        int count=0;
        int l1 = pref.length();
        for(String word: words){
            // if(word.length()<l1){
            //     continue;
            // }

            // if(word.substring(0,l1).equals(pref)){
            //     count++;
            // }

            if (word.startsWith(pref)){
                count+=1;
            }
        }

        return count;
    }
}