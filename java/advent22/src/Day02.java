import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day02 extends Solution {
    public Day02() throws IOException {
        super(2);
    }

    @Override
    public String partOne() {
        Map<Character, Character> wins = new HashMap<>();
        wins.put('A', 'Y');
        wins.put('B', 'Z');
        wins.put('C', 'X');

        List<String> input = getInput();
        int total = 0;
        for (String s : input) {
            char them = s.charAt(0);
            char you = s.charAt(2);
            int score = 0;
            switch (you) {
            case 'X' -> score += 1;
            case 'Y' -> score += 2;
            case 'Z' -> score += 3;
            default -> score += 0;
            }

            if (wins.get(them).equals(you)) {
                score += 6;
            } else if (them == you - ('X' - 'A')) {
                score += 3;
            }

            total += score;
            System.out.println(score);
        }
        return total + "";
    }

    @Override
    public String partTwo() {
        List<String> input = getInput();
        int total = 0;
        for (String s : input) {
            char them = s.charAt(0);
            char you = s.charAt(2);
            int score = 0;
            switch (you) {
            case 'X' -> {
                score += 0;
                switch (them) {
                case 'A' ->
                    // playing scissors
                    score += 3;
                case 'B' ->
                    // playing paper
                    score += 1;

                case 'C' ->
                    // scissors
                    score += 2;
                }
            }
            case 'Y' -> {
                score += 3;
                switch (them) {
                case 'A' ->
                    // playing rock
                    score += 1;
                case 'B' ->
                    // playing paper
                    score += 2;
                case 'C' ->
                    // scissors
                    score += 3;
                }
            }
            case 'Z' -> {
                score += 6;
                switch (them) {
                case 'A' ->
                    // playing paper
                    score += 2;
                case 'B' ->
                    // playing scissors
                    score += 3;
                case 'C' ->
                    // rock
                    score += 1;
                }
            }
            default -> score += 0;
            }

            total += score;
            System.out.println(score);
        }
        return total + "";
    }
}
