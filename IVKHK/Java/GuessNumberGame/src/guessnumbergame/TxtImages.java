/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package guessnumbergame;

/**
 *
 * @author pupil
 */
public class TxtImages {
        public static String getWinImage() {
            StringBuilder image = new StringBuilder();
            image.append("░░░░░░░░░░░░░░░░░░░░\n");
            image.append("░░░░░░░░░░░░░░░░░░░░\n");
            image.append("░░░░░▄▀▀▀▄░░░░░░░░░░\n");
            image.append("▄███▀░◐░░░▌░░░░░░░░░\n");
            image.append("░░░░▌░░░░░▐░░░░░░░░░\n");
            image.append("░░░░▐░░░░░▐░░░░░░░░░\n");
            image.append("░░░░▌░░░░░▐▄▄░░░░░░░\n");
            image.append("░░░░▌░░░░▄▀▒▒▀▀▀▀▄\n");
            image.append("░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄\n");
            image.append("░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄\n");
            image.append("░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄\n");
            image.append("░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄\n");
            image.append("░░░░░░░░░░░▌▌░▌▌░░░░░\n");
            image.append("░░░░░░░░░░░▌▌░▌▌░░░░░\n");
            return image.toString();
    }
        public static String getLoseImage() {
            StringBuilder image = new StringBuilder();
            image.append("███████████████████████████\n");
            image.append("███████▀▀▀░░░░░░░▀▀▀███████\n");
            image.append("████▀░░░░░░░░░░░░░░░░░▀████\n");
            image.append("███│░░░░░░░░░░░░░░░░░░░│███\n");
            image.append("██▌│░░░░░░░░░░░░░░░░░░░│▐██\n");
            image.append("██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n");
            image.append("██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n");
            image.append("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n");
            image.append("██▌░│██████▌░░░▐██████│░▐██\n");
            image.append("███░│▐███▀▀░░▄░░▀▀███▌│░███\n");
            image.append("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n");
            image.append("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n");
            image.append("████▄─┘██▌░░░░░░░▐██└─▄████\n");
            image.append("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n");
            image.append("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n");
            image.append("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n");
            image.append("██████████▄▄▄▄▄▄▄██████████\n");
            image.append("███████████████████████████\n");
            return image.toString();
        }
}
