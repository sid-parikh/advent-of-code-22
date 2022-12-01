import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day01 extends Solution {

    public Day01() throws IOException {
        super(1);
    }

    @Override
    public String partOne() {
        List<String> in = getInput();
        int current = 0;
        int max = Integer.MIN_VALUE;
        for (String s : in) {
            if (s.isBlank()) {
                max = Math.max(current, max);
                current = 0;
            } else {
                current += Integer.parseInt(s);
            }
        }
        return String.valueOf(max);
    }

    @Override
    public String partTwo() {
        List<Integer> elves = new ArrayList<>();
        List<String> in = getInput();
        int current = 0;
        for (String s : in) {
            if (s.isBlank()) {
                elves.add(current);
                current = 0;
            } else {
                current += Integer.parseInt(s);
            }
        }
        int answer = 0;
        Collections.sort(elves);
        for (int i = 1; i <= 3; i++) {
            answer += elves.get(elves.size() - i);
        }
        return String.valueOf(answer);
    }
}
