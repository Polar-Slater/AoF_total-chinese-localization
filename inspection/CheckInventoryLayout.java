import java.awt.*;
import java.io.InputStream;
import java.nio.file.*;
import java.util.Properties;
import java.text.MessageFormat;
import javax.swing.*;

/** Regression fixture for the inventory's fixed-size GridBag layout.
 * Does not launch the game or read/write saves. Minimum sizes are illustrative;
 * the assertions check that Swing retains the full preferred panel dimensions.
 */
public class CheckInventoryLayout {
    public static void main(String[] args) throws Exception {
        if (args.length < 1 || args.length > 2)
            throw new IllegalArgumentException("Usage: CheckInventoryLayout.java package-root [original-font.ttf]");
        Path root = Path.of(args[0]);
        Properties messages = new Properties();
        try (InputStream in = Files.newInputStream(root.resolve("com/aof/resource/text/i18n/messages-zh.properties"))) {
            messages.load(in);
        }
        Path fontPath = root.resolve("com/aof/resource/text/font").resolve(messages.getProperty("BUTTONTEXT_FONT"));
        Font font = Font.createFont(Font.TRUETYPE_FONT, fontPath.toFile());
        SwingUtilities.invokeAndWait(() -> {
            for (String amount : new String[]{"0", "623", "123456789"})
                verify(font.deriveFont(Font.BOLD, 18f), MessageFormat.format(messages.getProperty("TREASURE_S_GP"), amount), false);
        });
        if (args.length == 2) {
            Font original = Font.createFont(Font.TRUETYPE_FONT, Path.of(args[1]).toFile());
            if (original.getFamily().equals(font.getFamily()))
                throw new IllegalArgumentException("Distinct font families are needed to avoid Java metrics-cache collisions.");
            SwingUtilities.invokeAndWait(() -> verify(original.deriveFont(Font.BOLD, 18f), MessageFormat.format(messages.getProperty("TREASURE_S_GP"), "623"), true));
        }
    }

    private static void verify(Font font, String text, boolean expectCollapse) {
        JTextArea treasure = new JTextArea(text);
        treasure.setFont(font);
        treasure.setBorder(BorderFactory.createEmptyBorder(4, 4, 4, 4));
        treasure.setSize(590, 25);
        JPanel container = new JPanel(new GridBagLayout());
        container.setSize(950, 500);
        JPanel hero = new JPanel();
        hero.setPreferredSize(new Dimension(350, 500));
        hero.setMinimumSize(new Dimension(220, 295));
        JTabbedPane items = new JTabbedPane();
        items.setPreferredSize(new Dimension(590, 467));
        items.setMinimumSize(new Dimension(40, 200));
        GridBagConstraints c = new GridBagConstraints();
        c.gridx = 0; c.gridy = 0; c.gridwidth = 1; c.gridheight = 2;
        container.add(hero, c);
        c.gridx = 2; c.gridy = 0; c.gridheight = 1;
        c.insets = new Insets(0, 20, 0, 0); c.anchor = GridBagConstraints.WEST;
        container.add(treasure, c);
        c.gridx = 1; c.gridy = 1; c.gridwidth = 2;
        c.insets = new Insets(0, 10, 0, 0); c.anchor = GridBagConstraints.SOUTH;
        container.add(items, c);
        container.doLayout();
        boolean fullSize = items.getSize().equals(new Dimension(590, 467)) &&
                           hero.getSize().equals(new Dimension(350, 500));
        int requiredHeight = treasure.getPreferredSize().height + 467;
        if (expectCollapse ? fullSize || requiredHeight <= 500 : !fullSize || requiredHeight > 500)
            throw new AssertionError("Unexpected layout: requiredHeight=" + requiredHeight + ", items=" + items.getSize());
        System.out.printf("PASS: %s; required height %d/500; item panel %dx%d.%n",
                expectCollapse ? "original-font collapse reproduced" : "full-size inventory retained",
                requiredHeight, items.getWidth(), items.getHeight());
    }
}
