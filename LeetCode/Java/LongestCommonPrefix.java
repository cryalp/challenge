import java.util.Arrays;

public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length < 1 || strs.length > 200) {
            return "";
        }

        var commonPrefix = strs[0].toCharArray();

        for (var counter1 = 0; counter1 < strs.length; counter1++) {
            if (strs[counter1].length() < 0 || strs[counter1].length() > 200) {
                continue;
            }

            for (var counter2 = 0; counter2 < commonPrefix.length; counter2++) {
                if (counter2 < strs[counter1].length() && strs[counter1].charAt(counter2) != commonPrefix[counter2]) {
                    commonPrefix = Arrays.copyOfRange(strs[counter1].toCharArray(), 0, counter2);
                    continue;
                } else if (counter2 == strs[counter1].length()) {
                    commonPrefix = Arrays.copyOfRange(strs[counter1].toCharArray(), 0, counter2);
                    break;
                }
            }
        }

        return new String(commonPrefix);
    }
}
