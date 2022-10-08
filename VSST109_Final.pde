import processing.pdf.*;

String file_name = "N_Simon_Says.csv";
Table t;
String[][] time_note;
Element[] els;

void setup() {
  size(1920, 1080, PDF, "Abs_Simon_Says.pdf");
  colorMode(HSB, 360, 100, 100);
  background(0);

  //load csv file and read the first element of the first row
  //which is the total number of notes in the file
  t = loadTable(file_name);
  TableRow first_row = t.getRow(0);
  int total_notes = first_row.getInt(0);
  TableRow last_row = t.getRow(total_notes);
  int totoal_seconds = last_row.getInt(0);

  //create a 2d string array for every primary element
  //containing two secondary elements, which represents
  //time at index 0 and a single note at index 1
  time_note = new String[total_notes][2];
  for (int i = 0; i < total_notes; i++) {
    TableRow curr_row = t.getRow(i + 1); //starts from the second row in the file
    String curr_time = curr_row.getString(0);
    String curr_note = curr_row.getString(1);
    time_note[i][0] = curr_time;
    time_note[i][1] = curr_note;
  }

  //declaring and initializing an array of Element objects
  els = new Element[total_notes];
  for (int i = 0; i < els.length; i++) {
    els[i] = new Element(float(time_note[i][0]), time_note[i][1], totoal_seconds);
  }

  //println(els.length, total_notes);
}


void draw() {
  //stroke(0, 100);
  for (Element el : els) {
    //el.showCircle();
    if (frameCount % 10 == 0) {
      el.overlaps(els);
    }
    el.update();
  }
  
  if (frameCount >= 1000) {
    println("Done.");
    exit();
  }
}
