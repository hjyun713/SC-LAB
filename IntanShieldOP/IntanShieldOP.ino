#include "IntanShield.h"

bool FirstChannelPwr = true;
// bool FirstChannelPwr = false;
bool SecondChannelPwr = true;
//bool SecondChannelPwr = false;
String serialout = "";
String serialconstants = "";
#define INTERRUPT_RATE 2000
bool average_energy_mode;
uint8_t data;
long rawdata;
int serialdata1;
int serialdata2;
uint8_t d1;
uint8_t d2;

enum Bandselect { LowCutoff10Hz, LowCutoff1Hz, LowCutoff100mHz };
Bandselect band_setting;

void setup() {
  SPI.begin();
  pinMode(chipSelectPin, OUTPUT);
  pinMode(15, INPUT);
  pinMode(16, INPUT);
  pinMode(17, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  
  digitalWrite(chipSelectPin, HIGH);
  ADCSRA &= ~PS_128;
  ADCSRA |= PS_16;
  Serial.begin(250000);
  SPI.beginTransaction(SPISettings(24000000, MSBFIRST, SPI_MODE0));
  delay(250);
  SendWriteCommand(0, 0b11011110);
  SendWriteCommand(1, 0b00100000);
  SendWriteCommand(2, 0b00101000);
  SendWriteCommand(3, 0b00000000);
  SendWriteCommand(4, 0b11011000);
  SendWriteCommand(5, 0b00000000);
  SendWriteCommand(6, 0b00000000);
  SendWriteCommand(7, 0b00000000);
  SendWriteCommand(8, 30);
  SendWriteCommand(9, 5);
  SendWriteCommand(10, 43);
  SendWriteCommand(11, 6);
  uint8_t R12, RL, RLDAC1, R13, ADCaux3en, RLDAC3, RLDAC2;
  band_setting = LowCutoff10Hz;

  switch(band_setting) {
    case LowCutoff10Hz:
      RL = 0;
      RLDAC1 = 5;
      ADCaux3en = 0;
      RLDAC3 = 0;
      RLDAC2 = 1;
    break;
    case LowCutoff1Hz:
      RL = 0;
      RLDAC1 = 44;
      ADCaux3en = 0;
      RLDAC3 = 0;
      RLDAC2 = 6;
    break;
  case LowCutoff100mHz:
      RL = 0;
      RLDAC1 = 16;
      ADCaux3en = 0;
      RLDAC3 = 1;
      RLDAC2 = 60;
    break;
}
  R12 = ((RL << 7) | RLDAC1);
  R13 = (ADCaux3en << 7) | (RLDAC3 << 6) | RLDAC2;
  SendWriteCommand(12, R12);
  SendWriteCommand(13, R13);
  SendWriteCommand(14, 0b00000000);
  SendWriteCommand(15, 0b00000000);
  SendWriteCommand(16, 0);
  SendWriteCommand(17, 0);
  SetAmpPwr(FirstChannelPwr, SecondChannelPwr);
  Calibrate();
  SendConvertCommandH(FIRSTCHANNEL);
  SendConvertCommandH(SECONDCHANNEL);
  SendConvertCommand(FIRSTCHANNEL);
  SendConvertCommand(SECONDCHANNEL);
  pinMode(2, OUTPUT);
  Wire.begin();
  Wire.beginTransmission(56);
  Wire.write(0b11110000);
  Wire.write(0b00001100);
  Wire.endTransmission();
  digitalWrite(2, LOW);
  analogReference(EXTERNAL);
  ASSR &= ~(_BV(EXCLK) | _BV(AS2));
  cli();
  TCCR1B = (TCCR1B & ~_BV(WGM13)) | _BV(WGM12);
  TCCR1A = TCCR1A & ~(_BV(WGM11) | _BV(WGM10));
  TCCR1B = (TCCR1B & ~(_BV(CS12) | _BV(CS11))) | _BV(CS10);
  OCR1A = F_CPU / INTERRUPT_RATE;
  TIMSK1 |= _BV(OCIE1A);
  sei();
}

void loop() {
  if (digitalRead(15) == HIGH) {
    average_energy_mode = true;
    TWSR = TWSR | 0b11;
    TWBR = 40;
  } else {
    average_energy_mode = false;
    TWSR = TWSR & 0b11111100;
    TWBR = 30;
  }

  if (average_energy_mode == true) {
    if (LowGainMode())
      serialconstants = ",4400,0,50";
    else
      serialconstants = ",1100,0,50";
    cli();
    rawdata = ReadAccumulatorData(FIRSTCHANNEL);
    sei();
    if (!FirstChannelPwr)
      rawdata = 0;
    rawdata = rawdata / 20;
    serialdata1 = (int) (rawdata * 0.195);
    data = ScaleForDAC_ACC(rawdata);
    d1 = 0b00000000;
    d2 = 0b00000000;
    d1 = d1 | (data >> 4);
    d2 = d2 | (data << 4);
    Wire.beginTransmission(56);
    Wire.write(uint8_t(d1));
    Wire.write(uint8_t(d2));
    Wire.endTransmission();
    cli();
    rawdata = ReadAccumulatorData(SECONDCHANNEL);
    sei();
    if (!SecondChannelPwr)
      rawdata = 0;
    rawdata = rawdata / 20;
    serialdata2 = (int) (rawdata * 0.195);
    serialout = serialout + String(serialdata1) + "," + String(serialdata2) + serialconstants;
    Serial.println(serialout);
    serialout = "";
    data = ScaleForDAC_ACC(rawdata);
    d1 = 0b00010000;
    d2 = 0b00000000;
    d1 = d1 | (data >> 4);
    d2 = d2 | (data << 4);
    Wire.beginTransmission(56);
    Wire.write(uint8_t(d1));
    Wire.write(  uint8_t(d2));
    Wire.endTransmission();   
  }

  else {
    if (LowGainMode())
      serialconstants = ",2200,-2200";
    else
      serialconstants = ",550,-550,50";
    cli();
    rawdata = ReadChannelData(FIRSTCHANNEL);
    sei();
    if (!FirstChannelPwr)
      rawdata = 0;
    serialdata1 = (int) (rawdata * 0.195);
    data = ScaleForDAC(rawdata);
    d1 = 0b00000000;
    d2 = 0b00000000;
    d1 = d1 | (data >> 4);
    d2 = d2 | (data << 4);
    Wire.beginTransmission(56);
    Wire.write(uint8_t(d1));
    Wire.write(uint8_t(d2));
    Wire.endTransmission();
    cli();
    rawdata = ReadChannelData(SECONDCHANNEL);
    sei();
    if (!SecondChannelPwr)
      rawdata = 0;
    serialdata2 = (int) (rawdata * 0.195);
    serialout = serialout + String(serialdata1) + "," + String(serialdata2) + serialconstants;
    Serial.println(serialout);
    serialout = "";
    data = ScaleForDAC(rawdata);
    d1 = 0b00010000;
    d2 = 0b00000000;
    d1 = d1 | (data >> 4);
    d2 = d2 | (data << 4);
    Wire.beginTransmission(56);
    Wire.write(uint8_t(d1));
    Wire.write(uint8_t(d2));
    Wire.endTransmission();
  }
}