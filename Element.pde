class Element {
  float time;
  float x;
  float y = height/2;
  String note;
  int total_seconds;
  float xoff = 0;
  float yVel = random(-0.5, 0.5);
  int seed = int(random(200));
  int abs_degree;
  int interval;

  Element(float temp_time, String temp_note, int temp_ts) { 
    time = temp_time;
    note = temp_note;
    total_seconds = temp_ts;
    x = map(time, 0, total_seconds, 100, 1820);
    
    if(match(note, "C") != null){
      abs_degree = 0;
    } else if(match(note, "C") != null){
      abs_degree = 0;
    } else if(match(note, "G") != null){
      abs_degree = 30;
    } else if(match(note, "D") != null){
      abs_degree = 60;
    } else if(match(note, "A") != null){
      abs_degree = 90;
    } else if(match(note, "E") != null){
      abs_degree = 120;
    } else if(match(note, "B") != null){
      abs_degree = 150;
    } else if(match(note, "g") != null){
      abs_degree = 180;
    } else if(match(note, "d") != null){
      abs_degree = 210;
    } else if(match(note, "a") != null){
      abs_degree = 240;
    } else if(match(note, "e") != null){
      abs_degree = 270;
    } else if(match(note, "b") != null){
      abs_degree = 300;
    } else if(match(note, "F") != null){
      abs_degree = 330;
    } else {
      abs_degree = 0; //FIXME
    }
  }

  void showCircle() {
    circle(x, y, 10);
  }

  void overlaps(Element[] others) {
    for (int i = 0; i < others.length; i++) {
      float d = dist(x, y, others[i].x, others[i].y);

      if (d > 5 && d < 15) {
        interval = abs(abs_degree - others[i].abs_degree);
        int hue = (interval + 120)%360;
        stroke(hue, interval, 75, 100);
        line(x, y, (x + others[i].x)/2, (y + others[i].y)/2);
      }
    }
  }
  
  void update() {
    y += yVel;
    noiseSeed(seed);
    x += map(noise(xoff), 0, 1, -1, 1);
    xoff += 0.01;
  }
}
