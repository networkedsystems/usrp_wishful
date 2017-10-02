
import datetime
import logging
import wishful_controller
import gevent
import wishful_upis as upis
import time

log = logging.getLogger('wishful_controller')
log_level = logging.DEBUG
logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s.%(funcName)s() - %(levelname)s - %(message)s')

#Create controller
controller = wishful_controller.Controller(dl="tcp://127.0.0.1:8990", ul="tcp://127.0.0.1:8989")

#Configure controller
controller.set_controller_info(name="WishfulController", info="WishfulControllerInfo")

controller.add_module(moduleName="discovery", pyModuleName="wishful_module_discovery_pyre",
                      className="PyreDiscoveryControllerModule", 
                      kwargs={"iface":"lo", "groupName":"wishful_1234", "downlink":"tcp://127.0.0.1:8990", "uplink":"tcp://127.0.0.1:8989"})

#controller.set_controller_info(name="WishfulController", info="WishfulControllerInfo")
nodes = []
@controller.new_node_callback()
def new_node(node):
    nodes.append(node)
    print("added")


#start the radio
controller.run()
while not nodes:
    print("waiting for node")
    time.sleep(1)
    
#set parameters
#nodes[0] can be the list to use all the nodes -> controller.nodes(nodes).radio...
controller.node(nodes[0]).radio.iface("usrp0").set_parameters({'SELF_INT':True})
controller.node(nodes[0]).radio.iface("usrp0").set_parameters({'RETUNE_DUPLEXER':True})

controller.node(nodes[0]).radio.iface("usrp0").set_parameters({'SET_CD':'reset'})
time.sleep(2)
print('... Training')
controller.node(nodes[0]).radio.iface("usrp0").set_parameters({'SET_CD':'train'})
time.sleep(4)
print('... Fix Alpha')
controller.node(nodes[0]).radio.iface("usrp0").set_parameters({'SET_CD':'fix_alpha'})
time.sleep(2)
print('... Start CD')
controller.node(nodes[0]).radio.iface("usrp0").set_parameters({'SET_CD':'start'})
time.sleep(3)
