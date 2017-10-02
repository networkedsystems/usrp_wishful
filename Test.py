import time
from IBFD_agent import *

print('Start')
Agent = IBFDAgent(ip_address='10.33.136.138', ip_port = 5022)
Agent.device_address(10)
Agent.set_tx_power(9)
Agent.set_rx_gain(1)
Agent.set_collision_detection('reset')
Agent.start()
Agent.dest_address(11)
Agent.set_cd_avg_length(15)
Agent.set_cd_threshold(10)
Agent.si_enable()
time.sleep(3)

print('Retuen Duplexer')
Agent.retune_duplexer(True)
time.sleep(4)
Agent.retune_duplexer(False)

print('Mac Setting for CD training')
Agent.set_mac(1)
time.sleep(4)

#data['IQ_COMPLEX'][0:6]d


print('Train CD')
print('... Reset CD')
Agent.set_collision_detection('reset')
time.sleep(2)
print('... Training')
Agent.set_collision_detection('train')
time.sleep(4)
print('... Fix Alpha')
Agent.set_collision_detection('fix_alpha')
time.sleep(2)
print('... Start CD')
Agent.set_collision_detection('start')
time.sleep(3)
print('Request CD results')
CD_res = Agent.req_cd_result()
print(CD_res)

#Data = bytearray([1,2,3,4])
#Agent.send_payload(Data)

IQ_Data = Agent.req_iq_data()
ReceivedPacket = Agent.req_recv_pkt()




print('Exit!')
Agent.si_disable()
Agent.stop()
