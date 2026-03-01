"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

"""

if __name__ == '__main__':
        for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        students.sort(key=lambda x: x[1])
        


        """
        const int redPin = 11;
const int greenPin = 12;
const int bluePin = 13;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  // 1. Red
  setColor(HIGH, LOW, LOW);
  delay(1000);

  // 2. Green
  setColor(LOW, HIGH, LOW);
  delay(1000);

  // 3. Blue
  setColor(LOW, LOW, HIGH);
  delay(1000);

  // 4. Yellow (Red + Green)
  setColor(HIGH, HIGH, LOW);
  delay(1000);

  // 5. Cyan (Green + Blue)
  setColor(LOW, HIGH, HIGH);
  delay(1000);

  // 6. Magenta (Red + Blue)
  setColor(HIGH, LOW, HIGH);
  delay(1000);

  // 7. White (All on)
  setColor(HIGH, HIGH, HIGH);
  delay(1000);

  // 8. Orange
  setColor(HIGH, HIGH, LOW);
  delay(500);

  // 9. Pink
  setColor(HIGH, LOW, HIGH);
  delay(500);

  // 10. Purple
  setColor(HIGH, LOW, HIGH);
  delay(500);
}

void setColor(int red, int green, int blue) {
  digitalWrite(redPin, red);
  digitalWrite(greenPin, green);
  digitalWrite(bluePin, blue);
}
        """

        """
        Here’s an example for an RGB LED (common cathode) connected like this:

Red → Pin 11

Green → Pin 12

Blue → Pin 13

Common → GND

(Each color pin should have a 220Ω resistor)

Works on an Arduino Uno.
        """