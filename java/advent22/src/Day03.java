import java.io.IOException;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Day03 extends Solution {
    public Day03() throws IOException {
        super(3);
    }

    @Override
    public String partOne() {
        List<String> in = getInput();
        int total = 0;

        for (String s : in) {
            char[] firstHalf = s.substring(0, s.length() / 2).toCharArray();
            char[] secondHalf = s.substring(s.length() / 2).toCharArray();
            Set<Character> first = new HashSet<>();
            Set<Character> second = new HashSet<>();
            for (char c : firstHalf) {
                first.add(c);
            }
            for (char c : secondHalf) {
                second.add(c);
            }
            for (char c : first) {
                if (second.contains(c)) {
                    // Found it!
                    if (Character.isUpperCase(c)) {
                        total += c - 'A' + 27;
                    } else {
                        total += c - 'a' + 1;
                    }
                }
            }

        }
        return String.valueOf(total);

    }

    @Override
    public String partTwo() {
        List<String> in = getInput();
        int total = 0;

        for (int i = 0; i < in.size() - 2; i += 3) {
            char[] f = in.get(i).toCharArray();
            char[] s = in.get(i + 1).toCharArray();
            char[] t = in.get(i + 2).toCharArray();
            Set<Character> first = new HashSet<>();
            Set<Character> second = new HashSet<>();
            Set<Character> third = new HashSet<>();

            for (char c : f) {
                first.add(c);
            }
            for (char c : s) {
                second.add(c);
            }
            for (char c : t) {
                third.add(c);
            }
            for (char c : first) {
                if (second.contains(c) && third.contains(c)) {
                    // Found it!
                    if (Character.isUpperCase(c)) {
                        total += c - 'A' + 27;
                    } else {
                        total += c - 'a' + 1;
                    }
                }
            }

        }
        return String.valueOf(total);
    }
}
