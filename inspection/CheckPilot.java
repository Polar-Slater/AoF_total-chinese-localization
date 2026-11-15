import java.awt.Font;
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class CheckPilot {
    public static void main(String[] args) throws Exception {
        Path root = Path.of(args[0]);
        Font font;
        try (InputStream input = Files.newInputStream(root.resolve("com/aof/resource/text/font/simhei.ttf"))) {
            font = Font.createFont(Font.TRUETYPE_FONT, input);
        }
        int count = 0;
        try (var files = Files.list(root.resolve("com/aof/resource/text/i18n"))) {
            for (Path file : files.toList()) {
                Properties props = new Properties();
                try (InputStream input = Files.newInputStream(file)) { props.load(input); }
                if (!"zh".equals(props.getProperty("LOCALE"))) throw new Exception("Wrong locale");
                for (String value : props.stringPropertyNames()) {
                    String text = props.getProperty(value);
                    if (font.canDisplayUpTo(text) >= 0) throw new Exception("Missing glyph in " + value);
                }
                count += props.size();
            }
        }
        System.out.println("PASS: Java Properties decoded " + count + " entries; font covers every pilot character.");
    }
}
