import java.util.HashMap;

public class RomanToInt {
    public int romanToInt(String s) {
        int sum = 0;
        var romanDefinations = new HashMap<String, Integer>();
        romanDefinations.put("I", 1);
        romanDefinations.put("V", 5);
        romanDefinations.put("X", 10);
        romanDefinations.put("L", 50);
        romanDefinations.put("C", 100);
        romanDefinations.put("D", 500);
        romanDefinations.put("M", 1000);

        for (int counter = 0; counter < s.length(); counter++) {
            var currentChar = String.valueOf(s.charAt(counter));
            var value = romanDefinations.get(currentChar);
            if ((counter + 1) < s.length()) {
                var nextChar = String.valueOf(s.charAt(counter + 1));
                if (currentChar.equals("I") && (nextChar.equals("V") || nextChar.equals("X"))) {
                    value = romanDefinations.get(String.valueOf(s.charAt(counter + 1))) - 1;
                    counter += 1;
                } else if (currentChar.equals("X") && (nextChar.equals("L") || nextChar.equals("C"))) {
                    value = romanDefinations.get(String.valueOf(s.charAt(counter + 1))) - 10;
                    counter += 1;
                } else if (currentChar.equals("C") && (nextChar.equals("D") || nextChar.equals("M"))) {
                    value = romanDefinations.get(String.valueOf(s.charAt(counter + 1))) - 100;
                    counter += 1;
                }
            }

            sum += value;
        }


        return sum;
    }
}
