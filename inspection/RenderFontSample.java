import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.*;
import java.nio.file.*;
import java.util.Properties;
import javax.imageio.ImageIO;
import javax.swing.JLabel;

/** Headless Swing HTML preview; this does not replace an in-game layout test. */
public class RenderFontSample {
    private static Font load(Path path) throws Exception {
        try (InputStream in = Files.newInputStream(path)) {
            return Font.createFont(Font.TRUETYPE_FONT, in).deriveFont(17f);
        }
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 3) throw new IllegalArgumentException("Usage: package-root legacy-font output.png");
        Path resources = Path.of(args[0]).resolve("com/aof/resource/text");
        Properties p = new Properties();
        try (InputStream in = Files.newInputStream(resources.resolve("i18n/messages-zh.properties"))) { p.load(in); }
        Font oldFont = load(Path.of(args[1]));
        Font newFont = load(resources.resolve("font").resolve(p.getProperty("DEFAULTTEXT_FONT")));
        String prefix = "&nbsp;\u2022 ";
        String html = "<html><body><b>" + p.getProperty("SWAMPGLOBAL") + "</b><br>"
            + prefix + p.getProperty("S_SPEED").replace("{0}", "-20%") + "<br>"
            + prefix + "<i>" + p.getProperty("AFFECTS_ALL_UNITS_ON_BATTLEFIELD") + "</i><br>"
            + prefix + "<i>" + p.getProperty("S_ARE_UNAFFECTED").replace("{0}",
                String.join(", ", p.getProperty("PLANTS"), p.getProperty("ELEMENTALS"),
                    p.getProperty("GHOSTS"), p.getProperty("INCORPOREAL_UNITS"), p.getProperty("FLOATING_UNITS")))
            + "</i><br>" + p.getProperty("SWAMP_DESCRIPTION")
            + p.getProperty("GLOBALATTRIBUTE_TEMPORARY_BATTLEBOARD_DESCRIPTION")
            + "<br>" + prefix + "<i>English fallback: Plants, Elementals and Ghosts.</i>"
            + "</body></html>";
        BufferedImage image = new BufferedImage(900, 540, BufferedImage.TYPE_INT_RGB);
        Graphics2D graphics = image.createGraphics();
        graphics.setColor(new Color(24, 24, 24)); graphics.fillRect(0, 0, 900, 540);
        graphics.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
        Font[] fonts = {oldFont, newFont};
        for (int row = 0; row < fonts.length; row++) {
            int y = row * 260;
            graphics.setColor(Color.WHITE); graphics.setFont(new Font("Dialog", Font.BOLD, 16));
            graphics.drawString((row == 0 ? "Before: " : "After: ") + fonts[row].getFontName(), 20, y + 28);
            JLabel label = new JLabel(html); label.setFont(fonts[row]); label.setForeground(Color.WHITE);
            label.setVerticalAlignment(JLabel.TOP); label.setSize(860, 215);
            Graphics2D panel = (Graphics2D) graphics.create(20, y + 40, 860, 215);
            label.paint(panel); panel.dispose();
        }
        graphics.dispose();
        Path output = Path.of(args[2]);
        if (output.getParent() != null) Files.createDirectories(output.getParent());
        ImageIO.write(image, "png", output.toFile());
        System.out.println("Rendered Swing HTML font comparison: " + output);
    }
}
