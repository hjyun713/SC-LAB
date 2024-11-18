#include <Servo.h>
#include <ESP8266WiFi.h>

Servo servo[5];

const char* ssid = "d3dlab3G";    // Wi-Fi 네트워크 이름
const char* password = "029408637";    // Wi-Fi 네트워크 비밀번호
WiFiClient client;

IPAddress serverIP(192, 168, 2, 186);   // 서버의 IP 주소
const uint16_t serverPort = 7015;   // 서버의 포트 번호

void act_idle();
void act_rock();
void act_paper();
void act_scissors();

void setup() {
  Serial.begin(250000);

  // Set servo attach 3~7 
  servo[0].attach(5);
  servo[1].attach(4);
  servo[2].attach(14);
  servo[3].attach(12);
  servo[4].attach(13);
  
  act_idle(); //robot_standby
  // delay(10);
  // Wi-Fi 연결
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    // delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  // delay(3000);
}

void loop() {

  if (!client.connected()) {    // 클라이언트가 연결되어 있지 않으면, 서버에 연결
    Serial.println("Connecting to server...");
    // delay(10000);
    if (client.connect(serverIP, serverPort)) {
      Serial.println("Connected to server");
      // delay(1000);
      //client.println("client-connection");   // 서버에 데이터 전송
    } else {
      Serial.println("Connection to server failed");
    }
  }

  // main-robot-action
  if (client.available()) {    // 서버에서 데이터 수신 // 
    // delay(1000);
    int data = client.readStringUntil('\r').toInt();
    Serial.println("Received from server: " + String(data));

    //branch
    switch (data) {
      //Idle
    case 0:
      act_idle();
      break;
      // Paper
    case 1:
      act_rock();
      break;
      //Scissors
    case 2:
      act_paper();
      break;
      // Rock
    case 3:
      act_scissors();
      break;
    }
    // delay(1000);
  }
}


void act_idle()
{
  for (int i = 0; i < 5; i++) {
    if(i != 1 && i != 2 && i != 3)
      servo[i].write(60);
  }
  servo[1].write(120);
  servo[2].write(120);
  servo[3].write(120);
}

void act_rock()
{
  for (int i = 0; i < 5; i++) {
    if (i == 1 || i == 2 || i == 3)
      servo[i].write(0);
    else
      servo[i].write(180);
  }
}

void act_paper()
{
  for (int i = 0; i < 5; i++) {
    if (i==0 || i==4)
      servo[i].write(0);
    else
      servo[i].write(180);
  }
}

void act_scissors()
{
  for (int i = 0; i < 5; i++) {
    if(i == 3)
      servo[i].write(0);
    else
      servo[i].write(180);
  }
}
