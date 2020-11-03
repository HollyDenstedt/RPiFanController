# RPiFanController
Basic Python Script For Fan Controller

I would reccomend running a basic stress test to see how hot your pi will get and set the temps from there. 

Run These Commands To Setup A Test

sudo apt-get install stress

wget https://raw.githubusercontent.com/ssvb/cpuburn-arm/master/cpuburn-a53.S

gcc -o cpuburn-a53 cpuburn-a53.S

while true; do vcgencmd measure_clock arm; vcgencmd measure_temp; sleep 10; done& stress -c 4 -t 900s
