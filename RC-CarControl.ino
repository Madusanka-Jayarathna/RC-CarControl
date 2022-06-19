int t = 0; 
void setup() {
pinMode(12,OUTPUT);   //left motors reverse
pinMode(11,OUTPUT);   //right motors forward
pinMode(10,OUTPUT);   //right motors reverse
pinMode(13,OUTPUT);   
Serial.begin(9600); 
}

void loop() {
if(Serial.available()>0){
  t = Serial.read();
  Serial.println(t);
  }

if(t == 49){     
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
  digitalWrite(12,HIGH);
  digitalWrite(13,LOW);
  t = 49;
  }

else if (t==48){
  digitalWrite(10,HIGH);
  digitalWrite(11,LOW);
  digitalWrite(12,LOW);
  digitalWrite(13,HIGH);
  t = 48;
  }

else if(t==50){
  digitalWrite(10,HIGH);
  digitalWrite(11,LOW);
  digitalWrite(12,HIGH);
  digitalWrite(13,LOW);
  t = 50;
  }

else if(t==51){
  digitalWrite(10,LOW);
  digitalWrite(11,HIGH);
  digitalWrite(12,LOW);
  digitalWrite(13,HIGH);
  t = 51;
  }
  
else if(t==52){
  digitalWrite(10,LOW);
  digitalWrite(11,LOW);
  digitalWrite(12,LOW);
  digitalWrite(13,LOW);
  t = 52;
  }
}
