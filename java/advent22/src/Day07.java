import java.io.IOException;
import java.util.HashMap;
import java.util.List;

public class Day07 extends Solution {

    private long totalSize = 0;
    private long starTwoAns = Long.MAX_VALUE;
    private final Directory root = new Directory( null);
    private long starOneAns = 0;

    public Day07() throws IOException {
        super(7);
    }

    @Override
    public String partOne() {
        // Parse input
        List<String> lines = getInput();
        // Start at root of tree
        Directory curr = root;
        for (int i = 1; i < lines.size(); i++) {
            String line = lines.get(i);
            // Listing children
            if (line.strip().equals("$ ls")) {
                // Keep going until end of output
                int j = i + 1;
                while (j < lines.size() && !lines.get(j).startsWith("$")) {
                    line = lines.get(j);
                    // New Subdirectory
                    if (line.startsWith("dir")) {
                        String name = line.strip().substring(4);
                        curr.dirs.put(name, new Directory(curr));
                    } else {
                        long size = Long.parseLong(line.substring(0, line.indexOf(' ')));
                        curr.size += size;
                    }

                    j++;
                }
                i = j - 1;

                // Change current directory
            } else if (line.startsWith("$ cd")) {
                String newDir = line.substring(5).strip();
                if (newDir.equals("..")) {
                    curr = curr.parent;
                } else {
                    curr = curr.dirs.get(newDir);
                }
            }
        }

        // DFS
        totalSize = dfsPartOne(root);
        return String.valueOf(starOneAns);
    }

    @Override
    public String partTwo() {
        // Target space is needed - (total - used);
        long targetSpace = 30000000 - (70000000 - totalSize);
        dfsPartTwo(root, targetSpace);
        return String.valueOf(starTwoAns);
    }

    /**
     * DFS through Directories for Star One. Saves the answer into starOneAns.
     * @param c root of directory tree
     * @return total size of directory tree
     */
    private long dfsPartOne(Directory c) {
        if (c == null) {
            return 0;
        }
        long sum = c.size;
        for (Directory d : c.dirs.values()) {
            sum += dfsPartOne(d);
        }
        if (sum <= 100000) {
            // Sum of all directories smaller than 100,000
            starOneAns += sum;
        }
        return sum;
    }

    /**
     * DFS through directories for Star Two. Saves the answer into starTwoAns.
     * @param c root of directory tree
     * @param target minimum size of directory to look for
     * @return size of directory tree
     */
    private long dfsPartTwo(Directory c, long target) {
        if (c == null) {
            return 0;
        }
        long sum = c.size;
        for (Directory d : c.dirs.values()) {
            sum += dfsPartTwo(d, target);
        }
        if (sum >= target) {
            starTwoAns = Math.min(sum, starTwoAns);
        }
        return sum;
    }


    /**
     * Node class. Reference to parent and all child directories.
     */
    private static class Directory {
        Directory parent;
        HashMap<String, Directory> dirs = new HashMap<>();
        long size = 0;

        Directory(Directory parent) {
            this.parent = parent;
        }
    }
}
