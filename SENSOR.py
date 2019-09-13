import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import MySQLdb
from datetime import datetime

sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BOARD)

pino_sensor = 25
con = MySQLdb.connect(host='localhost',user='root',passwd='root',db='iot')
con.select_db('iot')
cursor = con.cursor()

print("*** Lendo os valores de temperatura e umidade");

while(1):
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);

    if umid is not None and temp is not None:
        print ("temperatura = {0:0.1f} Umidade = {1:0.1f}n").format(temp, umid);
        print ("aguarda 5 segundos para efeturar nova leitura...n");
        sql = "INSERT INTO tabela(temperatura,umidade,data) values('%f','%f','%s')" % (temp,umid,datetime.now().strftime('%Y-%m-%d'))
        cursor.execute(sql)
        con.commit()
        time.sleep(5)
    else:
        print("falha ao ler dados do DHT11 !!");
        
        
