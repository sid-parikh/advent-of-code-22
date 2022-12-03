import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * This is a generic Solution class that all daily solutions will extend. This class provides basic methods to get the
 * day's input and to print the output to sysout.
 */
public abstract class Solution {


    /**
     * The numerical value of the day that is being solved. It is used to generate the filename to pull input from.
     */
    private final int DAY;
    private final List<String> in;

    public Solution(int day) throws IOException {
        this.DAY = day;
        // For some reason, even though there are provided methods to get a resource as a file, it would never find
        // the file when I used those. Only getResourceAsStream worked. Unfortunately, getResourceAsStream hides the
        // FileNotFoundException and reverts it to an NPE, which is far less useful. I had to throw and catch it to add
        // an error message explaining it is probably because the input file is not found.
        String filepath = "inputs/day" + String.format("%02d", DAY) + ".txt";
        in = new ArrayList<>();

        try (InputStream is = getClass().getClassLoader().getResourceAsStream(filepath)) {
            if (is == null) {
                throw new FileNotFoundException("Cannot Find Input File!");
            }

            Scanner scan = new Scanner(is);
            while (scan.hasNextLine()) {
                in.add(scan.nextLine());
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.out.println((new Day02()).getSolution());
    }

    /**
     * Gets the input from the file's location. Now with relative filepaths and a real resources folder.
     *
     * @return the puzzle input as a list of rows
     * @throws NullPointerException if input file is not found
     */
    protected final List<String> getInput() {
        return in;
    }

    /**
     * Returns a String, formatted for sysout, that contains the results of the solution for that day.
     */
    public String getSolution() {
        // Temps
        double start;
        double elapsed;

        // Run and time part one
        start = System.nanoTime();
        String resOne = partOne();
        elapsed = System.nanoTime() - start;
        resOne += String.format(" (%.4f ms)", elapsed / 1_000_000.0);

        // Run and time part two
        start = System.nanoTime();
        String resTwo = partTwo();
        elapsed = System.nanoTime() - start;
        resTwo += String.format(" (%.4f ms)", elapsed / 1_000_000.0);

        return String.format("---Day %02d---\nStar 1: %s\nStar 2: %s\n\n", DAY, resOne, resTwo);
    }

    /**
     * Solves part one of the day's puzzle.
     *
     * @return the answer as a String (so it doesn't have to be either int or long)
     */
    public abstract String partOne();

    /**
     * Solves part two of the day's puzzle.
     *
     * @return the answer as a String (so it doesn't have to be either int or long)
     */
    public abstract String partTwo();
}