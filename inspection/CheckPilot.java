import java.awt.Font;
import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.*;
import java.util.*;

public class CheckPilot {
    private static final List<String> FONT_KEYS = List.of(
        "INTROTEXT_FONT", "BUTTONTEXT_FONT", "EFFECTTEXT_FONT", "DEFAULTTEXT_FONT");

    private static void checkGlyphs(Font font, String text, String context) throws Exception {
        // Control characters are layout controls, not printable glyphs. NBSP is not skipped.
        for (int cp : text.codePoints().distinct().toArray()) {
            if (!Character.isISOControl(cp) && !font.canDisplay(cp)) {
                throw new Exception(String.format("Missing glyph U+%04X in %s; font=%s style=%d",
                    cp, context, font.getFontName(), font.getStyle()));
            }
        }
    }

    public static void main(String[] args) throws Exception {
        if (args.length < 1) {
            throw new IllegalArgumentException("Usage: CheckPilot.java package-root [English-properties ...]");
        }
        Path root = Path.of(args[0]);
        Path resources = root.resolve("com/aof/resource/text");
        Properties ui = new Properties();
        try (InputStream input = Files.newInputStream(resources.resolve("i18n/messages-zh.properties"))) {
            ui.load(input);
        }
        Map<String, Font> fonts = new LinkedHashMap<>();
        for (String key : FONT_KEYS) {
            String filename = ui.getProperty(key);
            if (filename == null || filename.isBlank() || filename.contains("/") || filename.contains("\\")) {
                throw new Exception("Missing or invalid font resource: " + key);
            }
            if (!fonts.containsKey(filename)) {
                try (InputStream input = Files.newInputStream(resources.resolve("font").resolve(filename))) {
                    fonts.put(filename, Font.createFont(Font.TRUETYPE_FONT, input));
                }
            }
        }
        List<Font> styles = new ArrayList<>();
        for (Font base : fonts.values()) {
            for (int style : new int[]{Font.PLAIN, Font.BOLD, Font.ITALIC, Font.BOLD | Font.ITALIC}) {
                Font font = base.deriveFont(style, 14f);
                // Engine inserts this tooltip prefix outside translated properties values.
                checkGlyphs(font, "\u00a0\u2022 ", "engine tooltip prefix (NBSP and bullet)");
                styles.add(font);
            }
        }
        int count = 0;
        try (var files = Files.list(resources.resolve("i18n"))) {
            for (Path file : files.filter(p -> p.toString().endsWith(".properties")).sorted().toList()) {
                Properties props = new Properties();
                try (InputStream input = Files.newInputStream(file)) { props.load(input); }
                if (!"zh".equals(props.getProperty("LOCALE"))) throw new Exception("Wrong locale in " + file);
                for (String key : props.stringPropertyNames()) {
                    for (Font font : styles) checkGlyphs(font, props.getProperty(key), file.getFileName() + ":" + key);
                }
                count += props.size();
            }
        }
        int fallbackCount = 0;
        for (int sourceIndex = 1; sourceIndex < args.length; sourceIndex++) {
            Path sourcePath = Path.of(args[sourceIndex]);
            String sourceName = sourcePath.getFileName().toString();
            if (!sourceName.endsWith("-en.properties")) throw new IllegalArgumentException("Expected English resource: " + sourcePath);
            Path localPath = resources.resolve("i18n").resolve(sourceName.replace("-en.properties", "-zh.properties"));
            Properties localized = new Properties();
            try (InputStream input = Files.newInputStream(localPath)) { localized.load(input); }
            Properties english = new Properties();
            // Extracted English reference uses Windows-1252, as documented by the game guide.
            try (Reader input = Files.newBufferedReader(sourcePath, Charset.forName("windows-1252"))) {
                english.load(input);
            }
            int resourceFallbackCount = 0;
            for (String key : english.stringPropertyNames()) {
                if (!localized.containsKey(key)) {
                    for (Font font : styles) checkGlyphs(font, english.getProperty(key), sourceName + " English fallback:" + key);
                    fallbackCount++;
                    resourceFallbackCount++;
                }
            }
            System.out.println("PASS: " + sourceName + ": " + resourceFallbackCount + " English fallback entries checked.");
        }
        System.out.println("PASS: Java Properties decoded " + count + " entries; " + fonts.keySet()
            + " cover translated text and engine tooltip symbols in plain/bold/italic/bold-italic.");
        System.out.println(args.length > 1 ? "PASS: " + fallbackCount + " English fallback entries checked across supplied resources."
            : "NOTE: English fallback not checked; supply extracted English resource files as additional arguments.");
    }
}
